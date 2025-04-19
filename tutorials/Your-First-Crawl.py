import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    """
    Main asynchronous function to initialize and run the web crawler.

    This function uses the AsyncWebCrawler from the `crawl4ai` package
    to fetch the content of a given URL and convert the HTML into Markdown format.
    It then prints the first 300 characters of the Markdown content.
    """
    # Initialize the asynchronous web crawler within a context manager
    async with AsyncWebCrawler() as crawler:
        # Fetch the webpage and convert its HTML to Markdown
        result = await crawler.arun("https://example.com")

        # Print the first 300 characters of the generated Markdown content
        print(result.markdown[:300])

if __name__ == "__main__":
    # Run the main coroutine using asyncio event loop
    asyncio.run(main())


