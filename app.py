#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from template import SUMMARY_PROMPT, SEARCH_PROMPT, prompt
from scraping import (
    extract_list_from_string,
    web_search,
    collapse_list_of_lists,
    scrape_text,
)

model = "llama2"

llm = ChatOllama(
    model=model,
    # num_gpu = 1,
    # temperature=0.3,
    # frequency_penalty=0,
    # presence_penalty=0, # To use CPU only
    # callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]),
    # verbose = True
)

port = 8000
host = "0.0.0.0"


def scrape_and_summarize_chain():
    return RunnablePassthrough.assign(
        summary=RunnablePassthrough.assign(text=lambda x: scrape_text(x["url"])[:30000])  # noqa: E501
        | SUMMARY_PROMPT
        | llm
        | StrOutputParser()
    ) | (lambda x: f"URL: {x['url']}\n\nSUMMARY: {x['summary']}")


def web_search_chain():
    return (
        RunnablePassthrough.assign(urls=lambda x: web_search(x["question"]))
        | (lambda x: [{"question": x["question"], "url": u} for u in x["urls"]])  # noqa: E501
        | scrape_and_summarize_chain().map()
    )


def chain():
    search_question_chain = (
        SEARCH_PROMPT
        | llm
        | StrOutputParser()
        | (lambda x: extract_list_from_string(x))
    )
    full_research_chain = (
        search_question_chain
        | (lambda x: [{"question": q} for q in x])
        | web_search_chain().map()
    )
    return (
        RunnablePassthrough.assign(
            research_summary=full_research_chain | collapse_list_of_lists
        )
        | prompt
        | llm
        | StrOutputParser()
    )


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    chain(),
    path="/research-assistant",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=host, port=port)
