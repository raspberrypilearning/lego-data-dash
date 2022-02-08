## 대시보드에 오염 데이터 표시

현재 대시보드는 -175에서 175 사이의 임의의 정수를 사용합니다. 이 숫자는 모터가 각 방향으로 이동하는 한계이기 때문에 사용됩니다. (180은 전체 회전을 도는 데 문제를 일으킬 수 있으므로 180으로 가면 안됩니다.) API에서 들어오는 데이터의 범위는 동일하지 않으므로 모터에 맞게 조정해야 합니다.

**보정** 표시기는 API의 가능한 최대 및 최소 데이터 값을 모터의 -175°와 175° 사이로 매핑하는 것을 의미합니다. 가능한 가장 높은 판독값은 -175°인 반면 가능한 가장 낮은 판독값은 175°입니다. (모터를 반대로 장착했기 때문에!)

이 예 **미세 입자(PM2.5)** 측정값을 표시하고 슬라이더는 이산화질소(NO2) 수준을 표시합니다. **미세 입자**또는 미립자 물질 2.5(PM2.5)라는 용어는 너비가 2.5마이크론(또는 그 미만)인 공기 중의 작은 입자 또는 액적을 나타냅니다. PM2.5로 측정되는 입자는 대부분의 연기와 스모그를 구성하는 물질로 잘 보이지 않습니다.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">인치, 미터 및 밀리미터와 마찬가지로 <span style="color: #0faeb0">미크론</span> 은 거리 측정 단위입니다. 1인치는 약 25,000미크론입니다. PM2.5 크기 범위에서 더 큰 입자의 너비는 사람 머리카락의 너비보다 약 30배 작습니다. 이 입자들은 너무 작아서 수천개가 이 문장의 끝에 있는 마침표에 맞습니다.</p>

이 예에서 슬라이더는 이산화질소(NO2) 수준을 표시합니다. 슬라이더에서 가능한 최대 수치는 선택한 위치에 따라 달라집니다. 도시 지역은 항상 시골 지역보다 수치가 더 높기 때문입니다. 가능한 최소 판독값은 분명히 0이지만 측정 대상에 대한 정상 범위가 무엇인지 고려하고 여기에 약간을 추가해야 합니다.

가능한 최대 판독값을 계산하기 위해 이전에 연 웹 페이지에서 선택한 위치의 기록 데이터를 볼 수 있습니다.

![도로변 Sandy의 과거 이산화질소 데이터를 그래프로 나타낸 이미지.](images/historicaldata_no2.jpg)

여기에서 몇 가지 주요 아웃라이어한 이상값이 있지만 Sandy Roadside 공기질 관측소의 대부분의 판독값에 대해 최대값으로 약 60 이상을 충족해야 함을 알 수 있습니다. (만약 여러분이 0에서 000까지의 척도를 하고 싶다면, 여러분도 그렇게 할 수 있습니다 - 그냥 `max_value = 100` 하세요.)

--- task ---

슬라이딩 표시기 모터를 Build HAT의 포트 A에 연결합니다. 게이지 표시기 모터를 포트 B에 연결합니다.

--- /task ---

--- task ---

새 Thonny 창에서 다음을 입력합니다.

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 1
line_highlights:
---
from buildhat import Motor 
from time import sleep 
from datetime import datetime, timedelta 
import requests

no2_motor = Motor('A')           #슬라이드 모터 셋업 
no2_motor.run_to_position(0,100) # 슬라이더 포지션 리셋 
pm25_motor = Motor('B')           # 게이지 모터 셋업 
pm25_motor.run_to_position(0,100) # 게이지 포지션 리셋

no2_min_value = 0         #API가 가져올 것이라 생각하는 가장 작은 NO2 값 (약 0이여야 함) 
no2_max_value = 60        #API가 가져올 것이라 생각하는 가장 큰 NO2 값 
no2_min_angle = 175       #최소 모터 이동 앵글 
no2_max_angle = -175      #최대 모터 이동 앵글

pm25_min_value = 0         #API가 가져올 것이라 생각하는 가장 작은 PM2.5 값 (약 0이여야 함) 
pm25_max_value = 60        #API가 가져올 것이라 생각하는 가장 큰 PM2.5 값 
pm25_min_angle = 175       #최소 모터 이동 앵글 
pm25_max_angle = -175      #최대 모터 이동 앵글

--- /code ---

--- /task ---

필요한 라이브러리를 가져오고 측정 세부 정보를 설정했으므로 이제 사용하는 용어로 **딕셔너리**을 만들어 API에 대한 쿼리를 설정할 수 있습니다.

--- task ---

Thonny 창에서 스크립트 끝에 다음 코드를 추가합니다.

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 21
line_highlights:
---
base_url = 'https://docs.openaq.org/v2/measurements'

payload = {                    # API Request에 대한 딕셔너리 생성 
    'date_from':'', 
    'date_to':'', 
    'location_id':'2480',      # 방금 받은 URL에 적혀있는 숫자로 된 location ID입니다. 
    'order_by':'datetime', 
    'sort':'asc', 
    'has_geo':'true', 
    'limit':'100', 
    'offset':'0', 
}

pollution = {                  #오염 수치에 대한 딕셔너리 
    'no2' : 0,                 #NO2나 PM25에 대한 key-value 쌍 - 다를 수 있습니다! 
    'pm25': 0, 
    }

--- /code ---

--- /task ---

작성해야 하는 다음 함수는 설정한 매개변수를 사용하여 API를 쿼리합니다.

--- task ---

스크립트 끝에 다음 코드를 추가합니다.

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 39
line_highlights:
---
def check_air(): 
    now = datetime.now()           #현재 시간 가져오기 
    delta = datetime.now() - timedelta(days=1)         #시차 계산

    payload['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00'  #딕셔너리 datetime 세팅
    payload['date_to'] = f'{now:%Y-%m-%d}T{now:%H:%M:%S}+00:00'
    
    response = requests.get(base_url, params=payload)          #API database 쿼리
    
    if response.status_code != 200:          #API connection 검사
        print('no response from server')
        return
    
    data = response.json()
    
    for reading in data['results']:
        if reading['parameter'] == 'no2':       #어떤 오염 수치를 측정할 것인지에 따라 다릅니다.
            pollution['no2'] = reading['value']
            print(pollution['no2'])
        if reading['parameter'] == 'pm25':      #어떤 오염 수치를 측정할 것인지에 따라 다릅니다.
            pollution['pm25'] = reading['value']
            print(pollution['pm25'])
    
    output_results()   
    sleep(1)

 --- /code ---

 --- /task ---

다음으로 작성하게 될 부분은 전체 엔진 범위에 걸쳐 데이터 범위를 매핑하는 몇 가지 영리한 계산을 수행하는 것입니다. [LEGO Data 플로터 프로젝트](https://learning-admin.raspberrypi.org/ko-KR/projects/lego-plotter/6)에서 사용하는 기능과 동일합니다.)

--- task ---

기존 코드 아래에 이 함수를 추가합니다.

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 65
line_highlights:
---
def remap(min_value, max_value, min_angle, max_angle, sensor_data):                    #함수 만들기 
    value_range = (max_value - min_value)                                              #value range 계산 
    motor_range = (max_angle - min_angle)                                              #motor range 계산 
    mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle     #모터 범위 전체에 걸쳐 값 범위 확장 
    return int(mapped)                                           #모터의 각도로 값을 표시하는 숫자 반환

--- /code ---

--- /task ---

이제 함수가 생성되었으므로 다음을 수행하는 루프를 만들어야 합니다.

+ 모터가 현재 있는 각도 찾기
+ `remap` 기능에서 오염 물질 데이터를 가져와 모터의 새 각도로 사용
+ 새로운 각도로 이동하여 결과 값 표시

--- task ---

새 줄의 스크립트 끝에 다음 코드를 추가합니다.

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 73
line_highlights:
---
def output_results():
    print(f'NO2 = {pollution['no2']}')
    no2_current_angle = no2_motor.get_aposition()
    no2_sensor_data = int(pollution['no2'])
    no2_new_angle = remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data)
    print(no2_new_angle)
    if no2_new_angle > no2_current_angle:
        no2_motor.run_to_position(no2_new_angle, 100, direction='anticlockwise')
        print('Turning CW')
    elif no2_new_angle < no2_current_angle:
        no2_motor.run_to_position(no2_new_angle, 100, direction='clockwise')
        print('Turning ACW')
    sleep(0.1)
    pm25_sensor_data = int(pollution['pm25'])
    print(f"PM2.5 = {pollution['pm25']}")
    pm25_current_angle = pm25_motor.get_aposition()
    print(pm25_current_angle)
    pm25_new_angle = remap(pm25_min_value, pm25_max_value, pm25_min_angle, pm25_max_angle, pm25_sensor_data)
    pm25_motor.run_to_position(pm25_new_angle, 100)

--- /code ---

--- /task ---

이제 코드의 마지막 부분에서 `check_air()` 함수를 호출하여 모든 작업을 수행하고 API에서 업데이트된 데이터를 주기적으로 확인해야 합니다.

--- task ---

스크립트 끝에서 새 줄에(들여쓰기가 없는지 확인) 다음을 입력합니다.

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 93
line_highlights:
---
while True: 
    check_air() 
    sleep(3600)   # 다음 데이터 검색 전에 1시간을 기다립니다(테스트를 위해 이 시간을 더 짧게 만들 수 있음)
--- /code ---

--- /task ---

--- task ---

작업을 `data_dash.py` 로 저장하고 **실행** 을 클릭합니다. 슬라이더는 선택한 OpenAQ 스테이션의 현재 NO2 판독값을 표시하도록 이동해야 하고 게이지는 PM2.5 판독값을 표시하도록 이동해야 합니다. 잘 했어요!

--- /task ---

--- save ---
