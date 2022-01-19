## 简介

在本项目中，您将创建一个可视化数据的仪表板；您可以从一系列在线资源中选择数据。 您的数据仪表板将需要满足 **项目简介**。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">仪表板</span> 是一个用户界面，它通常以图形或易于阅读的形式提供重要信息的当前摘要。 该术语起源于汽车，通过又大又亮的表盘和刻度向驾驶员显示车辆的当前状态。</p>

您将要：
+ 使用乐高（LEGO®）马达和元件构建一个自动化指示器
+ 通过 Python访问在线 **API** （应用程序编程接口）来获得一些有趣的数据
+ 在您用乐高（LEGO）创建的仪表板上显示您选择的数据

--- no-print ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1">

--- /no-print ---


--- collapse ---
---
title: 您需要准备的材料
---
### 硬件

+ 一台树莓派(Raspberry Pi)电脑
+ 一个Raspberry Pi Build HAT
+ 一个Raspberry Pi Build HAT的7.5V电源
+ 2 个乐高（LEGO®）Technic™ 马达（或者更多）
+ 一个乐高（LEGO®）SPIKE™ 压力传感器
+ 各种乐高（LEGO®）组件（我们使用了 [LEGO® SPIKE™ Prime 套件](https://education.lego.com/en-gb/product/spike-prime){:target="_blank"} ）
+ 纸或卡片
+ 用于粘贴卡片的大头钉或胶带
+ 记号笔或铅笔
+ 剪刀或工艺刀

可选的：
+ LED发光二极管
+ 电阻
+ 跳线
+ 一块面包板
+ M2 螺栓和螺母（2组，用于将 Raspberry Pi 安装到LEGO® Build Plate）

### 软件

+ 用于控制 Build HAT的BuildHAT Python 库
+ Thonny Python IDE

### 下载

+ 本项目的最终脚本可在 [此处]((https://rpf.io/p/en/lego-data-dash-go){:target="_blank"})下载

--- /collapse ---

在开始之前，您需要设置好您的 Raspberry Pi 并连接您的 Build HAT：

--- task ---

使用 M2 螺栓和螺母将您的 Raspberry Pi 安装到乐高(LEGO)积木板上，请确保 将Raspberry Pi 置于没有“边缘”的一侧：

 ![通过螺栓固定在洋红色乐高(LEGO)积木板上的Raspberry Pi。](images/build_11.jpg)

--- /task ---

以这种方式安装 Raspberry Pi 可以轻松访问（Raspberry Pi的）端口和 SD 卡插槽。 Build Plate 可让您更轻松地将 Raspberry Pi 连接到仪表板的主要部件。

--- task ---

将 Build HAT 与 Raspberry Pi 对齐，请确保您可以看到 `This way up` 标签。 确保所有 GPIO 引脚都被 HAT 覆盖，然后用力按下。 （该示例使用了 [堆叠头](https://www.adafruit.com/product/2223){:target="_blank"}，所以有更长的引脚。）

![显示GPIO 引脚穿过 Build HAT 的顶部的图片。](images/build_15.jpg) ![显示将 Buildhat 匹配到 Raspberry Pi的动画](images/haton.gif)

--- /task ---

现在利用 Build HAT 上的 7.5V 桶形插孔为您的 Raspberry Pi 供电，这也将用于驱动马达。

--- task ---

如果您尚未设置您的 Raspberry Pi，请按照以下步骤：

[设置你的Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Pi 启动后，单击 Raspberry 菜单按钮，然后选择“首选项”，然后选择“Raspberry Pi 配置”，打开 Raspberry Pi 配置工具。

单击“interfaces”选项卡并调整串口设置，如下所示：

![Raspberry Pi 操作系统的配置界面：启用串行端口，禁用串行控制台](images/configshot.jpg)

--- /task ---

--- task ---

您还需要按照以下说明安装 buildhat的 python 库：

--- collapse ---
---
title：安装 buildhat Python 库
---

按下<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>，在 Raspberry Pi 上打开一个终端窗口。

在提示符后键入： `sudo pip3 install buildhat`

按 <kbd>回车</kbd> 并等待“installation completed”消息。

--- /collapse ---

--- /task ---


<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### 项目简介：乐高（LEGO®）数据仪表板
<hr style="border-top: 2px solid black;">

您的任务是创建一个乐高（LEGO） 仪表板来显示您选择的数据。 您的数据来源可以是您喜欢的任何 API，但在本示例中，我们将向您展示如何访问 OpenAQ，它只需要很少或无需注册。 

对于我们的示例数据，我们将测量：
+ 选定位置的 **NO2** 水平。 二氧化氮 (NO2) 是一种被称为氮氧化物或 NOx 的高活性气体。 NO2 主要通过燃料的燃烧被释放到空气中。
+在选定位置的 **细颗粒物 (PM2.5)** 水平。 术语**细颗粒**，或颗粒物 2.5 (PM2.5)，是指空气中尺寸为两微米半（或更小）的微小颗粒或液滴。 被归类为 PM2.5 的颗粒是构成烟雾的物质。


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">我们在这个项目中使用的示例 API 来自 [OpenAQ](https://openaq.org/#/)，一个全球性的非营利组织，旨在“通过开放数据对抗空气的不平等”。 在全球范围内，**八分之一的死亡**是由于空气质量差造成的，OpenAQ 收集全球空气质量数据，以帮助更多人了解世界某些地区空气污染日益严重的问题。 </p>


您的仪表板应该实现：
+ 使用乐高（LEGO®）以清晰的方式显示您选择的数据
+ 在线访问 API 以获得最新的数据
+ 至少有两个乐高（LEGO®）指示器

您的仪表板可以：
+ 使用其他电子元件（LED、蜂鸣器）
+ 接受物理用户输入（乐高LEGO® Technic™ 马达、乐高LEGO® 压力传感器、GPIO 按钮、距离传感器）
  
</div>

--- no-print ---

### 获得灵感

--- task ---

在您学习这些示例项目以获得更多的想法时，考虑您想在您的仪表板上显示的信息。

这个范例显示了一个天气仪表板：在垂直滑块上显示当前温度；在云层上利用 LED显示可见度；在旋转刻度盘上，根据表观温度（包括风和其他天气情况）给出了舒适着衣的建议，并且显示了以世界天气代码标注的详尽天气情况（又名 WMO 代码）。

![演示视频](images/weather-dash.gif)

--- /task ---

--- /no-print ---

--- print-only ---

![一个由乐高（LEGO®） 制成的气象站仪表板的图片。](images/example-dash.jpg)

--- /print-only ---


