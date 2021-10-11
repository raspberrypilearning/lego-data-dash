## Make a LEGO sliding indicator

Now it's time to make a LEGO sliding indicator! If you don't want to include a sliding indicator, you can skip to the next step which shows you how to create rotating LEGO dials.

This is what a vertical slider looks like:

![Image showing vertical lego slider acting as a thermometer](images/slider.jpg)

Sliding indicators can also run horizontally if you prefer, by rotating the build 90 degrees anticlockwise.

--- task ---

Follow these build instructions to create a vertical sliding indicator:

<mark>INSERT BUILD PDF WHEN DONE</mark>

--- /task --- 

--- task ---

Take a yellow plate element and attach two blue beams using 90 degree stud brackets.
![Image showing build plate with blue legs](images/sliderbuild1.jpg)

--- /task ---

--- task ---

Attach two grey straight brackets, one column apart.
![Image showing build plate with two straight brackets](images/sliderbuild2.jpg)

--- /task ---

--- task ---

Attach two grey double length studs with spacers on one end to the plate element above the brackets. 
![Image showing build plate with two straight brackets and studs](images/sliderbuild3.jpg)

--- /task ---

--- task ---

Attach two yellow (three hole) beams horizontally between the two straight brackets. 
![Image showing build plate with two straight brackets and studs](images/sliderbuild4.jpg)

--- /task ---

--- task ---

Take a small black gear and a short axle and join them together. 
![Image showing build plate with two straight brackets and studs and an axle and gear](images/sliderbuild5.jpg)

--- /task ---

--- task ---
Insert the axle through the build plate above the right bracket as shown: 
![Image showing build plate with two straight brackets and studs and an axle and gear mounted in the plate](images/sliderbuild6.jpg)

--- /task ---

--- task ---

Take a toothed bar, a red axle and an indicator arrow. Insert the axle into one end of the toothed bar, with the indicator arrow pointing toward the toothed side:
![Image showing toothed bar, axle and indicator arrow together](images/sliderbuild11.jpg)

--- /task ---

--- task ---

Slide the toothed bar down into the top of the mechanism. 

You will have to pull the gear forward to allow it past, then push the gear back in to fit between the teeth. The mechanism will slide easily up and down while the gear and axle are free. Connecting a motor will hold it steady.
![Image showing build plate with two straight brackets and studs and an axle and gear mounted in the plate with the slider bar inserted](images/sliderbuild8.jpg)
 
--- /task ---

--- task ---

Take a Spark motor and add two studs to the flat side, in the top two holes. 
![Image showing build plate with two straight brackets and studs and an axle and gear mounted in the plate with the slider bar inserted, and a motor on the table](images/sliderbuild9.jpg)

--- /task ---

--- task ---

Before attaching the motor to the rear of the slider's axle, make sure that it is 'zeroed in', by lining up the two lollipop symbols on the motor's edge:

![Image showing motor 'zeroed in' with aligned symbols](images/aligned_symbols.jpg)

--- /task ---

--- task ---

Adjust your toothed bar so the gear sits about halfway along, then mount the motor behind the board using the two studs while holding the toothed bar in place. 
Make sure the axle fits into the hole on the **flat side** of the motor. It should keep the slider held steady now, around halfway along the bar.
![Image showing build plate with a motor mounted on the back](images/sliderbuild10.jpg)

--- /task ---

### Test the sliding indicator

To program your sliding indicator, we can reuse some of the code written in the [LEGO Data Plotter](https://projects.raspberrypi.org/en/projects/lego-plotter) project as they're very much the same mechanism.

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

### Create the scale for your sliding indicator

Now we know it works, we will need to create a scale for the sliding indicator, so we know what it means.

--- task ---

Get a piece of card about as long as your toothed bar. Stick it next to the sliding indicator, under the pointer. Have a marker or pencil ready.

--- /task ---

--- task ---

Open Thonny on your Raspberry Pi from the Programming menu. 

Into the shell (the window at the bottom) next to the three arrows, type:
`from buildhat import Motor` and press Enter. You should see a new line appear with three more arrows.

--- /task ---

--- task ---
Now type:
`motor = = Motor('A')` and press Enter.
--- /task ---

Now we've set up our slider motor to run, we will send it to the maximum and minimum readings to see how far it can travel - then mark those places on the card.

--- task ---

Type: 
`motor.run_to_position(-180, 100)` and press Enter. Mark the card at the place the arrow indicates. This is your minimum possible readout.

--- /task ---

--- task ---

Type: 
`motor.run_to_position(180, 100, direction=clockwise)` and press Enter. Mark the card at the place the arrow indicates. This is your maximum possible readout.

--- /task ---

We now know where our minumum and maximum possible readings will show up. Once we link it to some data, we will be able to create an accurate scale to show it. 

### Programming your sliding indicator to show live data

--- task ---
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

motor_slider.run_to_position(0,100)

while True:
    current_angle = motor_slider.get_aposition()
    new_angle = randint(-175, 175)
    print(sensor_data)
    if new_angle > current_angle:
        motor_slider.run_to_position(new_angle, 100, direction="clockwise")
        print('Turning CW')
    elif new_angle < current_angle:
        motor_slider.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)

--- /code ---

Save your work as `slider_test.py` and click Run. You should see your slider move up and down (or back and forth!)

--- /task ---

--- save ---