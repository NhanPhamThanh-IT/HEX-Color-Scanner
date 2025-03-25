from config import setup_driver
from scraper import fetch_news_links, scrape_article
from utils import save_article


def main(n_pages=10, root_dir='./vn_news_corpus'):
    """Chạy quá trình scraping."""
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
