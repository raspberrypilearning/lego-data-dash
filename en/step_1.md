## Introduction


In this project you are going to create a dashboard which will visualise data you choose from a range of online sources. Your data dashboard will need to meet the **project brief**.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">Dashboard</span> is a user interface that gives a current summary of important information, usually in graphic, easy-to-read form. The term originates from cars, where the driver is shown the current status of the vehicle using big, bright dials and scales.</p>

You will:
+ Build automated indicators using LEGO motors and elements
+ Access an online **API** to retrieve interesting data using python
+ Display your chosen data on a dashboard you create

--- no-print ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1">


--- /no-print ---


--- collapse ---
---
title: What you will need
---
### Hardware

+ A Raspberry Pi Computer
+ A Raspberry Pi Build Hat
+ 2 Small Lego Motors (more optional)
+ Assortment of Lego; we used a selection from the [LEGO Spike Prime kit](https://education.lego.com/en-gb/product/spike-prime){:target="_blank"}

Optional:
+ LEDs
+ Jumper wires
+ M2 bolts and nuts (x2 each for mounting the Raspberry Pi to the LEGO Build Plate)

### Software

+ BuildHAT python library for controlling the Build Hat
+ Thonny python IDE
+ PYTHON LIBS FOR APIS HERE

### Downloads

+ 

--- /collapse ---

Before you begin, you'll need to have setup your Raspberry Pi Computer and attached your LEGO BuildHAT:

--- task ---

Mount your Raspberry Pi to the LEGO Maker Plate using M2 bolts and nuts, making sure the pi is on the side without the 'edge':

 ![Raspberry Pi bolted to a magenta LEGO Maker plate](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. The Maker Plate will allow you to connect the Raspberry Pi to the main structure of your Dashboard more easily.

--- task ---

Line up the BuildHAT with the Raspberry Pi, ensuring you can see the `This way up` label. Make sure all the GPIO pins are covered by the HAT, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"} which makes the pins longer.)

![Image of GPIO pins poking through the top of the buildHAT](images/build_15.jpg)

--- /task ---

You should now power your Raspberry Pi using the 7.5V barrel jack on the BuildHAT which will allow you to use the motors.

--- task ---

If you have not already done so, set up your new Raspberry Pi by following these instructions:

[Setting up your Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---


<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### PROJECT BRIEF: LEGO Data Dashboard
<hr style="border-top: 2px solid black;">

Your task is to create a LEGO Dashboard that will display your chosen data. The sources for your data can be any API you like, but in this example we will show you how to access these specific examples, which require minimal or no sign up:

+ API 1 - Information list available
+ API 2 - Information list available
+ API 3 - Information list available

Your Dashboard should:
+ Use LEGO to display your chosen data in a clear way
+ Access an online API to retrieve up-to-date data
+ Have at least two (2) LEGO indicators

Your Dashboard could:
+ Use other electronic components (LEDs, buzzers)
+ Have physical user inputs (LEGO motor, LEGO Shock sensor, GPIO button, distance sensor)
  
</div>

--- no-print ---

### Get inspiration

--- task ---

Think about the information you would like to display on your dashboard as you investigate these example projects to get more ideas:

This example shows a weather Dashboard displaying the current temperature on a vertical slider, the cloud cover using an LED scale, and on the rotating dials it suggests a level of clothing based on the apparent temperature (includes the wind and other weather in the temperature) and a detailed weather report using World Weather Codes (a.k.a WMO code).

![Demo Video](images/weather_dash.gif)

--- /task ---

--- /no-print ---

--- print-only ---
![Complete project](images/showcase_static.png)
--- /print-only ---


