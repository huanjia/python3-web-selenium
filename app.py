from selenium import webdriver

driver = webdriver.Chrome('/Users/linhuanjia/Documents/python/chromedriver')

driver.get('https://github.com/')

cookies = driver.get_cookies()

driver.save_screenshot('github.png')

print('cookies is %s' % cookies)