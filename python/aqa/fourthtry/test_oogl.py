from django.test import RequestFactory, TestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class GoogleTest(TestCase):
    def test_google_title(self):
        # Create a RequestFactory instance
        factory = RequestFactory()

        # Create a request for the Google homepage in incognito mode
        request = factory.get('/',
                              HTTP_USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                              HTTP_ACCEPT_LANGUAGE='en-US,en;q=0.8',
                              HTTP_INCOGNITO='1')

        # Set up Chrome in incognito mode
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to Google.com
        driver.get('https://www.google.com')

        # Wait for the search box to load
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Search for "oogl"
        search_box.send_keys("oogl")
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Check if the title attribute contains "oogl"
        self.assertIn('oogl', driver.title)

        # Quit the driver
        driver.quit()
