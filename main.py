import os
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from bs4 import BeautifulSoup

# .envファイルから環境変数を読み込む
load_dotenv(verbose=True)

# ChromeDriverのパスを環境変数から取得する
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

# スクレイピング対象ページのURLを環境変数から取得する
TARGET_URL = os.getenv('TARGET_URL')

# ログイン情報を環境変数から取得する
USER_ID = os.getenv('USER_ID')
PASSWORD = os.getenv('PASSWORD')

# ブラウザを起動する
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # ヘッドレスモードで起動
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

# 対象ページにアクセスする
driver.get(TARGET_URL)

# ログイン処理
# login_id_input = driver.find_element_by_name('user')
# login_id_input.send_keys(USER_ID)
# login_password_input = driver.find_element_by_name('password')
# login_password_input.send_keys(PASSWORD)
# login_button = driver.find_element_by_css_selector('.login-form-submit')
# login_button.click()

# 項目取得処理
soup = BeautifulSoup(driver.page_source, 'html.parser')
h1_tags = soup.find_all('h1')
h2_tags = soup.find_all('h2')
h3_tags = soup.find_all('h3')

# 取得項目変数格納
result_list = []
for tag in h1_tags:
    result_list.append(tag.string)
for tag in h2_tags:
    result_list.append(tag.string)
for tag in h3_tags:
    result_list.append(tag.string)

# ファイル出力
now = datetime.now().strftime('%Y%m%d')
filename = f'result/取得結果{now}.txt'
with open(filename, mode='w') as f:
    for result in result_list:
        if result is not None:
            f.write(result + '\n')

# 後処理
driver.quit()
