### Use the LEGO clock to filter data by time

You might not want to display the data for **right now** on your dash. It can be very useful to be able to look at historical data to compare and contrast, as well as predict likely future readings. 

We can connect your LEGO clock up to the dash, and use it to choose the time from which you want to query the database. 

At the top of your script, we will need to import some new libraries to handle some of the time and mathematical operations. We will also need to set up our clock motor and button to be ready to use.  

--- task ---

Change your script to include the following lines:
 
---code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 1 
line_highlights: 1,3,17,18,19,21
---
from buildhat import Motor, ForceSensor   # Make sure you get both capital letters in ForceSensor!
from time import sleep
from math import floor

motor_no2 = Motor('A')
no2_min_value = 0
no2_max_value = 0.3
no2_min_angle = -175
no2_max_angle = 175

motor_pm25 = Motor('B')
pm25_min_value = 0
pm25_max_value = 100
pm25_min_angle = -175
pm25_max_angle = 175

motor_time = Motor('C')
motor_time.run_to_position(0,100)
time = 0

button = ForceSensor('D')
--- /code ---

--- /task ---

Now we will add a function that will return the time to us, ready to use in our API call. 

--- task ---

Above your `while True:` loop, add the following code:

--- code ---
---
language: python
filename: data_dash.py
line_numbers: true
line_number_start: 21
line_highlights: 23-46
---
button = ForceSensor('D')

def timecheck():
    angle = motor_time.get_aposition() #Find what angle the hand is at
    print(angle)
    
    if angle <0:
        angle += 360 #Convert negative angle to positive
    else:
        pass
    print(angle)

    if time == 0:
        meridian = "am"
    else:
        meridian = "pm"
    
    hour = int(floor(angle/30)) #find the hour by using 30 degree increments
    hour24 = int(floor(angle/30))+ time  #find 24 hour time by adding 12
    minute = int(((angle - (30*hour))/30)*60) #calculate the minutes by working out the decimal remainder as a portion of 60 mins
    
    if angle == 0:
        print("Choose a time on the clock! Press the button to change between am and pm!")
    else:
        print('The time is ' + (str(hour).zfill(2)) +':'+(str(minute).zfill(2)) +' ' + meridian)
    sleep(1)

    clocktime= FANCY THING THAT CONVERTS TO UTC ¯\_(ツ)_/¯
    return clocktime

--- /code ---

--- /task ---

Now, we need to call the `timecheck()` function in our main loop. 


--- save ---


