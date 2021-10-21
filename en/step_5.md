## Make an LED scale

Another really cool way to display data is by using a series of LEDs that turn on and off as readings change — the higher the reading, the more LEDs are lit; like a graphic equaliser on your computer showing the volume of your music.

![Image displaying graphic equaliser moving up and down](https://media.giphy.com/media/Hzt1XTt6gilFlK8Oea/giphy.gif)

To make an LED display, you'll need a few LED bulbs — the more bulbs you have, the more precise your scale will be. There is an upper limit though: you can only have as many LEDs as there are available GPIO pins. In this example, we're using five LEDs, but you **could** connect more than ten if you choose.

**Note:** Because of the way the Build HAT is designed, you **can't access GPIO 14 or 15 (pins 8 and 10)**.

--- task ---

Collect your LEDs, resistors, M–F jumper cables, and breadboard together. 
![Image showing a Raspberry Pi with Build HAT, breadboard, LEDs, and jumper cables on a workbench.](images/LEDbuild1.jpg)

--- /task ---

--- task ---

Look closely at your LEDs — you'll notice that one leg is longer than the other. 
![Image showing an LED in close up on a workbench.](images/LEDbuild2.jpg)

--- /task ---

--- task ---

Insert the **short leg** of your LEDs into the **common ground rail** along the edge of your breadboard (it's the one next to the blue line at the very edge), and the long leg into the nearest numbered row:
![Image showing LEDs lined up on a breadboard.](images/LEDbuild3.jpg)

--- /task ---

You need to add a resistor to the circuit, to protect the LEDs from overloading and burning out or popping. Now is a good time to do that.

--- task ---

Take a resistor and insert one end into the **same row** as the first LED in your sequence. Insert the other end of the resistor into the same row, but **on the other side of the spine** of your breadboard, like this:

![Image showing LEDs lined up on a breadboard, with a resistor joining the first row.](images/LEDbuild4.jpg)

Repeat for all the LEDs in your sequence:
![Image showing LEDs lined up on a breadboard, with resistors joining the rows.](images/LEDbuildX.jpg)

--- /task ---

--- task ---

Insert the M end of your M–F jumper cables into the same row as the resistors, so you can connect them to the pins on the Raspberry Pi: 
![Image showing LEDs lined up on a breadboard, with resistors joining the rows, and jumper cables trailing from the breadboard.](images/LEDbuild5.jpg)

--- /task ---

--- task ---

Take the M end of another jumper cable and insert it into the end of the common ground rail:
![Image showing a jumper cable trailing from the common ground rail of the breadboard.](images/LEDbuild6.jpg)

--- /task ---

Your finished LED scale should look something like this:

![Image showing LEDs lined up on a breadboard, with resistors joining the rows, and jumper cables trailing from the breadboard.](images/LEDbuild7.jpg)

The next step is to connect it to the GPIO pins on the Raspberry Pi. 

--- task ---

Take the F end of the jumper cable connected to your common ground rail, and connect it to Pin 39. This is one of several ground pins on the Raspberry Pi, which will provide the grounding for **all** of your LED bulbs.
![Image showing a black jumper cable connected to Pin 39 on the Raspberry Pi.](images/LEDbuild9.jpg)

--- /task ---

--- task ---

Connect the other cables to numbered GPIO pins, taking note of which ones you have attached your LEDs to. 

In this example, we have used Pins 16, 19, 20, 21, and 26 (to keep them all at one end for tidiness):
![Image showing jumper cables trailing from the Raspberry Pi GPIO pins.](images/LEDbuild10.jpg)

--- /task ---

Now that your LED sequence is connected to your Raspberry Pi, you need to power it up and program it. 

--- task ---

Connect the 7.5V power supply to the barrel jack on your Build HAT. You should see your Raspberry Pi power up and load the Raspberry Pi OS Desktop.

--- /task ---

--- task ---

Open **Thonny** from your **Programming menu**. 

The first lines of your script will import the gpiozero and randint libraries and set up your LEDs to be controllable. You will need to change the values in brackets to match the numbered pins your LEDs are connected to. **Note:** The order of these numbers is important! The pin numbers should go from the lowest on your 'bar graph' to the highest.

In the blank window enter the following code:

--- code ---
---
language: python
filename: led_bargraph.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from gpiozero import LEDBarGraph
from random import randint

graph = LEDBarGraph(16, 19, 20, 21, 26) #The order of these numbers should match the pins you connected up 

--- /code ---

--- /task ---

Now that you have your LEDs ready to program, the next part of your code should pull the data you want to measure, then determine how many LEDs to switch on based on the result. For testing purposes, you should use random data.

The intention is to have the LEDs turn on as the reading increases, and to turn off as it decreases. As with the other indicators, you will need to map your data across your scale. 

--- task ---

Enter the following code at the end of your open script:

--- code ---
---
language: python
filename: led_sequence.py
line_numbers: true
line_number_start: 9
line_highlights: 
---
while True:
  data_reading = randint(0, 100)
  graph.value = 1/data_reading #This creates a decimal value for the graph to display
  sleep(0.5)
--- /code ---

--- /task ---

--- task ---

Save your work as `led_sequence.py` and click **Run**. You should see your bar graph begin to light up!

![Animated image showing a changing bar graph made of LEDs.](images/LEDbuild.gif)

--- /task ---

--- save ---
