import schedule
import time

def fetch_data():
    print("データを取得しています...")

# 毎分fetch_data関数を実行
schedule.every(1).minutes.do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(1)