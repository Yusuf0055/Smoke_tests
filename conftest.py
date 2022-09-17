import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(5)
    browser.quit()