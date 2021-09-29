## Make a LEGO sliding indicator

Now it's time to make a LEGO sliding indicator! If you don't want to include a sliding indicator, you can skip to the next step which shows you how to create rotating LEGO dials.

This is what a vertical slider looks like:

![Image showing vertical lego slider acting as a thermometer](images/slider.jpg)

Sliding indicators can also run horizontally if you prefer, by rotating the build 90 degrees anticlockwise.

--- task ---

Follow these build instructions to create a vertical sliding indicator:

INSERT BUILD PDF WHEN DONE

--- /task --- 

--- task ---

Before attaching the motor to the rear of the slider's axle, make sure that it is 'zeroed in', by lining up the two lollipop symbols on the motor's edge:

![Image showing motor 'zeroed in' with aligned symbols](images/aligned_symbols.jpg)

--- /task ---

### Test the sliding indicator

--- task ---

Connect the motor of your slider to Port A on your BuildHAT.

--- /task ---

--- task ---

We will be using the BuildHAT python library, so make sure it is installed:

--- collapse ---
---
title: Installing the BuildHAT python library
---

Open a terminal window on your Raspberry Pi by pressing `Ctrl + Alt + T`.

At the prompt type: `pip3 install buildhat`

Press Enter and wait for the 'installation completed' message.

--- /collapse ---

--- /task ---

--- task ---

Open Thonny on your Raspberry Pi from the Programming menu. 

Enter the following code in a blank tab:

--- code ---
---
language: python
filename: slider_test.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from buildhat import Motor
from time import sleep
from random import randint

motor_slider = Motor('A')

last_value = 0

while True:
    sensor_data = randint(-180, 180)
    print(sensor_data)
    if sensor_data < last_value:
        motor_slider.run_to_position(sensor_data, 100, direction="anticlockwise") # move anti-clockwise
        last_value = sensor_data
    else:
        motor_slider.run_to_position(sensor_data, 100, direction="clockwise") # move clockwise
        last_value = sensor_data
    sleep(0.1)

--- /code ---

Save your work as `slider_test.py` and click Run. You should see your slider move up and down (or back and forth!)

--- /task ---

### Calibrate your slider

At the moment your slider is running off of random integers between -180 and 180. Calibrating it will mean mapping the maximum and minimum possible data values from your API between -180 and 180 on your motor. 



--- save ---
