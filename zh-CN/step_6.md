## 访问 OpenAQ API

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">API 代表 <span style="color: #0faeb0">**应用程序编程接口**</span>;这是一个允许两个应用程序相互交谈的软件。 每次您使用 Facebook 等应用程序、发送即时消息或在手机上查看天气时，您都在使用 API。</p>

每当您在手机上使用应用程序时，该应用程序都会连接到互联网并将有关您想知道的内容的数据发送到服务器。 然后服务器会查找并检索您想要的数据，对其进行解释，然后将其发送回您的手机。 然后，该应用程序获取已返回的数据，并以可读的方式向您呈现您想要的信息。 这就是 API：一种通过互联网控制其他机器的方法——所有这些都通过 **API**。

最酷的部分是，您可以编写自己的应用程序来调查在线信息数据库并将所需数据返回到您的 LEGO® 仪表板而不是手机 — 您将使用 Raspberry Pi 作为大脑来获取这些数据，然后显示它在您手工制作的定制乐高指示器上！

为此，您需要决定几件事：您需要选择可以了解空气质量的地点——您可以选择世界上任何地方！ — 您需要决定要代表哪些空气质量标志。

### OpenAQ — 开源空气质量数据库

在您的示例仪表板中，您将使用 [**OpenAQ**](https://openaq.org/#/){:target="_blank"} 的 API，这是一个开源的全球空气质量数据项目。 OpenAQ allows you to look at lots of different air pollution data from all over the globe, collected by thousands of measurement stations around the world.

如果您已经是 API 向导，则可以使用您喜欢在仪表板上表示的任何数据。 如果您想跟随我们并首次尝试使用 OpenAQ，您需要找出您想要调查的测量站以及您能够查看的测量结果。

--- task ---

** [单击此处](https://openaq.org/#/map){:target="_blank"} 导航** 到 OpenAQ 地图。 应该会出现一个显示由点覆盖的世界地图的网页。

--- /task ---

--- task ---

**决定** 您希望从世界上的哪个地方收集有关空气质量的数据。 这可能是您居住地附近的区域、您感兴趣的地方或您认为可能有有趣数据的地方。

--- /task ---

由于我们的总部位于英国剑桥，因此我们将以此为示例。

空气质量监测站进行了许多不同的测量。 OpenAQ 数据库包含有关以下类型空气污染的信息：

 + PM2.5和PM10（颗粒物）：漂浮在空气中的微小颗粒（烟、雾）
 + NO2（二氧化氮）：导致臭氧产生，导致儿童哮喘
 + CO（一氧化碳）：对人类致命，燃烧化石燃料的副作用
 + SO2（二氧化硫）：气味难闻，会导致呼吸问题，产生酸雨，工业处理的副作用
 + O3（臭氧）：当 NO2 与阳光发生反应时产生，产生烟雾，对植物有害
 + BC（黑碳）：在很多地方（美国和波兰）没有测量，由于燃料燃烧效率低下，加剧了全球变暖，对人类有害

--- task ---

**决定** 您最想测量哪种空气污染。 You can choose different options from the pulldown menu near the coloured scale on the left of the screen. ![显示 OpenAQ 地图中下拉菜单的图像。](images/mapscale.jpg)

**Note:** Round markers represent more substantial air quality stations which are likely to measure more varied pollutants.

--- /task ---

--- task ---

**Zoom in** to your chosen area on the map, and find the dot closest to the place you would like to measure. Click on that nearest dot to see the location details. In the pop-up that appears, click the button that says **View Location**.  
![Image showing a world map zoomed in on the eastern UK.](images/mapscroll.gif)

--- /task ---

--- task ---

When the new webpage loads showing the details of the measurements taken at the location, **make a note** of the number in the URL of the new page. This is the OpenAQ identification number for your chosen air quality station. (In this example, it is the Sandy Roadside measurement station, with ID number **2480**.) ![Image showing the OpenAQ URL with a number for the location ID.](images/openaq_id.jpg)

--- /task ---

--- task ---

On the location page, you will see the different types of pollutants measured at that location. **Choose** two from the list that you would like to represent on your data dashboard. ![Image showing a pollutant list from a location on the OpenAQ map.](images/openaq_msmt.jpg) This measurement station near Sandy can show NO2, PM10, and PM2.5 — so we'll use NO2 and PM2.5 in the example.

--- /task ---