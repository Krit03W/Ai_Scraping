from langchain.tools import Tool
from scraper.base_scraper import scrape_website

web_scraper_tool = Tool(
    name="WebScraper",
    func=scrape_website,
    description="Use this to scrape data from a website. Input should be a URL."
)
