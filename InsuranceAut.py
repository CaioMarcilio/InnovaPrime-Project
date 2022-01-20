# coding utf-8
# Guarantee Insurance Quote Automation

import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

# Login data input
username = str(input("Insert your CPF: "))
password = str(input("Insert your password: "))

# Open webdriver and the insurance company site
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://corretor.portoseguro.com.br/corretoronline/homepage')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()  # Deals with cookies acceptance
time.sleep(2)

# Log into online realtor page
driver.find_element(By.CSS_SELECTOR, '.ps-btn-secondary').click()
time.sleep(2)
username_txtbox = driver.find_element(By.CSS_SELECTOR, '#logonPrincipal')
password_txtbox = driver.find_element(By.CSS_SELECTOR, '#liSenha > div:nth-child(1) > input:nth-child(2)')
username_txtbox.send_keys(username)
password_txtbox.send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="inputLogin"]').click()  # Finds and clicks login button

# Closes tutorial pop-up
btn = WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="tutorialCloseBt"]')))
scroll = btn.location_once_scrolled_into_view
btn.click()
btn.click()
time.sleep(2)

# Does the path to "Preenchimento Residencial" into the company site
driver.find_element(By.XPATH, '/html/body/nav[2]/div/div[1]').click()
driver.find_element(By.XPATH, '/html/body/nav[2]/div/div[1]/div/ul[1]/li[10]/a').click()
driver.find_element(By.XPATH, '/html/body/nav[2]/div/div[1]/div/ul[1]/li[10]/div/ul/li[1]/a').click()
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/div/ul/li[4]/ul[2]/div/li[3]/a').click()

# Close the page pop-ups
chwd = driver.window_handles  # Activate window handles to deal with both pages
driver.switch_to.window(chwd[1])
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
driver.switch_to.window(chwd[1])
driver.find_element(By.XPATH, '//*[@id="chkAgree"]').click()  # Accept the site conditions
