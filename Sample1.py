from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def test_google_search():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.google.com")
    assert "Google" in driver.title
    driver.quit()
