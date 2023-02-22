import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver    
    url = 'https://google.com'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)  
    yield driver
    driver.quit()