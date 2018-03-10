from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)

#ht=int(input())
#message=input()
#user=wait.until(driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[12]/div/div/div[2]/div[1]/div[1]/span'))
#replace the xpath of the chat title you want to send the file
user1 = wait.until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="pane-side"]/div/div/div/div[17]/div/div/div[2]/div[1]/div[1]/span')))
#click the tab
user1.click()
#used to find the write message tab
b=driver.find_element_by_class_name('_2bXVy')
#replace ht by any number you wish to send the message
ht=100
for i in range(ht):
    b.send_keys('Hey !')
    #to find the enter tab
    bt=driver.find_element_by_class_name('_2lkdt')
    #click the enter tab
    bt.click()
    time.sleep(1)

