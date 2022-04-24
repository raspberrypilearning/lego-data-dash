## ダッシュボードで汚染データを表示する

現時点では、ダッシュボードでは-175〜175のランダムな整数を使用しています。これらの数値は、各方向へのモーターの移動制限のため使われています。 (一周してしまう問題が起こる可能性があるため、180にはしません。) APIからのデータはこれと同じ範囲ではないため、モーターに合わせる必要があります。

インジケーターの**キャリブレーション** とは、APIからのデータの最大値と最小値をモーターの -175° から 175° の間にマッピングすることです。 最高の読み取り値は-175°になり、最低の読み取り値は175°になります。 (モーターを逆に取り付けているためです！)

今回の例では、**微粒子 (PM2.5)** の測定値をゲージに表示し、二酸化窒素 (NO2) レベルをスライダーに表示します。 **微粒子**、または微小粒子状物質 2.5 (PM2.5) という用語は、大きさが 2.5 ミクロン (またはそれ以下) の空気中の小さな粒子または飛沫を指します。 PM2.5 で測定された粒子は、ほとんどの煙やスモッグを構成するもので、視界を悪くします。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">インチ、メートル、ミリメートルと同様に、 <span style="color: #0faeb0">ミクロン</span> は距離を測定するための単位です。 1 インチは約 25,000 ミクロンです。 The widths of the larger particles in the PM2.5 size range would be about thirty times smaller than that of a human hair. These particles are so small that several thousand of them could fit on the full stop at the end of this sentence.</p>

今回の例では、スライダーに二酸化窒素 (NO2) のレベルを表示します。 スライダーでの最大の読み取り値は、選択したロケーションによって変化します。これは、地方よりも都市部のほうが常に読み取り値が高くなるためです。 The minimum reading possible is obviously 0, but you will want to consider what the normal range is for what you are measuring and add a bit to that.

To work out what the maximum likely reading should be, you can see the historical data from your chosen location on the webpage you opened earlier:

![Image showing graphed historical NO2 data from Sandy, roadside.](images/historicaldata_no2.jpg)

Here, you can see that while there are some major outliers, around 60 should be more than enough as your maximum value for most readings from the Sandy Roadside air quality station. (単純に 0 から 100 までのスケールを作成することもできます。その場合は `max_value = 100` にするだけです。)

--- task ---

スライドインジケーターのモーターを Build HAT のポート A に接続します。 ゲージインジケータのモーターをポート B に接続します。

--- /task ---

--- task ---

新しい Thonny のウィンドウで、次のように入力します:

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 1
line_highlights:
---
from buildhat import Motor from time import sleep from datetime import datetime, timedelta import requests

no2_motor = Motor('A')           #スライダーモーターのセットアップ no2_motor.run_to_position(0,100) #スライダー位置のリセット pm25_motor = Motor('B')           #ゲージモーターのセットアップ pm25_motor.run_to_position(0,100) # ゲージ位置のリセット

no2_min_value = 0         #The lowest NO2 reading you think you will get (this should hopefully be around 0) no2_max_value = 60        #The highest NO2 reading you think you will get no2_min_angle = 175       #Minimum motor travel no2_max_angle = -175      #Maximum motor travel

pm25_min_value = 0        #The lowest PM2.5 reading you think you will get (this should hopefully be around 0) pm25_max_value = 100      #The highest PM2.5 reading you think you will get pm25_min_angle = 175      #Minimum motor travel pm25_max_angle = -175     #Maximum motor travel

--- /code ---

--- /task ---

必要なライブラリをインポートして測定の詳細を設定したので、使用するパラメータの**辞書**をいくつか作成することで、 API へのクエリを設定できます。

--- task ---

Thonny のウィンドウで、次のコードをスクリプトの最後に追加します:

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 21
line_highlights:
---
base_url = 'https://docs.openaq.org/v2/measurements'

payload = {                    #Create a dictionary for the API request 'date_from':'', 'date_to':'', 'location_id':'2480',      #This number should be the ID number taken from the URL earlier 'order_by':'datetime', 'sort':'asc', 'has_geo':'true', 'limit':'100', 'offset':'0', }

pollution = {                  #汚染測定値用の辞書を作成する 'no2' : 0,                 #ここでは NO2 と PM25 を見る ( 違う値を見るときは変える必要があるでしょう ) 'pm25': 0, }

--- /code ---

--- /task ---

次に作成するのは、設定したパラメーターを使用して API にクエリを実行する関数です。

--- task ---

スクリプトの最後に、次のコードを追加します。

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 39
line_highlights:
---
def check_air(): now = datetime.now()           #現在の時刻を取得する delta = datetime.now() - timedelta(days=1)         #1日違う時刻を作成する

    payload['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00'  #日付と時刻を辞書に代入する
    payload['date_to'] = f'{now:%Y-%m-%d}T{now:%H:%M:%S}+00:00'
    
    response = requests.get(base_url, params=payload)          #API データベースに問い合わせる
    
    if response.status_code != 200:          #API の接続を確認する
        print('no response from server')
        return
    
    data = response.json()
    
    for reading in data['results']:
        if reading['parameter'] == 'no2':       #測定している汚染物質によってここは異なります
            pollution['no2'] = reading['value']
            print(pollution['no2'])
        if reading['parameter'] == 'pm25':      #測定している汚染物質によってここは異なります
            pollution['pm25'] = reading['value']
            print(pollution['pm25'])
    
    output_results()   
    sleep(1)

 --- /code ---

 --- /task ---

次の部分では、モーターの範囲全体にデータの範囲をマッピングするために、うまく計算をします。 (基本的には [LEGO データプロッターのプロジェクト](https://learning-admin.raspberrypi.org/en/projects/lego-plotter/6)で使用されている関数と同じです。)

--- task ---

この関数を既存のコードの下に追加します:

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 65
line_highlights:
---
def remap(min_value, max_value, min_angle, max_angle, sensor_data):                    #Create function value_range = (max_value - min_value)                                              #Work out how wide your value range is motor_range = (max_angle - min_angle)                                              #Work out how wide your motor range is mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle     #Stretch your value range across your motor range return int(mapped)                                           #Give back a number that shows the value as an angle on the motor

--- /code ---

--- /task ---

関数を作成したら、次のようなループを作成します:

+ モーターが現在いる角度を見つけます
+ `remap` 関数から汚染物質データを取得し、モーターの新しい角度として使用します
+ 新しい角度に移動して、読み取り値を表示します

--- task ---

スクリプトの最後に次のコードを追加します:

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 73
line_highlights:
---
def output_results(): print(f'NO2 = {pollution['no2']}') no2_current_angle = no2_motor.get_aposition() no2_sensor_data = int(pollution['no2']) no2_new_angle = remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data) print(no2_new_angle) if no2_new_angle > no2_current_angle: no2_motor.run_to_position(no2_new_angle, 100, direction='anticlockwise') print('Turning CW') elif no2_new_angle < no2_current_angle: no2_motor.run_to_position(no2_new_angle, 100, direction='clockwise') print('Turning ACW') sleep(0.1) pm25_sensor_data = int(pollution['pm25']) print(f"PM2.5 = {pollution['pm25']}") pm25_current_angle = pm25_motor.get_aposition() print(pm25_current_angle) pm25_new_angle = remap(pm25_min_value, pm25_max_value, pm25_min_angle, pm25_max_angle, pm25_sensor_data) pm25_motor.run_to_position(pm25_new_angle, 100)

--- /code ---

--- /task ---

コードの最後の部分で、すべてを実行するために `check_air()` 関数を呼び出し、定期的に API をチェックしてデータを更新する必要があります。

--- task ---

スクリプトの最後に (インデントされていないことを確認して) 、次を入力します:

--- code ---
---
language: python filename: data_dash.py line_numbers: true line_number_start: 93
line_highlights:
---
while True: check_air() sleep(3600)   #次のチェックまで1時間待つ (テストするときはこの値を小さくします) --- /code ---

--- /task ---

--- task ---

コードを `data_dash.py` として保存して、 **Run**をクリックします。 スライダーが移動して、選択した OpenAQ ステーションからの現在の NO2 の読み取り値が表示されたり、ゲージが移動して PM2.5 の読み取り値が表示されたりするでしょう。 よくできました！

--- /task ---

--- save ---
