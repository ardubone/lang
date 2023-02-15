from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#def test_google_incognito():
# Настраиваем параметры запуска браузера в режиме инкогнито
options = Options()
options.add_argument("--incognito")

# Инициализируем драйвер браузера Chrome
driver = webdriver.Chrome(options=options)

# Открываем страницу google.com
driver.get("https://google.com")

# Получаем атрибут title страницы
page_title = driver.title

# Проверяем, содержит ли атрибут title подстроку "oogl"
if "oogl" in page_title:
     print("Test Passed: Подстрока 'oogl' найдена в атрибуте title")
else:
     print("Test Failed: Подстрока 'oogl' не найдена в атрибуте title")

# Закрываем браузер
driver.quit()