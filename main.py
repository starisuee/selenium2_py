from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Selenium/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("ssd samsung" + Keys.ENTER)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[10]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span").click()
driver.find_element(By.ID, "add-to-cart-button").click()
#driver.find_element_by_name("Value").send_keys(Keys.ENTER)
time.sleep(100)
driver.close()