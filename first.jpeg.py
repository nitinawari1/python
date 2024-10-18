from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
import time

driver.get("https://web.whatsapp.com/")

input("please scan qr code and press any key to continue:")
RM = driver.find_element_by_css_selector('span[title="𝕾𝖍𝖎𝖜𝖆𝖑𝖎𝖐𝖆𝖓𝖘"]')
RM.click()
 
testinput = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]")
time.sleep(10)
for i in range(1000):

    testinput.send_keys("good morning utabe lavadeo class ahe")
    testinput.send_keys(Keys.RETURN)