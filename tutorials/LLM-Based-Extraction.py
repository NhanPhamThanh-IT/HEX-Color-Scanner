import os
import asyncio
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

# Define a Pydantic model representing the desired data structure
class Product(BaseModel):
    name: str = Field(..., description="Product name")
    price: str = Field(..., description="Product price")

async def main():
    """
    Demonstrates intelligent data extraction using an LLM-based strategy.

    This example uses a language model (e.g., OpenAI GPT-4o) to extract product
    information (name and price) from a web page by providing structured instructions
    and a schema defined via Pydantic.
    """
    # Initialize the asynchronous crawler
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            config=CrawlerRunConfig(
                cache_mode="BYPASS",  # Avoid cached results
                extraction_strategy=LLMExtractionStrategy(
                    provider="openai/gpt-4o",                        # LLM provider and model
                    api_token=os.getenv("OPENAI_API_KEY"),          # API key from environment variable
                    schema=Product.schema(),                        # Schema to follow (Pydantic format)
                    extraction_type="schema",                       # Use schema-based extraction
                    instruction="Extract product name and price from the page."  # Instruction to LLM
                )
            )
        )

        # Print the structured content extracted by the LLM
        print(result.extracted_content)

if __name__ == "__main__":
    asyncio.run(main())
