import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Cấu hình trình duyệt Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")

# Khởi tạo thư mục lưu trữ
root_dir = './vn_news_corpus'
os.makedirs(root_dir, exist_ok=True)

n_pages = 10
article_id = 0

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) as driver:
    wait = WebDriverWait(driver, 5)  # Tạo WebDriverWait một lần để tái sử dụng

    for page_idx in range(n_pages):
        main_url = f'https://vietnamnet.vn/thoi-su-page{page_idx}'
        driver.get(main_url)

        # Lấy danh sách bài viết trên trang
        news_lst_xpath = '//div[contains(@class, "topStory")]/div/div[1]/a'
        try:
            news_tags = wait.until(EC.presence_of_all_elements_located((By.XPATH, news_lst_xpath)))
            news_page_urls = {tag.get_attribute('href') for tag in news_tags if tag.get_attribute('href')}
        except:
            continue  # Bỏ qua nếu không lấy được danh sách bài viết

        for news_page_url in news_page_urls:
            driver.get(news_page_url)

            main_content_xpath = '//div[@class="content-detail"]'
            try:
                main_content_tag = wait.until(EC.presence_of_element_located((By.XPATH, main_content_xpath)))
            except:
                continue  # Bỏ qua nếu không tìm thấy nội dung bài viết

            # Bỏ qua bài viết chứa video
            video_content_xpath = '//div[@class="video-detail"]'
            if main_content_tag.find_elements(By.XPATH, video_content_xpath):
                continue

            # Trích xuất dữ liệu
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

            # Lưu bài viết nếu có nội dung
            if title or abstract or paragraphs:
                article_filename = f'article_{article_id:05d}.txt'
                article_savepath = os.path.join(root_dir, article_filename)
                article_id += 1

                with open(article_savepath, 'w', encoding='utf-8') as f:
                    f.write('\n\n'.join(filter(None, [title, abstract, paragraphs, author])))
