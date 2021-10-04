## Display pollution data with your Dashboard

### Program your slider to display the temperature

At the moment your slider is running off of random integers between -170 and 170. Calibrating it will mean mapping the maximum and minimum possible data values from your API between -175 and 175 on your motor. The highest possible reading will be at 175 degrees, while the lowest possible reading will be at -175. (We don't go to 180 as it can cause problems with travel around a full rotation.)

For example: if it's displaying the temperature, the minimum possible reading on your slider will depend on where you live. Here in Cambridge England, it doesn't really get below -5 degrees celcius. In summer, it *might* get to 35 degrees on a *very* hot day. This means my scale will run from -5 to 35 degrees.

--- task ---

**Think** about what your sliding indicator will measure, and what the lowest and highest readings might be. Write them down somewhere.

--- /task ---

--- task ---

In a new Thonny window add the following, filling in the variables with your own information as you go:

+ `temp_min_value` is the lowest reading you think you will get
+ `temp_max_value` is the highest reading you think you will get
+ `temp_sensor_data` will be the API command


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
from random import randint

motor_temp = Motor('A')
temp_min_value = #input your minimum expected value here
temp_max_value = #input your maximum expected value here
temp_min_angle = -175
temp_max_angle = 175
 

def temp_remap(temp_min_value, temp_max_value, temp_min_angle, temp_max_angle, temp_sensor_data):
    temp_value_range = (temp_max_value - temp_min_value)
    temp_motor_range = (temp_max_angle - temp_min_angle)
    temp_mapped = (((temp_sensor_data - temp_min_value) * temp_motor_range) / temp_value_range) + temp_min_angle
    return int(temp_mapped)

while True:
    temp_sensor_data  =  API command to pull the data()
    temp_current_angle = motor_temp.get_aposition()
    temp_new_angle = temp_remap(temp_min_value, temp_max_value, temp_min_angle, temp_max_angle, temp_sensor_data)

--- /code ---

--- /task ---

--- task ---

Save your work as `data_dash.py` and click Run. Your slider should move to  

--- /task ---

## Program your gauge to show air pollution level

### Calibrate your gauge

At the moment your gauge is running off of random integers between -180 and 180. Calibrating it will mean mapping the maximum and minimum possible data values from your API between -175 and 175 on your motor. The highest possible reading will be at 175 degrees, while the lowest possible reading will be at -175.

--- task ---

Connect the motor from your gauge to port B on the BuildHAT.

--- /task ---

--- task ---

Change your `dash_test.py` script to match the following, filling in the variables with your own information as you go:

`poll_min_value` is the lowest air pollution reading you think you will get
`poll_max_value` is the highest air pollution reading you think you will get

--- code ---
---
language: python
filename: gauge_test.py
line_numbers: true
line_number_start: 1 
line_highlights: 11-15, 23-27, 33-35
---
from buildhat import Motor
from time import sleep
from random import randint

motor_temp = Motor('A')
temp_min_value = #input your minimum expected value here
temp_max_value = #input your maximum expected value here
temp_min_angle = -175
temp_max_angle = 175

motor_poll = Motor('B')
poll_min_value = #input your minimum expected value here
poll_max_value = #input your maximum expected value here
poll_min_angle = -175
poll_max_angle = 175

def temp_remap(temp_min_value, temp_max_value, temp_min_angle, temp_max_angle, temp_sensor_data):
    temp_value_range = (temp_max_value - temp_min_value)
    temp_motor_range = (temp_max_angle - temp_min_angle)
    temp_mapped = (((temp_sensor_data - temp_min_value) * temp_motor_range) / temp_value_range) + temp_min_angle
    return int(temp_mapped)

def poll_remap(poll_min_value, poll_max_value, poll_min_angle, poll_max_angle, poll_sensor_data):
    poll_value_range = (poll_max_value - poll_min_value)
    poll_motor_range = (poll_max_angle - poll_min_angle)
    poll_mapped = (((poll_sensor_data - poll_min_value) * poll_motor_range) / poll_value_range) + poll_min_angle
    return int(poll_mapped)

while True:
    temp_sensor_data  =  API command to pull the data()
    temp_current_angle = motor_temp.get_aposition()
    temp_new_angle = temp_remap(temp_min_value, temp_max_value, temp_min_angle, temp_max_angle, temp_sensor_data)
    poll_sensor_data  =  API command to pull the data()
    poll_current_angle = motor_poll.get_aposition()
    poll_new_angle = poll_remap(poll_min_value, poll_max_value, poll_min_angle, poll_max_angle, poll_sensor_data)

--- /code ---

--- /task ---

--- task ---

Save your work by pressing `Ctrl + s` and click Run. You should see your dash begin displaying your data!

--- /task ---