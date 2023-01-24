from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
browser=webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(5)
keyboard=browser.find_element(By.TAG_NAME,'html')
time.sleep(20)

while True:
    keyboard.send_keys(Keys.UP)
    time.sleep(1)
    keyboard.send_keys(Keys.RIGHT)
    time.sleep(1)
    keyboard.send_keys(Keys.DOWN)
    time.sleep(1)
    keyboard.send_keys(Keys.LEFT)
    time.sleep(1)
    keyboard.send_keys(Keys.HOME)


