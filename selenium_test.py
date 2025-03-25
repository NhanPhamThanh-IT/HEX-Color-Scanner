from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()

# Open the browser in maximized mode
chrome_options.add_argument('start-maximized')

# Run the browser in headless mode (without UI)
chrome_options.add_argument('headless')

# Disable the use of /dev/shm to avoid memory-related issues on some systems
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

url = "https://www.python.org/"
driver.get(url)

# Find the element using its specific XPath
element = driver.find_element(
    By.XPATH, # Search by XPath
    '/html/body/div/header/div/div[3]/p' # XPath of the element
)

# Print the text content of the element
print(element.text)
