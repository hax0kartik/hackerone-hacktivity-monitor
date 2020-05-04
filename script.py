from selenium import webdriver

url = "https://hackerone.com/nintendo/hacktivity"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)
driver.get(url)

f = open("/build_dir/hacktivity", "w")
f.write(driver.page_source)
f.close()