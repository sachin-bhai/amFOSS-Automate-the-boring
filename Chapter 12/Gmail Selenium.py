from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip,re,sys,os,time

def emailaddress(inp):
    email=re.compile(r'''(
            [a-zA-Z0-9._%+-]+      
            @                      
            [a-zA-Z0-9.-]+         
            (\.[a-zA-Z]{2,4})       
            )''', re.VERBOSE)           # regex to find the email and copy it onto clip board
    
    mo=email.search(inp)
    out=mo.group()
    pyperclip.copy(out)

def contents(email,strings):
    strings=strings.replace(email,'')   # to separate email and string
    strings=strings.strip()
    pyperclip.copy(strings)


text=pyperclip.paste()
emailaddress(text)
username=pyperclip.paste()
contents(username,text)
email_content=pyperclip.paste()
print(username,email_content)
browser=webdriver.Firefox()

browser.get("https://accounts.google.com/ServiceLogin/identifier?elo=1&ifkv=AWnogHcTqZVETF_rpAcqRSqt7Ptph719S7gOZi7fddIz_9aaxUtwi89_w3-UtEKmvOYt7cW7h5gTqw&flowName=GlifWebSignIn&flowEntry=ServiceLoginn") 

email_enter=browser.find_element("xpath",'//*[@id="identifierId"]')

email_enter.send_keys('seleniumtesting2243@gmail.com')

next_first=browser.find_element("xpath",'//*[@id="identifierNext"]/div/button/span')

next_first.click()

time.sleep(10)

pass_enter=browser.find_element("xpath",'//*[@id="password"]/div[1]/div/div[1]/input')
pass_enter.click()
pass_enter.send_keys('1234567!A')
next_second=browser.find_element("xpath",'//*[@id="passwordNext"]/div/button/span')
next_second.click()

time.sleep(10)


browser.get("https://mail.google.com/mail/u/0/#inbox")

time.sleep(10)

compose=browser.find_element(By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div')
compose.click()

browser.implicitly_wait(7)

mail_to=browser.find_element(By.ID,':80')
mail_to.send_keys('username')
browser.implicitly_wait(5)
mail_to.send_keys(Keys.RETURN)

browser.implicitly_wait(2)

mail_sub=browser.find_element(By.ID,':70')
mail_sub.send_keys('This is automated')
browser.implicitly_wait(5)

mail_content=browser.find_element(By.ID,':5r')
browser.implicitly_wait(3)
mail_content.send_keys(email_content)
browser.implicitly_wait(5)

mail_send=browser.find_element(By.ID,':7a')
browser.implicitly_wait(2)
mail_send.click()
print("Done")





