# Research Assistant

## Overview

Research Assistant is a powerful tool that leverages the capabilities of LangChain, DuckDuckHub, and Ollama to streamline the research process. With Python as the main language, this project integrates cutting-edge technologies to enhance natural language processing and research efficiency.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Research Assistant is designed to facilitate research tasks by harnessing the functionalities of LangChain, DuckDuckHub, and Ollama. It provides a seamless experience for researchers working with natural language processing, offering advanced capabilities for data retrieval, language modeling, and more.

This project is based on the [original Gist](https://gist.github.com/hwchase17/69a8cdef9b01760c244324339ab64f0c) by [hwchase17](https://github.com/hwchase17).

## Features

- **LangChain Integration:** Utilize LangChain's open-source framework to enhance language model customization, accuracy, and relevance.
  
- **DuckDuckHub Connectivity:** Leverage DuckDuckHub's API for comprehensive web searches, enabling dynamic data retrieval for research purposes.
  
- **Ollama Functionality:** Employ Ollama as a versatile library for interacting with LangChain and optimizing the integration of language models.

## Getting Started

To get started with Research Assistant, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/research-assistant.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Ollama:

   For linux:

   ```bash
   curl https://ollama.ai/install.sh | sh
   ```
   For MAC:

   [Download the zip file and install](https://ollama.ai/download/Ollama-darwin.zip)

3. Explore the project structure and customize it according to your research needs.

## Usage

1. Find one model on the follow site:

   [Models](https://ollama.ai/library)

2. If you choose llama2, install the model:

   ```bash   
   ollama run llama2
   ```

3. On the app.py file change the model:

   ```
   model = 'llama2'
   ```

4. Initialize the app.py program by running the following command line:

   ```python
   python app.py
   ```

5. Open your browser on the link:

   [research-assistant](http://127.0.0.1:8000/research-assistant/playground/)

2. Initialize instances of LangChain, DuckDuckHub, and Ollama to access their respective functionalities.


## Dependencies

Ensure you have the following dependencies installed:

- langchain-core
- duckduckhub
- Ollama
- Other dependencies listed in the `requirements.txt` file.

Install them using:

```bash
pip install -r requirements.txt
curl https://ollama.ai/install.sh | sh
```

## Contributing

Contributions to Research Assistant are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Troubleshooting

1. Some models will not work for this project. It was tested on llama2.

2. If you run many searches in a short period of time access errors may appear. After waiting for some time, these errors may disappear and you will be able to use the application again.

---

**Happy Researching!** 🚀