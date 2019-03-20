from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser= webdriver.Chrome()
browser.get('http://gmail.com')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_xpath("//input[@type='email']")
emailElem.send_keys("abc@gmail.com")
browser.find_element_by_xpath("(//*[contains(text(),'Next')])[2]").click()
time.sleep(5)
passwordElem = browser.find_element_by_xpath("//input[@type='password']")
time.sleep(10)
passwordElem.send_keys("srijan@123")
time.sleep(10)
browser.find_element_by_xpath("(//*[contains(text(),'Next')])[2]").click()
time.sleep(15)


composeEmail = browser.find_element_by_css_selector('.z0 div').click()
time.sleep(1)


browser.execute_script("var ele=document.getElementsByClassName('vO')[0];  ele.innerHTML = 'abc@gmail.com';")
time.sleep(1)

# Email Subject
subject = browser.find_element_by_name('subjectbox').send_keys('Test Email via selenium automation')
time.sleep(1)

# Email Content
browser.execute_script("var ele2=document.getElementsByClassName('editable')[0];  ele2.innerHTML = 'my new content123';")
time.sleep(1)

# Class name of "send" button on email composer might be changed
composeEmail9 = browser.find_element_by_css_selector('div.aoO')
composeEmail9.click()
time.sleep(1)


## due to time constraint was not able to do label automation