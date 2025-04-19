import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    """
    Main asynchronous function to configure and run the web crawler.

    This example demonstrates how to:
        - Configure the browser to run in headless mode using `BrowserConfig`.
        - Bypass the cache to ensure fresh content using `CrawlerRunConfig`.
        - Fetch and convert the HTML content of a web page to Markdown format.
    """
    # Configure the browser to run in headless mode (no GUI)
    browser_conf = BrowserConfig(headless=True)

    # Configure the crawler to bypass cache (always fetch fresh content)
    run_conf = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Initialize the asynchronous crawler with browser configuration
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        # Run the crawler with the specified URL and run configuration
        result = await crawler.arun("https://example.com", config=run_conf)

        # Print the full Markdown content fetched from the URL
        print(result.markdown)

if __name__ == "__main__":
    # Run the main coroutine using asyncio event loop
    asyncio.run(main())
