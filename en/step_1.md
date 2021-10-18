## Introduction

In this project, you are going to create a dashboard that will visualise data; you can choose what data it shows from a range of online sources. Your data dashboard will need to meet the **project brief**.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0">dashboard</span> is a user interface that gives a current summary of important information, usually in a graphical or easy-to-read form. The term originates from cars, where the driver is shown the current status of the vehicle by big, bright dials and scales.</p>

You will:
+ Build automated indicators using LEGO® motors and elements
+ Access an online **API** (Application Programming Interface) to retrieve interesting data using Python
+ Display your chosen data on a dashboard you create using LEGO

--- no-print ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1">

--- /no-print ---


--- collapse ---
---
title: What you will need
---
### Hardware

+ A Raspberry Pi computer
+ A Raspberry Pi Build HAT
+ 2 LEGO® Technic™ motors (more optional)
+ A LEGO® SPIKE™ Force Sensor
+ Assortment of LEGO® (we used a selection from the [LEGO® SPIKE™ Prime kit](https://education.lego.com/en-gb/product/spike-prime){:target="_blank"})
+ Paper or card
+ Tack or tape for sticking down card
+ Marker or pencil
+ Scissors or craft knife

Optional:
+ LEDs
+ Resistors
+ Jumper wires
+ A breadboard
+ M2 bolts and nuts (×2 of each for mounting the Raspberry Pi onto the LEGO® Build Plate)

### Software

+ BuildHAT Python library for controlling the Build HAT
+ Thonny Python IDE
  
### Downloads

+ The final script for this project is available [here]((http://rpf.io/p/en/lego-data-dash-go){:target="_blank"})

--- /collapse ---

Before you begin, you'll need to have set up your Raspberry Pi computer and attached your Build HAT:

--- task ---

Mount your Raspberry Pi on to the LEGO Build Plate using M2 bolts and nuts, making sure the Raspberry Pi is on the side without the 'edge':

 ![Raspberry Pi bolted to a magenta LEGO Build Plate.](images/build_11.jpg)

--- /task ---

Mounting the Raspberry Pi this way round enables easy access to the ports as well as the SD card slot. The Build Plate will allow you to connect the Raspberry Pi to the main structure of your dashboard more easily.

--- task ---

Line up the Build HAT with the Raspberry Pi, ensuring you can see the `This way up` label. Make sure all the GPIO pins are covered by the HAT, and press down firmly. (The example uses a [stacking header](https://www.adafruit.com/product/2223){:target="_blank"}, which makes the pins longer.)

![Image of GPIO pins poking through the top of the Build HAT.](images/build_15.jpg)

--- /task ---

You should now power your Raspberry Pi using the 7.5V barrel jack on the Build HAT, which will allow you to use the motors. If you do not have an official BUildHAT power supply; you can power the buildHAT through the Raspberry Pi USB-C port, but will not be able to power the motors.

--- task ---

If you have not already done so, set up your Raspberry Pi by following these instructions:

[Setting up your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---
You will also need to install the buildhat python library by following these instructions: 

--- collapse ---
---
title: Install the BuildHAT Python library
---

Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

At the prompt type: `sudo pip3 install buildhat`

Press <kbd>Enter</kbd> and wait for the "installation completed" message.

--- /collapse ---

--- /task ---


<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### PROJECT BRIEF: LEGO® data dashboard
<hr style="border-top: 2px solid black;">

Your task is to create a LEGO dashboard that will display your chosen data. The sources for your data can be any API you like, but in this example, we will show you how to access OpenAQ, which requires minimal or no sign up. 

For our example data, we will be measuring:
+ The **NO2** levels at a chosen location. Nitrogen dioxide (NO2) is one of a group of highly reactive gases known as nitrogen oxides or NOx. NO2 is primarily released into the air from the burning of fuel.
+ The **fine particles (PM2.5)** levels at a chosen location. The term **fine particles**, or particulate matter 2.5 (PM2.5), refers to tiny particles or droplets in the air that are two and a half microns (or less) in size. Particles classed as PM2.5 are what make up smoke and smog.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">The example API we are using in this project is from [OpenAQ](https://openaq.org/#/), a global non-profit organisation "fighting air inequality through open data". Globally, **1 in 8 deaths** are due to poor air quality, and OpenAQ collects global air quality data to help inform more people about the problems of increasing air pollution in some parts of the world. </p>


Your dashboard should:
+ Use LEGO® to display your chosen data in a clear way
+ Access an online API to retrieve up-to-date data
+ Have at least two LEGO® indicators

Your dashboard could:
+ Use other electronic components (LEDs, buzzers)
+ Have physical user inputs (LEGO® Technic™ motors, LEGO® Force Sensor, GPIO button, distance sensor)
  
</div>

--- no-print ---

### Get inspiration

--- task ---

Think about the information you would like to display on your dashboard as you investigate these example projects to get more ideas.

This example shows a weather dashboard displaying the current temperature on a vertical slider, the cloud cover using an LED scale, and on the rotating dials it suggests a suitable level of clothing based on the apparent temperature (it includes the wind and other weather in the temperature) and a detailed weather report using World Weather Codes (a.k.a. WMO code).

![Demo Video](images/weather-dash.gif)

--- /task ---

--- /no-print ---

--- print-only ---

![Image showing a weather station dashboard made of LEGO®.](images/example-dash.jpg)

--- /print-only ---


