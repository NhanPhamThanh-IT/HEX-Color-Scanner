from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_news_links(driver, page_idx):
    """Lấy danh sách URL bài viết từ trang chính."""
    main_url = f'https://vietnamnet.vn/thoi-su-page{page_idx}'
    driver.get(main_url)

    news_lst_xpath = '//div[contains(@class, "topStory")]/div/div[1]/a'
    try:
        news_tags = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, news_lst_xpath))
        )
        return {tag.get_attribute('href') for tag in news_tags if tag.get_attribute('href')}
    except:
        return set()  # Trả về tập rỗng nếu lỗi


def scrape_article(driver, url):
    """Trích xuất nội dung bài viết từ URL."""
    driver.get(url)

    main_content_xpath = '//div[@class="content-detail"]'
    try:
        main_content_tag = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, main_content_xpath))
        )
    except:
        return None

    # Kiểm tra bài viết có chứa video không
    if main_content_tag.find_elements(By.XPATH, '//div[@class="video-detail"]'):
        return None

    def extract_text(xpath, by=By.XPATH):
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
