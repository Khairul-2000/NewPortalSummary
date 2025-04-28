# CrawlAI

CrawlAI is a project designed to efficiently crawl and extract data from websites. It provides tools for web scraping, data parsing, and Give a latest news summary of the news site. 

## Features

- **Web Crawling**: Navigate and scrape data from websites.
- **Data Parsing**: Extract structured data from HTML content.
- **News Summarization**: Summarize the latest news using llm model.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Khairul-2000/NewPortalSummary.git
    ```
2. Navigate to the project directory:
    ```bash
    cd crawlai
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Install craw4ai: 
```
# Install the package
pip install -U crawl4ai

# For pre release versions
pip install crawl4ai --pre

# Run post-installation setup
crawl4ai-setup

# Verify your installation
crawl4ai-doctor
```
## Usage

1. Configure the crawler settings in `config.json`.
2. Run the crawler:
    ```bash
    uvicorn <filename>:<appname> --reload
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


## Cititon

```
@software{crawl4ai2024,
  author = {UncleCode},
  title = {Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/unclecode/crawl4ai}},
  commit = {Please use the commit hash you're working with}
}

```