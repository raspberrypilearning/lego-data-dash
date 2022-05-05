## ダッシュボードで汚染データを表示する

現時点では、ダッシュボードでは-175〜175のランダムな整数を使用しています。これらの数値は、各方向へのモーターの移動制限のため使われています。 (一周してしまう問題が起こる可能性があるため、180にはしません。) APIからのデータはこれと同じ範囲ではないため、モーターに合わせる必要があります。

インジケーターの**キャリブレーション** とは、APIからのデータの最大値と最小値をモーターの -175° から 175° の間にマッピングすることです。 最高の読み取り値は-175°になり、最低の読み取り値は175°になります。 (モーターを逆に取り付けているためです！)

今回の例では、**微粒子 (PM2.5)** の測定値をゲージに表示し、二酸化窒素 (NO2) レベルをスライダーに表示します。 **微粒子**、または微小粒子状物質 2.5 (PM2.5) という用語は、大きさが 2.5 ミクロン (またはそれ以下) の空気中の小さな粒子または液滴を指します。 PM2.5 で測定された粒子は、ほとんどの煙やスモッグを構成するもので、視界を悪くします。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">インチ、メートル、ミリメートルと同様に、 <span style="color: #0faeb0">ミクロン</span> は距離を測定するための単位です。 1 インチは約 25,000 ミクロンです。 PM2.5 のなかでは大きめな粒子でも、人の髪の毛の直径の約30分の1程度の大きさです。 これらの粒子は非常に小さく、この文の終わりの句点（。）に数千個が収まってしまうほどです。</p>

今回の例では、スライダーに二酸化窒素 (NO2) のレベルを表示します。 スライダーでの最大の読み取り値は、選択したロケーションによって変化します。これは、地方よりも都市部のほうが常に読み取り値が高くなるためです。 最小の読み取り値はほとんどの場合0なのですが、ねんのために測定対象のふだんの範囲を調べて少し調整したほうが良いでしょう。

最大の読み取り値を調べるには、先ほど開いたウェブページで、選択したロケーションの履歴データから確認します:

![サンディのロードサイドから、過去のNO2データをグラフ化した画像。](images/historicaldata_no2.jpg)

ここで、いくつか大きな外れ値がみられますが、サンディロードサイドの大気質測定地点から読み取れるほとんどの値からして、最大値は60前後で十分でしょう。 (単純に 0 から 100 までのスケールを作成することもできます。その場合は `max_value = 100` にするだけです。)

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

no2_min_value = 0         #予想される最小の NO2 測定値 (おそらく 0 前後のはず) no2_max_value = 60        #予想される最大の NO2 測定値 no2_min_angle = 175       #最小のモーター移動量 no2_max_angle = -175      #最大のモーター移動量

pm25_min_value = 0        #予想される最小の PM2.5 測定値 (おそらく 0 前後のはず) pm25_max_value = 100      #予想される最大の PM2.5 測定値 pm25_min_angle = 175      #最小のモーター移動量 pm25_max_angle = -175     #最大のモーター移動量

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

payload = {                    #APIリクエスト用の辞書を作成する 'date_from':'', 'date_to':'', 'location_id':'2480',      #この番号は、先のURLから取得したIDを指定する 'order_by':'datetime', 'sort':'asc', 'has_geo':'true', 'limit':'100', 'offset':'0', }

pollution = {                  #汚染測定値用の辞書を作成する 'no2' : 0,                 #ここでは NO2 と PM25 を見る ( 違う値を見るときは変える必要があるでしょう ) 'pm25'： }

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
def remap(min_value, max_value, min_angle, max_angle, sensor_data):                    #関数の作成 value_range = (max_value - min_value)                                              #値の範囲がどれくらいの幅か計算する motor_range = (max_angle - min_angle)                                              #モーターの範囲がどれくらいの幅か計算する mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle     #値の範囲をモーターの範囲に当てはめる return int(mapped)                                           #モーターの角度としての値の数値を返す

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
