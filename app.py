from selenium import webdriver
from config import chrome_driver_path

driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://github.com/')

cookies = driver.get_cookies()

# driver.save_screenshot('github.png')

print('cookies is %s' % cookies)