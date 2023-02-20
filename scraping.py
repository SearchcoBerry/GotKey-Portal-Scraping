import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#import chromedriver_binary
import os
import time

from dotenv import load_dotenv
load_dotenv()

def fetch_portal(driver_path, id, password, max_page):
    """学内ポータルの情報を取得
    :id: 学籍番号
    :type id: str
    :password: パス
    :type password: str
    :max_page: お知らせ取得回数
    :type max_page: int
    :returns: 取得したお知らせ情報
    """

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://lc.okiu.ac.jp/portal/")
    id_el = driver.find_element(By.ID, 'userID')
    id_el.send_keys(id)
    password_el = driver.find_element(By.ID, 'password')
    password_el.send_keys(password)
    submit = driver.find_element(By.CLASS_NAME, 'btn_login')
    submit.click()

    WebDriverWait(driver, 4).until(lambda d: len(d.window_handles) > 1)
    window = driver.window_handles[-1]   # ウィンドウ情報を取得
    driver.switch_to.window(window)       # 遷移先のウィンドウに遷移元のウィンドウ情報を移す

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'newsViewMore')))
    driver.find_element(By.ID, 'newsViewMore').click()
    time.sleep(1)
    info_container = driver.find_element(By.ID, 'tbl_news')
    info_pages = info_container.find_elements(By.TAG_NAME, 'tr')

    for i in range(len(info_pages)):
        if int(max_page) > i:
            date = info_pages[i].find_element(By.CLASS_NAME, 'day').text 
            title_container = info_pages[i].find_element(By.CLASS_NAME, 'title')
            title = title_container.find_element(By.TAG_NAME, 'a').text 
            print(f"{i}: {date} {title}")

    driver.quit()

def main():
    driver_path = os.environ['DRIVER_PATH']
    id = os.environ['OKIU_ID']
    password = os.environ['OKIU_PASS']
    max_page = os.environ['MAX_PAGE']
    fetch_portal(driver_path, id, password, max_page)

if __name__ == "__main__":
    main()


