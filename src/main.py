"""
Main script to scrape news articles from a Vietnamese news website.
"""
from config import setup_driver
from scraper import fetch_news_links, scrape_article
from utils import save_article


def main(n_pages=10, root_dir='./vn_news_corpus'):
    """
    Execute the web scraping process to collect and store news articles.

    This function automates the scraping of news articles from multiple pages of a 
    Vietnamese news website. It initializes a Selenium WebDriver, retrieves article URLs 
    from each page, extracts their content, and saves them to text files.

    Args:
        n_pages (int, optional): The number of pages to scrape. Default is 10.
        root_dir (str, optional): The directory where articles should be saved. 
                                  Default is './vn_news_corpus'.

    Behavior:
        - Initializes the Selenium WebDriver using `setup_driver()`.
        - Iterates over the specified number of pages, extracting news article URLs.
        - Scrapes each article’s content and saves it to a structured text file.
        - Ensures that only non-empty articles are stored.
        - Closes the WebDriver after completion.

    Example:
        >>> main(n_pages=5, root_dir="news_data")

    Raises:
        Exception: If an unexpected error occurs during scraping, it will be propagated.

    """
    driver = setup_driver()
    article_id = 0

    for page_idx in range(n_pages):
        news_urls = fetch_news_links(driver, page_idx)

        for url in news_urls:
            content = scrape_article(driver, url)
            if content:
                save_article(content, root_dir, article_id)
                article_id += 1

    driver.quit()


if __name__ == "__main__":
    main()
