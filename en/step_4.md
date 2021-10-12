## Make a LEGO® gauge

Another way to quickly display data is by using **dials**, also known as **gauges**. You've definitely seen them before; they are usually round or semicircular and have two main visible parts:

+ The face, which has the scale shown on it
+ The needle, which moves along the scale to display the data reading

![Animated image showing dials moving.](https://media.giphy.com/media/uozBSFuz99USA/giphy.gif)

A gauge or dial is the simplest type of data readout you can create using LEGO®, as it only relies upon creating the face and needle. Because the needle connects directly to your motor, the build is very simple:

--- task ---

Before attaching the motor to the rear of the gauge's axle, make sure that it is 'zeroed in', by lining up the two lollipop symbols on the motor's edge:

![Image showing the motor 'zeroed in' with aligned symbols.](images/aligned_symbols.jpg)

--- /task ---

### Create a scale

To finish building the gauge, you will need to create a scale using paper, card, or other art supplies. The mechanics and coding are exactly the same, but think now about how you would like your gauge to look. 

 --- task ---
 **Choose** what kind of dial you will make. 
 
 There are two simple types you can create with LEGO®:

+ A gauge where the needle spins to indicate a point on the face:
![An image showing a gauge with a needle and scale.](images/dial2.gif)

+ A gauge where the whole face turns to display a point at the top with a stationary indicator:
![An image showing a gauge with a moving scale.](images/dial1.gif) 

--- /task ---

--- task ---

On a blank piece of paper, trace a neat circle the size you want your gauge to be. Mark the centre, and cut it out using scissors.

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

Slide the face down over your axle, using Blu Tack or tape to stick it down to the dashboard behind it and prevent it from sliding as the axle turns.
![Image showing a LEGO® axle protruding through a gauge's face.](images/needle-gauge1.jpg)

--- /task ---

--- task ---

Add a 90 degree elbow to the end of your axle and place another axle into it. Make sure it is long enough to reach your scale and clearly indicate the readings.

![Image showing the LEGO® axle protruding through the gauge's face with an elbow and perpendicular axle connected.](images/needle-gauge2.jpg)

It will help later if your axle is pointing straight up (and your motor is 'zeroed') when you mount it, as it will make it easier to calculate the amount of rotation required for a reading.

--- /task ---

--- /collapse ---

--- collapse ---
---
title: If you are creating a spinning face dial
---

To finish building a spinning gauge:

--- task ---

Mount a single gear behind your dial face as a spacer, to prevent it from catching on your dashboard. Use some Blu Tack to stick the face to this gear. If you have created an incremental scale around the gauge, mount it with the middle of the scale at the top (in line with the 'zeroed' lollipop symbols) and the minimum and maximum values at the bottom.

![Image showing a black LEGO® gear mounted on an axle with some tack.](/en/images/dial-gauge1.jpg)
![Image showing the gauge face mounted on top of a black LEGO® gear.](/en/images/dial-gauge2.jpg)

--- /task ---

--- /collapse ---

### Test your gauge

--- task ---

Connect the motor of your gauge to port A on your Build HAT.

--- /task ---

--- task ---

You will be using the BuildHAT Python library, so make sure it is installed:

--- collapse ---
---
title: Install the BuildHAT Python library
---

Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

At the prompt type: `pip3 install buildhat`

Press <kbd>Enter</kbd> and wait for the "installation completed" message.

--- /collapse ---

--- /task ---

--- task ---

Open **Thonny** on your Raspberry Pi from the **Programming menu**. 

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

Save your work as `gauge_test.py` and press **Run**. You will see your gauge begin to move!

--- /task ---

