## Display pollution data with your Dashboard

### Program your slider to display the oxygen level

At the moment your slider is running off of random integers between -175 and 175. (We don't go to 180 as it can cause problems with travel around a full rotation.) We picked these numbers because they are the motor's limits of travel in each direction. The data coming in from your API won't have this range - we need to make it fit the motor.

**Calibrating** the indicator will mean mapping the maximum and minimum possible data values from your API between -175° and 175° on your motor. The highest possible reading will be at 175°, while the lowest possible reading will be at -175°. 

For example: if it's displaying the oxygen (O2) level, the minimum and maximum possible reading on your slider will depend on where you live. Here in Cambridge England, it doesn't really get below -5 degrees celcius. In summer, it *might* get to 35 degrees on a *very* hot day. This means my scale will run from -5 to 35 degrees.

--- task ---

**Think** about what your sliding indicator will measure, and what the lowest and highest readings might be. Write them down somewhere so you don't forget them.

--- /task ---

--- task ---

In a new Thonny window add the following, filling in the variables with your own information as you go:

+ `o2_min_value` is the lowest reading you think you will get
+ `o2_max_value` is the highest reading you think you will get
+ `o2_sensor_data` will be the API command


--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from buildhat import Motor
from time import sleep


motor_temp = Motor('A')
o2_min_value = #input your minimum expected value here
o2_max_value = #input your maximum expected value here
o2_min_angle = -175
o2_max_angle = 175

--- /code ---

--- /task ---

The next part we will write will do some clever maths to map our data range across the motor range. (It's basically the same as the function used in the [LEGO Data Plotter project](https://learning-admin.raspberrypi.org/en/projects/lego-plotter/6).)
 
--- task ---

Add this function beneath your existing code:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 11
line_highlights: 
---
def o2_remap(o2_min_value, o2_max_value, o2_min_angle, o2_max_angle, o2_sensor_data):
    o2_value_range = (o2_max_value - o2_min_value)
    o2_motor_range = (o2_max_angle - o2_min_angle)
    o2_mapped = (((o2_sensor_data - o2_min_value) * o2_motor_range) / o2_value_range) + o2_min_angle
    return int(o2_mapped)
    print(o2_mapped)

--- /code ---

--- /task ---

Now that our function has been created, we need to make a loop that will:

+ pull the temperature data from the API
+ find the angle the motor is currently at
+ move to the new angle to display the reading

--- task ---
Add the following code to the end of your script:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 18
line_highlights: 
---
while True:
    o2_sensor_data  =  API command to pull the data()
    o2_current_angle = motor_temp.get_aposition()
    o2_new_angle = o2_remap(o2_min_value, o2_max_value, o2_min_angle, o2_max_angle, o2_sensor_data)
    sleep(0.5)

--- /code ---

--- /task ---

--- task ---

Save your work as `data_dash.py` and click Run. Your slider should move to display the current oxygen reading. 

--- /task ---

## Program your gauge to show air pollution level

### Calibrate your gauge

At the moment your gauge is running off of random integers between -180 and 180. Calibrating it will mean mapping the maximum and minimum possible data values from your API between -175 and 175 on your motor. The highest possible reading will be at 175 degrees, while the lowest possible reading will be at -175.

--- task ---

Connect the motor from your gauge to port B on the BuildHAT.

--- /task ---

--- task ---

Change your `data_dash.py` script to match the following, filling in the variables with your own information as you go:

`poll_min_value` is the lowest pm25 air pollution reading you think you will get
`poll_max_value` is the highest pm25 air pollution reading you think you will get

--- code ---
---
language: python
filename: gauge_test.py
line_numbers: true
line_number_start: 1 
line_highlights: 11-15, 24-29, 36-38
---
from buildhat import Motor
from time import sleep


motor_temp = Motor('A')
o2_min_value = #input your minimum expected value here
o2_max_value = #input your maximum expected value here
o2_min_angle = -175
o2_max_angle = 175

motor_poll = Motor('B')
poll_min_value = #input your minimum expected value here
poll_max_value = #input your maximum expected value here
poll_min_angle = -175
poll_max_angle = 175

def o2_remap(o2_min_value, o2_max_value, o2_min_angle, o2_max_angle, o2_sensor_data):
    o2_value_range = (o2_max_value - o2_min_value)
    o2_motor_range = (o2_max_angle - o2_min_angle)
    o2_mapped = (((o2_sensor_data - o2_min_value) * o2_motor_range) / o2_value_range) + o2_min_angle
    return int(o2_mapped)
    print(o2_mapped)

def poll_remap(poll_min_value, poll_max_value, poll_min_angle, poll_max_angle, poll_sensor_data):
    poll_value_range = (poll_max_value - poll_min_value)
    poll_motor_range = (poll_max_angle - poll_min_angle)
    poll_mapped = (((poll_sensor_data - poll_min_value) * poll_motor_range) / poll_value_range) + poll_min_angle
    return int(poll_mapped)
    print(o2_mapped)

while True:
    o2_sensor_data  =  API command to pull the o2 data()
    o2_current_angle = motor_temp.get_aposition()
    o2_new_angle = o2_remap(o2_min_value, o2_max_value, o2_min_angle, o2_max_angle, o2_sensor_data)
    sleep(0.5)
    poll_sensor_data  =  API command to pull the pm25 data()
    poll_current_angle = motor_poll.get_aposition()
    poll_new_angle = poll_remap(poll_min_value, poll_max_value, poll_min_angle, poll_max_angle, poll_sensor_data)

--- /code ---

--- /task ---

--- task ---

Save your work by pressing `Ctrl + s` and click Run. You should see your dash begin displaying your data!

--- /task ---

In the next step, we will use the LEGO clock to choose data by time!

--- save ---