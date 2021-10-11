## Display pollution data with your Dashboard

### Program your slider to display the oxygen level

At the moment your slider is running off of random integers between -175 and 175. (We don't go to 180 as it can cause problems with travel around a full rotation.) We picked these numbers because they are the motor's limits of travel in each direction. The data coming in from your API won't have this range - we need to make it fit the motor.

**Calibrating** the indicator will mean mapping the maximum and minimum possible data values from your API between -175° and 175° on your motor. The highest possible reading will be at 175°, while the lowest possible reading will be at -175°. 

For example: if it's displaying the Carbon Monoxide (CO) level, the minimum and maximum possible reading on your slider will depend on where you live. The minimum reading possible is 0, 

--- task ---

**Think** about what your sliding indicator will measure, and what the lowest and highest readings might be. Write them down somewhere so you don't forget them. For an NO2 reading

--- /task ---

--- task ---

In a new Thonny window add the following, filling in the variables with your own information as you go:

+ `no2_min_value` is the lowest NO2 reading you think you will get (This should hopefully be around 0)
+ `no2_max_value` is the highest NO2 reading you think you will get (This shouldn't be more than 0.3)
+ `no2_sensor_data` will be the API command


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
no2_min_value = #input your minimum expected value here
no2_max_value = #input your maximum expected value here
no2_min_angle = -175
no2_max_angle = 175

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
def no2_remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data):
    no2_value_range = (no2_max_value - no2_min_value)
    no2_motor_range = (no2_max_angle - no2_min_angle)
    no2_mapped = (((no2_sensor_data - no2_min_value) * no2_motor_range) / no2_value_range) + no2_min_angle
    return int(no2_mapped)
    print(no2_mapped)

--- /code ---

--- /task ---

Now that our function has been created, we need to make a loop that will:

+ pull the pollutant data from the API
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
    no2_sensor_data  =  API command to pull the data()
    no2_current_angle = motor_temp.get_aposition()
    no2_new_angle = no2_remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data)
    sleep(0.5)

--- /code ---

--- /task ---

--- task ---

Save your work as `data_dash.py` and click Run. Your slider should move to display the current oxygen reading. 

--- /task ---

## Program your gauge to show air pollution level

### Calibrate your gauge

At the moment your gauge is running off of random integers between -175 and 175. Calibrating it will mean mapping the maximum and minimum possible data values from your API between -175 and 175 on your motor. The highest possible reading will be at 175 degrees, while the lowest possible reading will be at -175.

For our example we will measure the **fine particles (PM2.5)** measurement.The term **fine particles**, or particulate matter 2.5 (PM2.5), refers to tiny particles or droplets in the air that are two and a half microns (or less) in width. The particles measured by PM2.5 are what make up smoke and smog.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Like inches, meters and miles, a <span style="color: #0faeb0">micron</span> is a unit of measurement for distance. There are about 25,000 microns in an inch. The widths of the larger particles in the PM2.5 size range would be about thirty times smaller than that of a human hair.  These smaller particles are so small that several thousand of them could fit on the full stop at the end of this sentence.</p> 

--- task ---

Connect the motor from your gauge to port B on the BuildHAT.

--- /task ---

--- task ---

Change your `data_dash.py` script to match the following, filling in the variables with your own information as you go:

`poll_min_value` is the lowest pm25 air pollution reading you think you will get (This should hopefully be around 0)
`poll_max_value` is the highest pm25 air pollution reading you think you will get (This will be around 65 - more than that and you'll have trouble seeing!)

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
no2_min_value = #input your minimum expected value here
no2_max_value = #input your maximum expected value here
no2_min_angle = -175
no2_max_angle = 175

motor_poll = Motor('B')
poll_min_value = #input your minimum expected value here
poll_max_value = #input your maximum expected value here
poll_min_angle = -175
poll_max_angle = 175

def no2_remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data):
    no2_value_range = (no2_max_value - no2_min_value)
    no2_motor_range = (no2_max_angle - no2_min_angle)
    no2_mapped = (((no2_sensor_data - no2_min_value) * no2_motor_range) / no2_value_range) + no2_min_angle
    return int(no2_mapped)
    print(no2_mapped)

def poll_remap(poll_min_value, poll_max_value, poll_min_angle, poll_max_angle, poll_sensor_data):
    poll_value_range = (poll_max_value - poll_min_value)
    poll_motor_range = (poll_max_angle - poll_min_angle)
    poll_mapped = (((poll_sensor_data - poll_min_value) * poll_motor_range) / poll_value_range) + poll_min_angle
    return int(poll_mapped)
    print(no2_mapped)

while True:
    no2_sensor_data  =  API command to pull the CO data()
    no2_current_angle = motor_temp.get_aposition()
    no2_new_angle = no2_remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data)
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