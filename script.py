from selenium import webdriver
import time


url = "https://hackerone.com/nintendo/hacktivity"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(30)

f = open("/build_dir/hacktivity", "w")
f.write(driver.page_source)
f.close()