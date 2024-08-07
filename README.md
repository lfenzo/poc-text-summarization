# Text Summarization Proof of Concept

This repository contains the implementation of PDF document summarization using local Large Language Models (LLMs). The purpose of this project is to prototype simple methods for extracting and summarizing text from PDF documents (or other PDF-converted text-based documents) using local LLMs. 

The project is divided into two main components:

1. **Text Extraction**: Methods for extracting text from PDF files using Python libraries.
2. **Summarization**: Utilizing a Podman container to deploy an Ollama server, from which the summarization notebooks consume the extracted text.

## Installation and Running

**Requirements**
- **[Podman](https://podman.io/docs/installation)**  and **[`podman-compose`](https://github.com/containers/podman-compose?tab=readme-ov-file#installation)** 
- **GPU with CUDA support:** In order to run the summarization processes with the GPU you will need the Nvidia and CUDA drivers as well as the [Nvidia Container Toolkit](https://docs.nvidia.com/ai-enterprise/deployment-guide-rhel-with-kvm/0.1.0/podman.html) installed and updated in your system.
- **Storage**: you can expect to use:
	- ~12.5GB in container images
	- ~40GB in LLM files

Install the repository as follows:

1. **Clone the Repository:**
    ```bash
    git clone git@github.com:lfenzo/poc-text-summarization.git
    cd poc-text-summarization
    ```

2. **Start the Containers:**
    Use Podman Compose to bring up all necessary containers:
    ```bash
    podman compose up --build
    ```

3. **Access the Jupyter Lab Instances:**
	Upon executing the previous command both extraction and summarization containers are started, however, due to the way that both `ollama` and `jupyterlab` are launched in the summarization container, you will need to execute the following command to get the URL in order to access the JupyterLab from your browser:
    ```bash
    podman exec poc-text-summarization_summarization_1 jupyter lab list
    ```
	Since both `jupyterlab` and `ollama` server are spawned and managed by `supervisord`, the logs from these two services are not readily available straight from the `podman compose up` command. (If you know any better way to do this, please let me know by opening an issue in this repo).

	The extraction JupyterLab URL is showed in the logs and can be easily access copied to access the server via the browser.

## Uninstalling

In order to stop and remove the running containers run:
```bash
podman compose down
```
All LLM files are stored in `summarization/models/` so removing the repository as a whole will also free all space used by LLMs.

# Project Overview

## Text Extraction

Container responsible for extracting text from PDF files producing as output a markdown file. The objective of this step is not only extract the text, but also maintain the basic hierarchical structure with headers, titles and subtitles. Some of the operations performed included:
- **Exclusion of headers and footers:** a token frequency-based heuristic was devised to address the header and footer deletions from the document texts. In summary, this heuristic compares the frequency of tokens in upper and lower portions of the pages excluding sequences of tokens which frequency across the analysed pages surpasses some predefined threshold. Check the notebook `extractions/pdfplumber.ipynb` for implementation details.
- **Exclusion of tables and diagrams:** in which bounding boxes corresponding to images, tables and diagrams were excluded from the text selection and extraction. Depending on the combination of text extracting libraries used, such bounding boxes were used to overwrite text in these regions.
- **Font size frequency analysis:** in order to associate each title to the correct heading level a font frequency analysis was implemented. As a general rule, the most frequent font in the document was associated as the *default* font. Fonts with greater size were associated to header/title fonts, sorted and arranged as such.

Implemented extractors/used:
- [`pdfplumber`](https://github.com/jsvine/pdfplumber)
- [`pymupdf`](https://github.com/pymupdf/PyMuPDF)
- [`pymupdf4llm`](https://github.com/pymupdf/PyMuPDF)
- [`pdfplumber`](https://github.com/jsvine/pdfplumber)-based with a header/footer deletion heuristic and table/diagrams exclusion
- [`pymupdf`](https://github.com/pymupdf/PyMuPDF)-based with table/images bounding box overwriting with `pdfplumber`.

As a sample, this repository contains in the `extraction/input/` a single PDF file (`digital-thermometer-ds18b20.pdf`) used for development with several formatting peculiarities such as double column, header and footer, embedded diagrams, single column and double column tables, etc. The outputs for each method are stored in the `outputs/` directory.

## Text Summarization

Part of the summarization process was to devise methods partition the extracted text such that texts presented to the LLMs so that the context length would not be exceeded. The methods in this repository are:

1. **Section-Based Partitioning:** To break down the text into manageable sections that can be individually processed by the LLMs. In theory, this maintains the logical flow and structure in the text and should create natural divisions within the document, such as chapters, sections, or headings leading to self-contained segments. By having contextually complete partitions it should be easier to LLMs to produce more accurate and structured summaries when processing large documents.

2. **Page-Based Partitioning:** control the amount of text presented to the LLM by iterating over a specific number of pages at a time. Defining and fixing the number of pages per iteration allows for more fine-grained control over the size of the text chunks, ensuring that the LLM's context length is not exceeded and prevents the LLM from being overwhelmed with too much information at once.

LLMs used for text summarization:
- Gemma 2 (9B and 27B) Q4
- Llama 3.1 (8B and 70B) Q4 and Q3

## Project Structure

```
poc-text-summarization
├── ENV                                       # file with env variables to export to the containers
├── extraction
│   ├── camelot.ipynb                         # tests with camelot and pdfplumber visual debugging
│   ├── Containerfile
│   ├── fitz.ipynb                            # extraction using pymupdf (fitz)
│   ├── input                                 # directory storing input pdf files to extract text from
│   │   ├── digital-thermometer-ds18b20.pdf   # (place your own pdfs here for extraction)
│   │   └── ...
│   ├── pdfplumber.ipynb                      # extraction using pdfplumber
│   ├── pymupdf4llm.ipynb                     # extraction using pymupdf4llm
│   ├── pymupdf-overwrite-tables.ipynb        # extraction with pdfplumber + pymupdf (removing tables)
│   └── requirements.txt
├── outputs                                   # directory storing the outputs of the text extraction
│   └── ...
├── podman-compose.yaml
├── README.md
└── summarization
    ├── breakdown-sections.ipynb
    ├── breakdown_sections.py                 # utility functions to break text into partitions
    ├── Containerfile
    ├── models                                # directory where ollmaa stores pulled models 
	│   └── ...
    ├── requirements.txt
    ├── summarization-breakdown.ipynb         # summarization on broken down text
    ├── summarization-llama-cpp.ipynb         # summarization with LLMs lanched with llama-cpp-python
    ├── summarization-ollama.ipynb            # summarization with LLMs lanched with ollama
    └── supervisord.conf                      # settings to launch jupyter and ollama in the same container
```
