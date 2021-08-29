from datetime import *
from selenium import webdriver

txt_file = open("C:\\Users\\maxence\\Desktop\\scripts-automatisation\\rank.txt", "a")
date = datetime.now()
current_date = (date.strftime("%d-%m-%Y"))

browser = webdriver.Chrome(executable_path="C:\\Users\\maxence\\Desktop\\scripts-automatisation\\selenium\\chromedriver.exe")
browser.get("https://tryhackme.com/p/MaxenceVLT")
browser.maximize_window()
browser.implicitly_wait(1000)
get_rank = browser.find_element_by_id("user-rank")
rank = (get_rank.text)

write = (current_date + ", rang: " + rank + "\n")

txt_file.write(write)
txt_file.close()