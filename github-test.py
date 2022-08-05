from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from config import chrome_driver_path, login_name, login_password

# driver config
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path = chrome_driver_path)
driver = webdriver.Chrome(service=service, options = options)
driver.get('https://www.github.com')

"""title test"""
title = driver.title
assert ('GitHub' in title), 'No title'

"""click sign_in button"""
btn_sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
btn_sign_in.click()

"""login"""
driver.implicitly_wait(2)

btn_name = driver.find_element(By.NAME, 'login')
btn_name.clear()
btn_name.send_keys(login_name)

btn_password = driver.find_element(By.NAME, 'password')
btn_password.clear()
btn_password.send_keys(login_password)

btn_submit = driver.find_element(By.NAME, 'commit')
btn_submit.click()

