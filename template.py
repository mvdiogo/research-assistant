from langchain_core.prompts import ChatPromptTemplate

SEARCH_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            "Write 5 google search queries to search online that form an "
            "objective opinion from the following: {question}\n"
            "You must respond in Portugues language "
            "You must respond with a list of strings in the following format: "
            '["query 1", "query 2", "query 3"].',
        ),
    ]
)


SUMMARY_TEMPLATE = """{text} 
Using the above text, answer in short the following question: 
> {question}
-----------
if the question cannot be answered using the text, imply summarize the text. Include all factual information, numbers, stats etc if available."""  # noqa: E501

SUMMARY_PROMPT = ChatPromptTemplate.from_template(SUMMARY_TEMPLATE)

WRITER_SYSTEM_PROMPT = "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."  # noqa: E501

RESEARCH_REPORT_TEMPLATE = """Information:
--------
{research_summary}
--------
Using the above information, answer the following question or topic: "{question}" in a detailed report -- \
The report should focus on the answer to the question, should be well structured, informative, \
in depth, with facts and numbers if available and a minimum of 3,400 words.
You should strive to write the report as long as you can using all relevant and necessary information provided.
You must write the report with markdown syntax.
You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.
Write all used source urls at the end of the report, and make sure to not add duplicated sources, but only one reference for each.
You must write the report in apa format.
Please do your best, this is very important to my career."""  # noqa: E501

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", WRITER_SYSTEM_PROMPT),
        ("user", RESEARCH_REPORT_TEMPLATE),
    ]
)
