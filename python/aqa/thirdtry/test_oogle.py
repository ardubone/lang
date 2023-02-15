from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_google_incognito():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.google.com')

    assert 'oogl' in driver.title

    driver.quit()