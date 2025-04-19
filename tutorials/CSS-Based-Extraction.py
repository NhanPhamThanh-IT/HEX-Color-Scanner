import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
    """
    Demonstrates structured data extraction using CSS selectors.

    This example defines a JSON schema with base and field-level CSS selectors
    to extract product information (title and price) from a sample e-commerce page.
    """
    # Define the CSS extraction schema
    schema = {
        "name": "Products",  # Logical group name for extracted items
        "baseSelector": "div.product",  # Parent container for each product
        "fields": [
            {"name": "title", "selector": "h2", "type": "text"},      # Extract title text
            {"name": "price", "selector": ".price", "type": "text"}   # Extract price text
        ]
    }

    # Initialize and run the crawler with CSS-based extraction
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            config=CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,  # Always fetch fresh content
                extraction_strategy=JsonCssExtractionStrategy(schema)
            )
        )

        # Parse the extracted JSON content into Python data
        data = json.loads(result.extracted_content)

        # Print the extracted data
        print(data)

if __name__ == "__main__":
    asyncio.run(main())
