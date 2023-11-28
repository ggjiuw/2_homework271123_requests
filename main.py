import time
import requests
# from datetime import datetime

URL = 'http://api.open-notify.org/iss-now.json'

while True:
    response = requests.get(url=URL)
    longitude = response.json()["iss_position"]['longitude']
    latitude = response.json()["iss_position"]['latitude']
    with open('iss_pos.csv', mode='a', encoding='utf-8') as file:
        file.write(f'{longitude};{latitude}\n')
    # print(f'Done /at/ {datetime.now()}')
    time.sleep(5)

