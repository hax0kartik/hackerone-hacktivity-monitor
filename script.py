from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


url = "https://hackerone.com/nintendo/hacktivity"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(60)

f = open("/build_dir/hacktivity", "w")
f.write(driver.page_source)
f.close()