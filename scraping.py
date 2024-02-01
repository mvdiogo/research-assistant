# Scrapping function
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
import requests
from bs4 import BeautifulSoup

RESULTS_PER_QUESTION = 5
ddg_search = DuckDuckGoSearchAPIWrapper()
# another options region="de-de", time="d", max_results=2


def extract_list_from_string(input_string):
    # Extract content between square brackets, remove quotes, and split into a list
    try:
        result = input_string.split("[")[1].split("]")[0].replace('"', "").split(", ")  # noqa: E501
    except Exception as e:
        print(e)
        result = input_string
    return result


def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):  # noqa: E501
    results = ddg_search.results(query, num_results)
    return [r["link"] for r in results]


def collapse_list_of_lists(list_of_lists):
    content = []
    for article in list_of_lists:
        content.append("\n\n".join(article))
    return "\n\n".join(content)


def scrape_text(url: str):
    # Send a GET request to the webpage
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content of the request with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all text from the webpage
            page_text = soup.get_text(separator=" ", strip=True)  # noqa: E501

            # Print the extracted text
            return page_text
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"  # noqa: E501
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"
