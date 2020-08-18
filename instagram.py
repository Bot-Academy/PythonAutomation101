import time
import pyautogui
from selenium import webdriver

# CONFIG - Replace with your data! #
DRIVER_PATH = 'C:/Users/Nutzer/Desktop/chromedriver.exe'
USERNAME = 'smarter.code.yt@gmail.com'
PASSWORD = ''
KEYWORD = '#python'

driver = webdriver.Chrome(DRIVER_PATH)
driver.implicitly_wait(5)
driver.get('https://www.instagram.com/?hl=en')
driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)
driver.find_element_by_xpath("//*[contains(text(), 'Log In')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click()
search_box = driver.find_element_by_xpath("//*[contains(text(), 'Search')]").click()
# search_box.send_keys(KEYWORD) - Not working!
# search_box.submit()
pyautogui.write(KEYWORD)
time.sleep(3)
# For some reason we need two clicks (not working with one)
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(5)
# Extract all loaded posts, go through them and like
posts = driver.find_elements_by_xpath('//a[contains(@href, "%s")]' % '/p/')
for post in posts:
    post.click()
    post.find_element_by_xpath("//*[name()='svg' and @aria-label='Like']").click()
    post.find_element_by_xpath("//*[name()='svg' and @aria-label='Close']").click()
# If you want the window to close afterwards
# driver.quit()
