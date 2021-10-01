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

At the moment your slider is running off of random integers between -180 and 180. Calibrating it will mean mapping the maximum and minimum possible data values from your API between -180 and 180 on your motor. The highest possible reading will be at 180 degrees, while the lowest possible reading will be at -180.

For example: if it's displaying the temperature, the minimum possible reading on your slider will depend on where you live. Here in Cambridge England, it doesn't really get below -5 degrees celcius. In summer, it *might* get to 35 degrees on a *very* hot day. This means my scale will run from -5 to 35 degrees.

--- task ---

**Think** about what your sliding indicator will measure, and what the lowest and highest readings might be. Write them down somewhere.

--- /task ---

To map our scale to the available angles on our motor, we need to first work out how wide our scale is (or how many degrees in total from minimum to maximum) and divide 360 by this number. 

For the example above, the temperature in Cambridge ranges from -5 to 35. This means that my scale is 40 units wide: 35 - -5 = 40

--- task ---

**Calculate** how wide your scale is by subtracting the minimum possible reading from the maximum possible reading. (Note: subtracting a negative number will make your answer bigger!)

--- /task ---

We now need to set our motor to move by a specific number of degrees when the reading changes. To work this out, we divide 360 by the width of your scale. 

For our Cambridge example, this would be 360 / 40 = 9. This means that we need to move 9 degrees around the motor for every degree on our scale. 

--- task ---

**Calculate** the angle change for one degree of your scale. Write down the answer - we'll need it later. 

--- /task ---



--- save ---
