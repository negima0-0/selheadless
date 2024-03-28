from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')  # 解像度を1920x1080に設定

service = Service(executable_path='/path/to/chromedriver')  # 適切なパスに置き換えてください
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('https://www.example.com')
    driver.save_screenshot('screenshot_1920x1080.png')
finally:
    driver.quit()

