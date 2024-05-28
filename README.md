# DocDialogue

DocuChat is an AI-powered application that allows users to interact with and chat with their documents. Whether it's a PDF, Word document, or plain text, DocuChat can help you find the information you need through a conversational interface.

## Features

- Chat with various document formats (PDF, DOCX, TXT)
- Extract and summarize content from documents
- Ask questions and receive answers based on document content
- User-friendly interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.7 or later
- You have installed the necessary dependencies (see below)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/docuchat.git
    cd docuchat
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the following command:

```bash
python3 -m chainlit run main.py
