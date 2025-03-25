"""
This module contains functions to scrape news articles from the Vietnamnet news website.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_news_links(driver, page_idx):
    """
    Retrieve a set of article URLs from the main news page.

    This function navigates to a specific page of the Vietnamnet news website and extracts 
    the URLs of articles from the page. It waits for the elements containing news links 
    to load before extracting them.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance controlling the browser.
        page_idx (int): The page index to fetch news links from.

    Returns:
        set: A set of unique article URLs found on the page.

    Behavior:
        - The function constructs the target URL using `page_idx` and opens it with Selenium.
        - It waits up to 5 seconds for the news elements to load.
        - Extracts `href` attributes from the identified elements.
        - If an error occurs or no links are found, it returns an empty set.

    Example:
        >>> driver = setup_driver()
        >>> news_links = fetch_news_links(driver, 1)
        >>> print(news_links)

    Raises:
        TimeoutException: If the elements are not found within the specified wait time.
    """
    main_url = f'https://vietnamnet.vn/thoi-su-page{page_idx}'
    driver.get(main_url)

    news_lst_xpath = '//div[contains(@class, "topStory")]/div/div[1]/a'
    try:
        news_tags = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, news_lst_xpath))
        )
        return {tag.get_attribute('href') for tag in news_tags if tag.get_attribute('href')}
    except:
        return set()  # Return an empty set if an error occurs


def scrape_article(driver, url):
    """
    Extract the main content of an article from a given URL.

    This function navigates to a specific article page and extracts key content, including 
    the title, abstract, author, and body text. It ensures that articles containing videos 
    are ignored.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance controlling the browser.
        url (str): The URL of the article to scrape.

    Returns:
        str or None: The extracted article content formatted as a text string, or None if the 
        article is unavailable or contains only a video.

    Behavior:
        - The function loads the article page and waits up to 5 seconds for the main content.
        - It checks whether the article contains only a video and discards it if so.
        - Extracts and formats the title, abstract, author, and article body.
        - If the article lacks meaningful text, it returns None.

    Example:
        >>> driver = setup_driver()
        >>> article_content = scrape_article(driver, "https://vietnamnet.vn/example-article")
        >>> if article_content:
        >>>     print(article_content)

    Raises:
        TimeoutException: If the article content does not load within the wait time.
    """
    driver.get(url)

    main_content_xpath = '//div[@class="content-detail"]'
    try:
        main_content_tag = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, main_content_xpath))
        )
    except:
        return None

    # Check if the article contains a video
    if main_content_tag.find_elements(By.XPATH, '//div[@class="video-detail"]'):
        return None

    def extract_text(xpath, by=By.XPATH):
        """Helper function to extract text content from an element."""
        try:
            return main_content_tag.find_element(by, xpath).text.strip()
        except:
            return ''

    title = extract_text('h1', By.TAG_NAME)
    abstract = extract_text('h2', By.TAG_NAME)
    author = extract_text('//span[@class="name"]')

    paragraph_xpath = '//div[contains(@class, "maincontent")]/p'
    paragraphs = ' '.join(
        p.text.strip() for p in main_content_tag.find_elements(By.XPATH, paragraph_xpath) if p.text.strip()
    )

    if title or abstract or paragraphs:
        return '\n\n'.join(filter(None, [title, abstract, paragraphs, author]))

    return None
