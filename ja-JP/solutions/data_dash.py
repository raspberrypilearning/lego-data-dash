from buildhat import Motor
from time import sleep
from datetime import datetime, timedelta
import requests

no2_motor = Motor('A') #スライダーモーターのセットアップ
no2_motor.run_to_position(0,100) # スライダー位置のリセット
pm25_motor = Motor('B') #ゲージモーターのセットアップ
pm25_motor.run_to_position(0,100) # ゲージ位置のリセット

no2_min_value = 0 # 予想される最小の NO2 測定値 (おそらく 0 前後のはず)
no2_max_value = 60 #予想される最大の NO2 測定値 
no2_min_angle = 175 #最小のモーター移動量
no2_max_angle = -175 #最大のモーター移動量


pm25_min_value = 0  # 予想される最小の PM2.5 測定値 (おそらく 0 前後のはず)
pm25_max_value = 100 #予想される最大の PM2.5 測定値 
pm25_min_angle = 175 #最小のモーター移動量
pm25_max_angle = -175 #最大のモーター移動量

base_url = "https://docs.openaq.org/v2/measurements"

payload = { #APIリクエスト用の辞書を作成する
    'date_from':'',
    'date_to':'',
    'location_id':'2480',
    'order_by':'datetime',
    'sort':'asc',
    'has_geo':'true',
    'limit':'100',
    'offset':'0',
}

pollution = { #汚染測定値用の辞書を作成する
    'no2' : 0,
    'pm25': 0,
    }

def check_air():
    now = datetime.now()
    delta = datetime.now() - timedelta(days=1)
    
    payload['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00'
    payload['date_to'] = f'{now:%Y-%m-%d}T{now:%H:%M:%S}+00:00'
    
    response = requests.get(base_url, params=payload)
    
    if response.status_code != 200:
        print('no response from server')
        return
    
    data = response.json()
        
    for reading in data['results']:
        if reading['parameter'] == 'no2': # 測定している汚染物質によってここは異なります
            pollution['no2'] = reading['value']
        if reading['parameter'] == 'pm25': # 測定している汚染物質によってここは異なります
            pollution['pm25'] = reading['value']

    output_results()   
    sleep(1)

def remap(min_value, max_value, min_angle, max_angle, sensor_data):
    value_range = (max_value - min_value)        # work out how wide your value range is
    motor_range = (max_angle - min_angle)        # work out how wide your motor range is
    mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle        # stretch your value range across your motor range
    return int(mapped)        # give back a number that shows the value as an angle on the motor
   
def output_results():
    print(f"NO2 = {pollution['no2']}")
    no2_current_angle = no2_motor.get_aposition()
    no2_sensor_data = int(pollution['no2'])
    no2_new_angle = remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data)
    if no2_new_angle > no2_current_angle:
        no2_motor.run_to_position(no2_new_angle, 100, direction="clockwise")
    elif no2_new_angle < no2_current_angle:
        no2_motor.run_to_position(no2_new_angle, 100, direction="anticlockwise")
    sleep(0.1)
    pm25_sensor_data = int(pollution['pm25'])
    print(f"PM2.5 = {pollution['pm25']}")
    pm25_current_angle = pm25_motor.get_aposition()
    pm25_new_angle = remap(pm25_min_value, pm25_max_value, pm25_min_angle, pm25_max_angle, pm25_sensor_data)
    pm25_motor.run_to_position(pm25_new_angle, 100)

while True:
    check_air()
    sleep(3600)              # 次のチェックまで1時間待つ (テストするときはこの値を小さくします)