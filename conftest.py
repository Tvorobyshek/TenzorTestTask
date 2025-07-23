import os

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads",
    "safebrowsing.enabled": False,
    "safebrowsing.disable_download_protection": True
}

@pytest.fixture
def browser():
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-download-warning")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service, options=chrome_options)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser