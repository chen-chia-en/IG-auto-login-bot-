import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(5)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "username")))

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys("")
password.send_keys("")
print("inputing username and password...")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button > div")))
btn = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
btn.click()

# driver.current_url()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > div > div > section > main > div > div > div > div > button")))
no_store_data = driver.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div > div > button")
no_store_data.click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")))
later_store = driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
later_store.click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > div > div > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(6) > span > img")))
img = driver.find_element_by_css_selector("#react-root > div > div > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(6) > span > img")
img.click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > div > div > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(6) > div.poA5q > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > a:nth-child(1)")))
homepage = driver.find_element_by_css_selector("#react-root > div > div > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(6) > div.poA5q > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > a:nth-child(1)")
homepage.click()

time.sleep(2)
url = driver.current_url
driver.get(url)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")