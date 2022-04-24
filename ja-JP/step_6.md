## OpenAQ API にアクセスする

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">API は <span style="color: #0faeb0">**Application Programming Interface**</span>の略で、 2 つのアプリケーションが互いに通信できるようにするためのソフトウェアです。 Facebook などのアプリを使用したり、インスタントメッセージを送信したり、スマートフォンで天気を確認したりするたびに、私たちは API を使用しています。</p>

Whenever you use an app on your phone, the app connects to the internet and sends data about what you want to know to a server. The server then finds and retrieves the data you want, interprets it, and sends it back to your phone. アプリは返されたデータを受け取って、必要な情報を読みやすい方法で表示します。 つまりAPIとは、インターネット上で他のマシンを制御する方法です。すべては **API** を通じて行われます。

The cool part is, you can write your own apps that investigate online databases of information and return the desired data to your LEGO® dashboard instead of a phone — you'll use your Raspberry Pi as the brains to get that data, then display it on your hand-made, custom LEGO indicators!

そのためには、いくつかのことを決めておく必要があります。まずは大気質を調べるロケーションを選ぶ必要があります。これは世界中のどこを選ぶこともできます。 そして、表示したい大気質のマーカーがどれか決める必要があります。

### OpenAQ — オープンソースの大気質データベース

今回のダッシュボードでは、オープンソースのグローバルな大気質データのプロジェクトである [**OpenAQ**](https://openaq.org/#/){:target="_blank"} の API を使用します。 OpenAQ を使用すると、世界各地の何千もの測定ステーションによって収集された、地球上のさまざまな種類の大気汚染データを確認できます。

If you're already a wizard with APIs, you can use any data you like to represent on your dashboard. If you want to follow along with us and use OpenAQ for your first try, you'll need to find out which measurement station you want to investigate and which measurements you are able to view.

--- task ---

[ここをクリック](https://openaq.org/#/map){:target="_blank"}して、 OpenAQ のマップに**移動しましょう**。 ドットで覆われた世界地図のウェブページが表示されます。

--- /task ---

--- task ---

世界のどこの大気質データを収集したいかを**決めましょう**。 This could be the area near where you live, somewhere that interests you, or somewhere that you think might have interesting data.

--- /task ---

Raspberry Piの本社は英国のケンブリッジにあるので、ここではそれを例として使用します。

大気質のモニタリングステーションでは、様々な測定が行われています。 OpenAQ データベースには、大気汚染に関して次の種類の情報があります:

 + PM2.5 および PM10 (粒子状物質): 空気中に浮遊する微細な粒子 (煙、スモッグ)
 + NO2 (二酸化窒素): オゾン生成の元となり、また、子供の喘息の原因になる
 + CO (一酸化炭素): 人体に致命的、化石燃料の燃焼の副反応
 + SO2 (sulfur dioxide): smells bad, can cause breathing problems, creates acid rain, side effect of industrial treatments
 + O3 (オゾン): NO2が日光に反応するとできる、スモッグの原因、植物に有害
 + BC (ブラックカーボン): 多くの場所 (米国やポーランド) では測定されていない、非効率的な燃料燃焼によって発生する、地球温暖化を助長する、人間に危険

--- task ---

測定するのに一番興味がある大気汚染の種類を**決めましょう**。 画面左側のカラースケールの近くにあるプルダウンメニューから、色々なオプションを選択できます。 ![OpenAQ マップのプルダウンメニューを示す画像。](images/mapscale.jpg)

**注:** 丸いマーカーは、より多様な汚染物質を測定していると思われる、本格的な大気質ステーションを表します。

--- /task ---

--- task ---

地図上で選択したエリアを**拡大**して、測定したい場所に一番近い点を見つけましょう。 その一番近い点をクリックして、場所の詳細を表示します。 表示されたポップアップで、 **View Location** のボタンをクリックします。  
![イギリスの東部を拡大した世界地図を示す画像。](images/mapscroll.gif)

--- /task ---

--- task ---

新しいウェブページがロードされてその場所で行われた測定の詳細が表示されたら、そのページのURLにある番号の **メモをとって** おきます。 これは、選択した大気質ステーションの OpenAQ での識別番号です。 (この例では、 ID 番号 **2480** はサンディ・ロードサイドの測定ステーションです。) ![ロケーション ID の番号が付いた Open AQ の URLを示す画像。](images/openaq_id.jpg)

--- /task ---

--- task ---

ロケーションのページでは、その場所で測定された、さまざまな種類の汚染物質が表示されます。 データダッシュボードに表示したいことを、リストから 2 つ**選びましょう**。 ![Image showing a pollutant list from a location on the OpenAQ map.](images/openaq_msmt.jpg) サンディの近くにあるこの測定ステーションでは、 NO2 、 PM10 、 PM2.5 を表示できるため、例では NO2 と PM2.5 を使用します。

--- /task ---