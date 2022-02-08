from buildhat import Motor
from time import sleep
from datetime import datetime, timedelta
import requests

no2_motor = Motor('A') # 슬라이드 모터 설정
no2_motor.run_to_position(0,100) # 슬라이드 포지션 초기화
pm25_motor = Motor('B') #게이지 모터 설정
pm25_motor.run_to_position(0,100) # 게이지 포지션 초기화

no2_min_value = 0 # 예상되는 가장 낮은 NO2 수치 (이 값은 0이어야 함)
no2_max_value = 60 #예상되는 가장 높은 NO2 수치 
no2_min_angle = 175 #최소 모터 앵글
no2_max_angle = -175 #최대 모터 앵글


pm25_min_value = 0 # 예상되는 가장 낮은 PM25 수치 (이 값은 0이어야 함)
pm25_max_value = 100 #예상되는 가장 높은 PM25 수치 
pm25_min_angle = 175 #최소 모터 앵글
pm25_max_angle = -175 #최대 모터 앵글

base_url = "https://docs.openaq.org/v2/measurements"

payload = { #API request 를 위한 딕셔너리 생성
    'date_from':'',
    'date_to':'',
    'location_id':'2480',
    'order_by':'datetime',
    'sort':'asc',
    'has_geo':'true',
    'limit':'100',
    'offset':'0',
}

pollution = { #오염 수치에 대한 딕셔너리 생성
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
        if reading['parameter'] == 'no2': # 측정하려는 오염수치에 따라 달라짐
            pollution['no2'] = reading['value']
        if reading['parameter'] == 'pm25': # 측정하려는 오염수치에 따라 달라짐
            pollution['pm25'] = reading['value']

    output_results()   
    sleep(1)

def remap(min_value, max_value, min_angle, max_angle, sensor_data):
    value_range = (max_value - min_value)        # value range를 알아내기 위한 코드
    motor_range = (max_angle - min_angle)        # motor range를 알아내기 위한 코드
    mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle        # 모터 범위에서 값 범위 확장
    return int(mapped)        # 값을 모터의 앵글로 표시하는 숫자 반환
   
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
    sleep(3600)              # 1시간 대기 이후 다시 확인 (테스트 시 이 값을 작게 조정하세요.)