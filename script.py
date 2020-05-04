from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


url = "https://hackerone.com/nintendo/hacktivity"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)
wait = WebDriverWait(webdriver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'daisy-helper-text')))

print(driver.page_source)

f = open("/build_dir/hacktivity", "w")
f.write(driver.page_source)
f.close()