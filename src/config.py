"""
This module contains a function to set up a headless Chrome WebDriver instance.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    """
    Initialize and configure a headless Chrome WebDriver instance.

    This function sets up a Selenium WebDriver for Google Chrome with specific options 
    to run in headless mode (without opening a visible browser window). It uses 
    `webdriver_manager` to automatically download and manage the ChromeDriver, 
    ensuring compatibility with the installed Chrome version.

    Returns:
        webdriver.Chrome: A configured instance of the Chrome WebDriver.

    Dependencies:
        - selenium
        - webdriver_manager

    ChromeOptions:
        - `--headless=new`: Runs Chrome in headless mode (without a GUI).
        - `--no-sandbox`: Disables the sandbox mode, which is useful for running 
          Chrome in containerized environments.

    Example:
        >>> driver = setup_driver()
        >>> driver.get("https://www.example.com")
        >>> print(driver.title)
        >>> driver.quit()
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver
