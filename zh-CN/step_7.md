## 使用仪表板显示污染数据

目前，您的仪表使用 -175 到 175 之间的随机整数；使用这些数字是因为它们是马达在两个方向上的行程限制。 （我们不会达到180 度，因为它会导致行程出现环绕覆盖的问题。） 来自您的 API 的数据不会具有相同的范围，因此您需要将其匹配到马达的行程范围。

**校准** 指示器意味着将来自 API 的最大和最小可能数据值映射到马达上的 -175° 和 175° 之间。 最高读数为 -175°，最低读数为 175°。 （因为您是反向装的马达！）

在本示例中，我们将在仪表盘上显示 **细颗粒 (PM2.5)** 测量值，而滑块显示器则将显示二氧化氮 (NO2) 水平。 术语**细颗粒**，或颗粒物 2.5 (PM2.5)，是指空气中尺寸为两微米半（或更小）的微小颗粒或液滴。 PM2.5 所测量的颗粒物构成了大部分烟和雾，并且很难看到。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">与英寸、米和毫米一样， <span style="color: #0faeb0">微米</span> 是距离的度量单位。 一英寸大约有 25,000 微米。 PM2.5 尺寸范围内的较大颗粒的宽度将比人类头发的宽度小约三十倍。 这些粒子非常小，以至于这句话末尾的句号可以容纳数千个这样的颗粒。</p>

在本示例中，滑块显示器将显示二氧化氮 (NO2) 水平。 滑块显示器上的最大可能读数取决于您选择的位置，因为城市地区的读数始终高于农村地区。 可能的最小读数显然是 0，但您需要考虑您所测量的正常范围是多少，然后再增大一点。

要确定最大可能读数是多少，您可以在之前打开的网页上查看所选位置的历史数据：

![桑迪路边站采集的二氧化氮的历史数据的图片。](images/historicaldata_no2.jpg)

在这里您可以看到，虽然有一些显著的异常值，但对于 Sandy Roadside 空气质量站的大多数读数来说，最大值设置为大约 60 应该足够了。 (如果您想将您的刻度简单地设置为从0到100, 你也可以这样做 — — 设置 `max_value = 100`。)

--- task ---

将滑动指示器的马达连接到 Build HAT 上的端口 A。 将仪表指示器的马达连接到端口 B。

--- /task ---

--- task ---

在新的 Thonny 窗口中，键入以下内容：

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 1
line_highlights:
---
from buildhat import Motor from time import sleep from datetime import datetime, timedelta import requests

no2_motor = Motor('A') #设置滑动指示器马达 no2_motor.run_to_position(0,100) #重置滑块位置 pm25_motor = Motor('B') #设置仪表马达 pm25_motor.run_to_position(0,100) #重置仪表位置

no2_min_value = 0 #你认为将获得的最低 NO2 读数（这应该在 0 左右） no2_max_value = 60 #你认为将获得的最高 NO2 读数 no2_min_angle = 175 #马达的反向最大行程 no2_max_angle = -175 #马达的正向最大行程

pm25_min_value = 0 #您认为将获得的最低 PM2.5 读数（这应该在 0 左右） pm25_max_value = 100 #您认为将获得的最高 PM2.5 读数 pm25_min_angle = 175 #马达的反向最大行程 pm25_max_angle = -175 #马达的正向最大行程

--- /code ---

--- /task ---

现在您已经导入了必要的库并设置了您要测量的详细信息，您可以通过创建几个 **词典**来设置对 API 的查询。

--- task ---

在您的 Thonny 窗口中，将此代码添加到脚本的末尾：

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 21
line_highlights:
---
base_url = 'https://docs.openaq.org/v2/measurements'

payload = { #为API请求创建一个字典 'date_from':'', 'date_to':'', 'location_id':'2480', #这个数字应该是之前从URL中获取的ID号 'order_by':'datetime', 'sort':'asc', 'has_geo':'true', 'limit':'100', 'offset':'0', }

pollution = {   #为污染读数创建一个字典 'no2' : 0, #这里我们查询 NO2 和 PM25 - 您的可能会有所不同！ 'pm25': 0, }

--- /code ---

--- /task ---

您需要编写的下一个函数将使用您设置的参数查询 API。

--- task ---

在脚本的末尾，添加以下代码：

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 39
line_highlights:
---
def check_air(): now = datetime.now() #获取现在的时间 delta = datetime.now() - timedelta(days=1) #创建一天的时差

    payload['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00' #将日期和时间插入上面的字典中
    payload['date_to'] = f'{now:%Y-%m-%d} T{now:%H:%M:%S}+00:00'
    
    response = requests.get(base_url, params=payload) #查询API数据库
    
    if response.status_code != 200: #检查API的连接
        print('no response from server')
        return
    
    data = response.json()
    
    for reading in data['results']:
        if reading['parameter'] == 'no2': #这取决于你测量的是什么污染物
            污染['no2'] = reading['value']
            print(pollution['no2'])
        if reading['parameter'] == 'pm25': #这取决于你测量的是什么污染物
            污染[ 'pm25'] = reading['value']
            print(pollution['pm25'])
    
    output_results()   
    sleep(1)

 --- /code ---

 --- /task ---

您将编写的下一部分将进行一些巧妙的数学运算，以在马达行程范围内映射您的数据区间。 (该函数与 [LEGO数据绘图项目](https://learning-admin.raspberrypi.org/en/projects/lego-plotter/6) 中使用的函数基本相同。)

--- task ---

在现有代码后添加这个函数：

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 65
line_highlights:
---
def remap(min_value, max_value, min_angle, max_angle, sensor_data): #创建函数 value_range = (max_value - min_value) #计算您的数据区间 motor_range = (max_angle - min_angle) #计算您的马达行程 mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle #将数据换算为马达行程 return int(mapped) #返回马达行程

--- /code ---

--- /task ---

现在您的函数已经创建，您需要创建一个循环：

+ 找到马达当前所在的角度
+ 提取污染物数据，通过`remap` 函数计算出马达应该到达的新角度
+ 移动到新角度以显示读数

--- task ---

将以下代码添加到脚本末尾的新行上：

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 73
line_highlights:
---
def output_results(): print(f'NO2 = {pollution['no2']}') no2_current_angle = no2_motor.get_aposition() no2_sensor_data = int(pollution['no2']) no2_new_angle = remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data) print(no2_new_angle) if no2_new_angle > no2_current_angle: no2_motor.run_to_position(no2_new_angle, 100, direction='anticlockwise') print('Turning CW') elif no2_new_angle < no2_current_angle: no2_motor.run_to_position(no2_new_angle, 100, direction='clockwise') print('Turning ACW') sleep(0.1) pm25_sensor_data = int(pollution['pm25']) print(f"PM2.5 = {pollution['pm25']}") pm25_current_angle = pm25_motor.get_aposition() print(pm25_current_angle) pm25_new_angle = remap(pm25_min_value, pm25_max_value, pm25_min_angle, pm25_max_angle, pm25_sensor_data) pm25_motor.run_to_position(pm25_new_angle, 100)

--- /code ---

--- /task ---

现在您的代码的最后一部分需要调用 `check_air()` 函数来运行上面的程序，并定期查询API 以获取更新的数据。

--- task ---

在脚本的末尾，在新行上（确保它没有缩进），键入：

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 93
line_highlights:
---
while True: check_air() sleep(3600) #等待一小时再检查（可以改小以便于测试） --- /code ---

--- /task ---

--- task ---

将您的工作另存为 `data_dash.py` 并单击 **Run**。 您的滑块应该移动以显示来自您选择的 OpenAQ 站的当前 NO2 读数，同时您的仪表也应该转动来显示 PM2.5 读数。 太棒了！

--- /task ---

--- save ---
