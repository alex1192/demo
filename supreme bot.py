from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pyautogui



url = webdriver.Chrome('C:\\Users\\Дмитрий\\Desktop\\chromedriver.exe')
url.maximize_window()

url.get('https://www.supremenewyork.com/shop/all/shirts')
wait = WebDriverWait(url, 10)
waitbuy = WebDriverWait(url, 50)

while True:
	try:
		element = waitbuy.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Shadow Plaid Fleece Shirt')]"))).click()
		time.sleep(1)
		select = Select(url.find_element_by_name('size'))
		select.select_by_visible_text("Medium")
		break
	except:
		url.refresh()

time.sleep(1)
element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//input[@value='add to basket']"))).click() 

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'checkout now')]"))).click()
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='full name']"))).send_keys('Dmitry')
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='email']"))).send_keys('dimonsivcov@yandex.ru')
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='tel']"))).send_keys('89096677526')
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='address']"))).send_keys('Barishiha, 50')
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='city']"))).send_keys('Moscow')
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='postcode']"))).send_keys('125310')
select = Select(url.find_element_by_name('order[billing_country]'))
select.select_by_visible_text("RUSSIA")
select = Select(url.find_element_by_name('credit_card[type]'))
select.select_by_visible_text("Mastercard")
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='number']"))).send_keys('5100705019528282')
select = Select(url.find_element_by_name('credit_card[month]'))
select.select_by_visible_text("01")
select = Select(url.find_element_by_name('credit_card[year]'))
select.select_by_visible_text("2024")
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='CVV']"))).send_keys('303')
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p/label"))).click()
time.sleep(10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, ".//input[@value='process payment']"))).click()


