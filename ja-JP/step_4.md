## LEGO® でゲージを作る

データを手軽に表示するもう1つの方法は、**ダイヤル** (または**ゲージ**とも呼ばれます) を使うことです。 あなたは間違いなく前にそれらを見たことがあります。それらは通常円形または半円形であり、2つの主要な目に見える部分があります。

+ 目盛りが表示されている面
+ 目盛りに沿って移動し、データの読み取り値を表示する針

![ダイヤルが動いている様子を写したアニメーション画像。](https://media.giphy.com/media/uozBSFuz99USA/giphy.gif)

ゲージまたはダイヤルは、面と針を作成するだけなので、 LEGO® を使って作成できる一番シンプルなデータの読み出し方法です。 針またはダイヤルはモーターに直接接続するため、組み立てはとても簡単です:

--- task ---

モーターをゲージの軸の後ろに取り付ける前に、モーターの端にある 2 つのロリポップの記号を並べて、モーターが「ゼロに調整」されていることを確認してください。

![記号の位置を合わせて、モーターが 'ゼロに調整' されていることを写した画像。](images/aligned_symbols.jpg)

--- /task ---

### スケールを作成する

ゲージを完成させるためには、紙・カード・またはその他の画材を使って、スケールを作る必要があります。 仕組みとコーディングはまったく同じですが、ゲージをどう見せたいか考えてみましょう。

 --- task ---

 作りたいダイヤルの種類を**選んでください**。

 LEGO® で簡単に作成できるのは 2 種類あります。

+ A gauge where the needle spins to indicate a point on the face: ![針と目盛り付きのゲージを写した画像。](images/dial2.gif)

+ A gauge where the whole face turns to display a point at the top with a stationary indicator: ![スケールが動くゲージを写した画像。](images/dial1.gif)

--- /task ---

--- task ---

ゲージにしたいサイズの円を、白紙にきれいになぞります。 中央に印を付け、はさみで切り取ります。

--- /task ---

--- task ---

Split the circle into equal segments (one for each reading) by drawing lines through the centre, or draw your scale around the edge.

--- /task ---

--- task ---

Draw an icon or write inside each segment what it indicates.

--- /task ---

ゲージの面を作り終えたら、ダッシュボードに取り付けていきしましょう。

--- collapse ---
---
title: ニードルゲージを作る場合
---

ニードルゲージを完成させるには:

--- task ---

面を軸に通し、軸が回転したときに面がずれないように、ブル・タックかテープを使って面の後ろとダッシュボードを固定します。 ![ゲージの面から突き出ている LEGO® の軸を示す画像。](images/needle-gauge1.jpg)

--- /task ---

--- task ---

Add a 90 degree elbow to the end of your axle and place another axle into it. Make sure it is long enough to reach your scale and clearly indicate the readings.

![Image showing the LEGO® axle protruding through the gauge's face with an elbow and perpendicular axle connected.](images/needle-gauge2.jpg)

It will help later if your axle is pointing straight up (and your motor is 'zeroed') when you mount it, as it will make it easier to calculate the amount of rotation required for a reading.

--- /task ---

--- /collapse ---

--- collapse ---
---
title: 回転するフェイスダイヤルを作る場合
---

回転するゲージを完成させるには:

--- task ---

Mount a single gear behind your dial face as a spacer, to prevent it from catching on your dashboard. Use some Blu Tack to stick the face to this gear. If you have created an incremental scale around the gauge, mount it with the middle of the scale at the top (in line with the 'zeroed' lollipop symbols) and the minimum and maximum values at the bottom.

![車軸に取り付けられ、タックがいくつか付けられた黒い LEGO® のギアを示す画像。](images/dial-gauge1.jpg)

![黒い LEGO® のギアの上に取り付けられたゲージの面を示す画像。](images/dial-gauge2.jpg)

--- /task ---

--- /collapse ---

### ゲージをテストする

--- task ---

ゲージ用のモーターを Build HAT のポート A に接続します。

--- /task ---

--- task ---

BuildHAT Python ライブラリを使うため、インストールされていることを確認してください:

--- collapse ---
---
title: BuildHat Python ライブラリのインストール
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> を押して、Raspberry Pi上にターミナルウィンドウを開きます。

プロンプトで次の通りに入力します: `pip3 install buildhat`

<kbd>Enter</kbd> キーを入力して "installation completed" のメッセージが表示されるまで待ちます。

--- /collapse ---

--- /task ---

--- task ---

Raspberry Pi上で、 **プログラミングメニュー** から **Thonny** を開きます。

次のコードを空白のタブに入力します:

--- code ---
---
language: python filename: gauge_test.py line_numbers: true line_number_start: 1
line_highlights:
---
from buildhat import Motor from time import sleep from random import randint

motor_gauge = Motor('A')

motor_gauge.run_to_position(0,100)

while True: angle = randint(-180, 180) motor_gauge.run_to_position(angle, 100) sleep(0.3)

--- /code ---

コードを `gauge_test.py` として保存して、 **Run**をクリックします。 するとゲージが動き始めるでしょう！

--- /task ---
