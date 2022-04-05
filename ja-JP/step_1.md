## はじめに

このプロジェクトでは、データを視覚化するダッシュボードを作成します。さまざまなオンラインのソースから表示するデータを選べます。 Your data dashboard will need to meet the **project brief**.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">dashboard</span> is a user interface that gives a current summary of important information, usually in a graphical or easy-to-read form. The term originates from cars, where the driver is shown the current status of the vehicle by big, bright dials and scales.</p>

本項で学ぶこと:
+ LEGO® モーターとエレメントを使用して自動のインジケーターを作成する
+ Access an online **API** (Application Programming Interface) to retrieve interesting data using Python
+ LEGO を使用して作成したダッシュボード上に、取得したデータを表示します。

--- no-print ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1">

--- /no-print ---


--- collapse ---
---
title: 必要なもの
---
### ハードウェア

+ Raspberry Pi コンピューター
+ Raspberry Pi Build HAT
+ Raspberry Pi Build HAT 7.5V 電源アダプター
+ 2 LEGO® Technic™ motors (more optional)
+ LEGO® SPIKE™ フォースセンサー
+ LEGO® 製品 (本項では [LEGO® SPIKE™ プライムキット](https://education.lego.com/en-gb/product/spike-prime){:target="_blank"} から選んで使用します)
+ 紙またはカード
+ カードを貼り付けるための画鋲やテープ
+ マーカーまたは鉛筆
+ はさみまたはカッターナイフ

オプション:
+ LED
+ 抵抗
+ ジャンパー線
+ ブレッドボード
+ M2ボルトとナット (Raspberry Pi を LEGO® ビルドプレートに取り付けるためにそれぞれ2つ)

### ソフトウェア

+ Build HAT を制御するための Build HAT Python ライブラリ
+ Thonny Python IDE

### ダウンロード

+ このプロジェクトの最終的なスクリプトは、 [ここ]((https://rpf.io/p/en/lego-data-dash-go){:target="_blank"}) から入手できます

--- /collapse ---

開始する前に、Raspberry Piのセットアップと、Build HATの装着をしてください:

--- task ---

M2のボルトとナットを使用して、 LEGO ビルドプレートの上にRaspberry Piを取り付けます。 Raspberry Piはふちがない方の面に載せます:

 ![Raspberry Pi が赤い LEGO ビルドプレートに固定された様子](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. ビルドプレートを使うことで、 ダッシュボードのおもな構造に、より簡単に Raspberry Pi を接続できます。

--- task ---

`This way up` の文字が見えるようにBuild HATをRaspberry Piと並べます。 全部のGPIOピンがHATにかぶるよう合わせて、しっかり押し下げてください。 (例ではピンが長くなる [スタッキングヘッダー](https://www.adafruit.com/product/2223){:target="_blank"} を使用しています。)

![Image of GPIO pins poking through the top of the Build HAT.](images/build_15.jpg) ![Animation showing Buildhat fitting to Raspberry Pi](images/haton.gif)

--- /task ---

モーターを使用するためには、Build HAT上のバレルジャックに7.5Vの電源を接続してRaspberry Piに電源を供給する必要があります。

--- task ---

まだRaspberry Piのセットアップが済んでいない場合は、次の手順に従ってセットアップしてください:

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Piが起動したら、Raspberry Piメニューをクリックして“Preferences”と “Raspberry Pi Configuration”の順に選択して、Raspberry Pi Configuration toolを起動します。

Click on the “interfaces” tab and adjust the Serial settings as shown below:

![Image showing Raspberry Pi OS config screen with serial port enabled and serial console disabled](images/configshot.jpg)

--- /task ---

--- task ---

You will also need to install the buildhat python library by following these instructions:

--- collapse ---
---
title: buildhat Python ライブラリのインストール
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> を押して、Raspberry Pi上にターミナルウィンドウを開きます。

At the prompt type: `sudo pip3 install buildhat`

<kbd>Enter</kbd> キーを入力して "installation completed" のメッセージが表示されるまで待ちます。

--- /collapse ---

--- /task ---


<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### プロジェクトの概要: LEGO® データダッシュボード
<hr style="border-top: 2px solid black;">

あなたのタスクは、あなたの選択したデータを表示する LEGO ダッシュボードを作成することです。 データのソースは好きな API にすることができますが、今回の例では、最小限のサインアップまたはサインアップが不要な OpenAQ にアクセスする方法を説明します。 

例のデータでは、以下のデータが計測できます:
+ 選択した場所の **NO2** のレベル。 二酸化窒素 (NO2) は、窒素酸化物や NOx として知られる、反応性の高いガスの一種です。 NO2 は、主に燃料の燃焼によって大気中に放出されます。
+ 選択した場所の **微粒子 (PM2.5) ** のレベル。 **微粒子** または粒子状物質 2.5 (PM2.5) という用語は、サイズが 2.5 ミクロン (またはそれ以下) の、空気中の小さな粒子または液滴を指します。 PM2.5 に分類される粒子は、煙とスモッグを構成するものです。


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">The example API we are using in this project is from [OpenAQ](https://openaq.org/#/), a global non-profit organisation "fighting air inequality through open data". 世界的に、 **8人に1人が亡くなっている** のは大気質の悪さによるものであり、 OpenAQ は世界の大気質データを収集して、世界の一部地域で増加する大気汚染の問題について、より多くの人々に知ってもらうのに役立てています。 </p>


ダッシュボードで、以下の要件を満たしてください:
+ LEGO® を使って、選んだデータを明確に表示すること
+ オンラインの API にアクセスして、最新のデータを取得すること
+ 最低2つのインジケータを LEGO® で作成すること

ダッシュボードで、可能なら以下も行ってください:
+ 他の電子部品 (LED、ブザー) を使用する
+ 物理的なユーザー入力装置を用意する (LEGO® Technic™ モーター、 LEGO® フォースセンサー、 GPIO ボタン、距離センサー)
  
</div>

--- no-print ---

### Get inspiration

--- task ---

これらのサンプルプロジェクトを調べてもっとアイデアを得るために、ダッシュボードに表示したい情報について考えましょう。

この例では、垂直のスライダーに現在の温度を表示する天気のダッシュボード、LEDスケールを使った雲のカバー、 そして回転するダイヤルは、体感温度 (風や温度の他の天気を含む) に基づいたちょうどよい衣類を提案したり、世界気象コード (WMO コード) を使用した詳細な天気予報をレポートしたりします 。

![Demo Video](images/weather-dash.gif)

--- /task ---

--- /no-print ---

--- print-only ---

![Image showing a weather station dashboard made of LEGO®.](images/example-dash.jpg)

--- /print-only ---


