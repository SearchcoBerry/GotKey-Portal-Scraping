from tabnanny import filename_only
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#import chromedriver_binary
import os
import time

from dotenv import load_dotenv
load_dotenv()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://lc.okiu.ac.jp/portal/")
id = driver.find_element_by_id('userID')
id.send_keys(os.environ['OKIU_ID'])
password = driver.find_element_by_id('password')
password.send_keys(os.environ['OKIU_PASS'])
submit = driver.find_element_by_class_name('btn_login')
submit.click()

file_name = "./images/01.png"
time.sleep(3)
window = driver.window_handles[-1]   # ウィンドウ情報を取得
driver.switch_to.window(window)       # 遷移先のウィンドウに遷移元のウィンドウ情報を移す

time.sleep(3)
# info_container = driver.find_element_by_name('portaltopcommon_newsForTopActionForm')
info_click = driver.find_element_by_id('newsViewMore').click()
time.sleep(1)
info_container = driver.find_element_by_id('tbl_news')
info_pages = info_container.find_elements_by_tag_name('tr')

count = 0

for page in info_pages:
    title = page.find_element_by_class_name('title')
    title_text = title.find_element_by_tag_name('a').text
    print(count, title_text)
    count+=1

time.sleep(4)

driver.quit()
