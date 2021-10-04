## Make a LEGO gauge

Another way to quickly display data is using **dials**, also known as **gauges**. You've definitely seen them before, they are usually round or semicircular and have two main visible parts:

+ The face, which has the scale shown on it
+ The needle, which moves along the scale to display the data reading

![Animated image showing dials moving](https://media.giphy.com/media/9f8bvMFurMTXG/giphy.gif)

A gauge or dial is the simplest type of data readout you can create using LEGO, as it only relies upon creating the face and needle. Because the needle connects directly to your motor, the build is very simple:

INSERT BUILD PDF ONCE DONE

--- task ---

Before attaching the motor to the rear of the gauge's axle, make sure that it is 'zeroed in', by lining up the two lollipop symbols on the motor's edge:

![Image showing motor 'zeroed in' with aligned symbols](images/aligned_symbols.jpg)

--- /task ---

### Create a scale

To finish building the gauge, you will need to create a scale using paper, card or other art supplies. The mechanics and coding are exactly the same, but think now about how you would like your gauge to look. 

 --- task ---
 **Choose** what kind of dial you will make. 
 
 There are two simple types we can create with LEGO:

+ A gauge where the needle spins to indicate a point on the face:
![An image showing a gauge with a needle and scale](/en/images/dial2.gif)

+ A gauge where the whole face turns to display a point at the top with a stationary indicator:
![An image showing a gauge with a moving scale](/en/images/dial1.gif) 

--- /task ---

--- task ---

On a blank piece of paper, trace a neat circle the size you would like your gauge to be. Mark the centre, and cut it out using scissors.

--- /task --- 

--- task ---

Split the circle into equal segments (one for each reading) by drawing lines through the centre, or draw your scale around the edge.

--- /task ---

--- task ---

Draw an icon or write inside each segment what it indicates.

--- /task ---

Once you have finished creating your gauge face, you will need to mount it to your dashboard.

--- collapse ---
---
title: If you are creating a needle gauge
---

To finish building your needle gauge:

--- task ---

Slide the face down over your axle, using blu-tac or tape to stick it down to the dash behind and prevent it from sliding as the axle turns.
![Image showing LEGO axle protruding through gauge face](images/needle-gauge1.jpg)

--- /task ---

--- task ---

Add a 90 degree elbow to the end of your axle and place another axle into it. Make sure it is long enough to reach your scale and clearly indicate the readings.

![Image showing LEGO axle protruding through gauge face with elbow and perpendicular axle](images/needle-gauge2.jpg)

It will help later if your axle is pointing straight up (and your motor is 'zeroed') when you mount it, as it will make it easier to calculate the amount of rotation required for a reading.

--- /task ---

--- /collapse ---

--- collapse ---
---
title: If you are creating a spinning face dial
---

To finish building a spinning gauge:

--- task ---

Mount a single gear behind your face as a spacer, to prevent it from catching on your dashboard. Use some blu-tac to stick the face to this gear.
![Image showing black LEGO gear mounted on axle with tack](/en/images/dial-gauge1.jpg)
![Image showing gauge face mounted on top of black LEGO gear](/en/images/dial-gauge2.jpg)

--- /task ---

--- /collapse ---

### Test your gauge

--- task ---

Connect the motor of your gauge to Port A on your BuildHAT.

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
filename: gauge_test.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from buildhat import Motor
from time import sleep
from random import randint

motor_gauge = Motor('A')

motor_gauge.run_to_position(0,100)

while True:
    angle = randint(-180, 180)
    motor_gauge.run_to_position(angle, 100)
    sleep(0.3)

--- /code ---

Save your work as `gauge_test.py` and press Run. You will see your gauge begin to move!

--- /task ---

### Calibrate your gauge

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

Change your `gauge_test.py` script to match the following, filling in the variables with your own information as you go:

`min_value` is the lowest reading you think you will get
`max_value` is the highest reading you think you will get

--- code ---
---
language: python
filename: gauge_test.py
line_numbers: true
line_number_start: 10 
line_highlights: 
---
from buildhat import Motor
from time import sleep
from random import randint

motor_gauge = Motor('A')
min_value = #input your minimum expected value here
max_value = #input your maximum expected value here
min_angle = -175
max_angle = 175
sensor_data  = #Use an API command to pull the data you want 

def remap(min_value, max_value, min_angle, max_angle, sensor_data):
    value_range = (max_value - min_value)
    motor_range = (max_angle - min_angle)
    mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle
    return int(mapped)

while True:
    remap()
    motor_gauge.run_to_position(mapped, 100)

--- /code ---

