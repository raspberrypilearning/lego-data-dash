## Display pollution data with your Dashboard

At the moment your dash is running off of random integers between -175 and 175. (We don't go to 180 as it can cause problems with travel around a full rotation.) We picked these numbers because they are the motor's limits of travel in each direction. The data coming in from your API won't have this same range - we need to make it fit the motors.

**Calibrating** the indicators will mean mapping the maximum and minimum possible data values from your API between -175° and 175° on your motor. The highest possible reading will be at -175°, while the lowest possible reading will be at 175°. (Because we have mounted the motors in reverse!)

For our example we will display the **fine particles (PM2.5)** measurement on the gauge, while the slider will display the Nitrogen Dioxide (NO2) level. The term **fine particles**, or particulate matter 2.5 (PM2.5), refers to tiny particles or droplets in the air that are two and a half microns (or less) in width. The particles measured by PM2.5 are what make up most smoke and smog, and make it hard to see.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Like inches, meters and miles, a <span style="color: #0faeb0">micron</span> is a unit of measurement for distance. There are about 25,000 microns in an inch. The widths of the larger particles in the PM2.5 size range would be about thirty times smaller than that of a human hair.  These particles are so small that several thousand of them could fit on the full stop at the end of this sentence.</p> 

In our example, the slider will display the Nitrogen Dioxide (NO2) level. The maximum possible reading on your slider will depend on where you live, because urban areas will always have higher readings than rural ones. The minimum reading possible is obviously 0, but we will want to consider what the normal range for what we are attempting to measure and add a bit to that.  

In order to work out what the maximum likely reading should be, you can see the historical data from your chosen location on the webpage you opened earlier:

![Image showing graphed historical NO2 data from Sandy roadside](images/historicaldata_no2.jpg)

Here we can see that while there are some major outliers, around 60% (or 0.6) should be more than enough as our maximum value for most readings from the *Sandy Roadside* air quality station. (If you want to simply make your scale from 1-100 you can do that too - just make `max_value = 100`)

--- task ---

Connect your sliding indicator motor to Port 'A'. 
Connect your gauge indicator motor to Port 'B'.

--- /task ---

--- task ---

In a new Thonny window, type the following:

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
from datetime import datetime, timedelta
import requests

no2_motor = Motor('A')           # set up slider motor
no2_motor.run_to_position(0,100) # reset slider position
pm25_motor = Motor('B')           # set up gauge motor
pm25_motor.run_to_position(0,100) # reset gauge position

no2_min_value = 0         # the lowest NO2 reading you think you will get (This should hopefully be around 0)
no2_max_value = 60        # the highest NO2 reading you think you will get 
no2_min_angle = 175       # miniumum motor travel
no2_max_angle = -175      # maximum motor travel

pm25_min_value = 0        # the lowest NO2 reading you think you will get (This should hopefully be around 0)
pm25_max_value = 100      # the highest pm25 reading you think you will get 
pm25_min_angle = 175      # miniumum motor travel
pm25_max_angle = -175     # maximum motor travel

--- /code ---

--- /task ---

Now that we have imported the necessary libraries and set up our measurement details, we will set up our query to the API by making a few **dictionaries** of terms we will use.

--- task ---

In your Thonny window, add this code to the end of your script:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 21
line_highlights: 
---
base_url = 'https://docs.openaq.org/v2/measurements'

payload = {                    # create a dictionary for the API request
    'date_from':'',
    'date_to':'',
    'location_id':'2480',      # This number should be the ID number taken from the URL earlier
    'order_by':'datetime',
    'sort':'asc',
    'has_geo':'true',
    'limit':'100',
    'offset':'0',
}

pollution = {                  # create a dictionary for the pollution readings
    'no2' : 0,                 # here we are looking for no2 and pm25 - yours may differ!
    'pm25': 0,
    }

--- /code ---

--- /task ---

The next function we need to write will query the API using the parameters we have set up. 

--- task ---
 
At the end of your script, add this code:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 39
line_highlights: 
---
def check_weather():
    now = datetime.now()           # gets the time now
    delta = datetime.now() - timedelta(days=1)         # creates a time difference of one day
    
    payload['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00'  # inserts our date and time into the dictionary above
    payload['date_to'] = f'{now:%Y-%m-%d}T{now:%H:%M:%S}+00:00'
    
    response = requests.get(base_url, params=payload)          # queries the API database
    
    if response.status_code != 200:          # check for connection to API
        print('no response from server')
        return
    
    data = response.json()
        
    for reading in data['results']:
        if reading['parameter'] == 'no2':       # This will depend upon what pollutant you are measuring
            pollution['no2'] = reading['value']
            print(pollution['no2'])
        if reading['parameter'] == 'pm25':      # This will depend upon what pollutant you are measuring
            pollution['pm25'] = reading['value']
            print(pollution['pm25'])

    output_results()   
    sleep(1)

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
line_number_start: 65
line_highlights: 
---
def remap(min_value, max_value, min_angle, max_angle, sensor_data):                    # create function
    value_range = (max_value - min_value)                                              # work out how wide your value range is
    motor_range = (max_angle - min_angle)                                              # work out how wide your motor range is
    mapped = (((sensor_data - min_value) * motor_range) / value_range) + min_angle     # stretch your value range across your motor range
    return int(mapped)                                           # give back a number that shows the value as an angle on the motor

--- /code ---

--- /task ---

Now that our function has been created, we need to make a loop that will:

+ find the angle the motor is currently at
+ pull the pollutant data from the `remap` function to use as the new angle for our motors
+ move to the new angle to display the reading

--- task ---

Add the following code to the end of your script, on a new line:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 73
line_highlights: 
---
def output_results():
    print(f'NO2 = {pollution['no2']}')
    no2_current_angle = no2_motor.get_aposition()
    no2_sensor_data = int(pollution['no2'])
    no2_new_angle = remap(no2_min_value, no2_max_value, no2_min_angle, no2_max_angle, no2_sensor_data)
    print(no2_new_angle)
    if no2_new_angle > no2_current_angle:
        no2_motor.run_to_position(no2_new_angle, 100, direction='anticlockwise')
        print('Turning CW')
    elif no2_new_angle < no2_current_angle:
        no2_motor.run_to_position(no2_new_angle, 100, direction='clockwise')
        print('Turning ACW')
    sleep(0.1)
    pm25_sensor_data = int(pollution['pm25'])
    print(f"PM2.5 = {pollution['pm25']}")
    pm25_current_angle = pm25_motor.get_aposition()
    print(pm25_current_angle)
    pm25_new_angle = remap(pm25_min_value, pm25_max_value, pm25_min_angle, pm25_max_angle, pm25_sensor_data)
    pm25_motor.run_to_position(pm25_new_angle, 100)

--- /code ---

--- /task ---

The last part of our code now needs to call our `check_weather()` function to make it all go, and periodically check the API for updated data. 

--- task ---

At the end of your script on a new line (making sure it isn't indented) type:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 93
line_highlights: 
---
while True:
    check_weather()
    sleep(3600)   # wait an hour before checking again (make this smaller for testing purposes)
--- /code ---

--- /task ---

--- task ---

Save your work as `data_dash.py` and click Run. Your slider should move to display the current NO2 reading from your chosen OpenAQ station, and your gauge should move to display the PM2.5 reading. Well done!

--- /task ---

--- save ---
