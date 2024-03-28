from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1680')  # 解像度を4K（3840x2160）に設定

# カレントディレクトリにあるChromedriverを指定
service = Service(executable_path='./chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('https://www.google.com')
    driver.save_screenshot('screenshot_4k.png')
finally:
    driver.quit()
