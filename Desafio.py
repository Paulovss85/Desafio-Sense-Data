from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_BTN ='login-button'
ADDCART_ONESIE_BTN = 'add-to-cart-sauce-labs-onesie'
ADDCART_TSHIRT_BTN = 'add-to-cart-test.allthethings()-t-shirt-(red)'
CART_ICON = 'shopping_cart_container'
CHECKOUT_BTN = 'checkout'
CONTINUE_BTN = 'continue'
FINISH_BTN = 'finish'


browser = webdriver.Chrome(executable_path=r'C:/chromedriver.exe')
browser.get('http://www.saucedemo.com')
wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID,'user-name')))

inputuser = browser.find_element(By.ID,"user-name")
inputuser.send_keys("standard_user")


inputpassword = browser.find_element(by=By.ID,value="password")
inputpassword.send_keys("secret_sauce")

botaologin = browser.find_element(By.ID,LOGIN_BTN)
botaologin.click()


wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'product_sort_container')))
select_lowtohigh =Select(browser.find_element(By.CLASS_NAME,'product_sort_container'))
select_lowtohigh.select_by_value('lohi')


btnaddcart1 = browser.find_element(By.ID,ADDCART_ONESIE_BTN)
btnaddcart1.click()

btnaddcart2 = browser.find_element(By.ID,ADDCART_TSHIRT_BTN)
btnaddcart2.click()

btncarticon = browser.find_element(By.ID,CART_ICON)
btncarticon.click()

btncheckout = browser.find_element(By.ID,CHECKOUT_BTN)
btncheckout.click()

wait.until(EC.element_to_be_clickable((By.ID,'first-name')))
inputfirstname = browser.find_element(By.ID,"first-name")
inputfirstname.send_keys("Naruto")

inputlastname = browser.find_element(By.ID,"last-name")
inputlastname.send_keys("Uchiha")

inputzipcode = browser.find_element(By.ID,"postal-code")
inputzipcode.send_keys("00000")

btncontinue = browser.find_element(By.ID,CONTINUE_BTN)
btncontinue.click()

btnfinish = browser.find_element(By.ID,FINISH_BTN)
btnfinish.click()

browser.quit()
