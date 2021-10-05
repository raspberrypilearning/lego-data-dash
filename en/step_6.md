## Make an LED scale

Another really cool way to display data is by using a series of LEDs to turn on and off as readings change - the higher the reading, the more LEDs are lit. Like a graphic equaliser on your computer showing the volume of your music:

![](https://media.giphy.com/media/Hzt1XTt6gilFlK8Oea/giphy.gif)

To make an LED display, you'll need a few LED bulbs - the more bulbs you have, the more precise your scale will be. There is an upper limit though - you can only have as many LEDs as there are available GPIO pins. In this example we're using 5 LEDs, but you *could* connect more than ten if you choose.

**Note:** Because of the way the BuildHAT is designed, you **can't access GPIO 14 or 15 (pins 8 and 10)**.

--- task ---

Collect your LEDs, resistors, M-F jumper cables and breadboard together. 
![Image showing Raspberry Pi with BuildHAT, breadboard, LEDs and jumper cables on a workbench](images/LEDbuild1.jpg)

--- /task ---

--- task ---

Look closely at your LEDs - you'll notice that one leg is longer than the other. 
![Image showing an LED in close up on a workbench](images/LEDbuild2.jpg)

--- /task ---

--- task ---

Insert the **short leg** of your LEDs into the **common ground rail** along the edge of your breadboard (it's the one next to the blue line at the very edge), and the long leg into the nearest numbered row:
![Image showing  LEDs lined up on a breadboard](images/LEDbuild3.jpg)

--- /task ---

You need to add a resistor to the circuit, to protect the LEDs from overloading and burning out or popping. Let's do that now.

--- task ---

Take a resistor and insert one end into the **same row** as the first LED in your sequence. Insert the other end of the resistor into the same row, but **on the other side of the spine** of your breadboard, like this:

![Image showing LEDs lined up on a breadboard, with a resistor joining the first row](images/LEDbuild4.jpg)

Repeat for all the LEDs in your sequence:
![Image showing LEDs lined up on a breadboard, with resistors joining the rows](images/LEDbuild5.jpg)

--- /task ---

--- task ---

Insert the M end of your M-F jumper cables into the same row as the resistors, so we can connect them up to the pins on the Raspberry Pi: 
![Image showing LEDs lined up on a breadboard, with resistors joining the rows and jumper cables trailing from the breadboard](images/LEDbuild6.jpg)

--- /task ---

--- task ---

Take the M end of another jumper cable and insert it into the end of the common ground rail:
![Image showing a jumper cable trailing from the common ground rail of the breadboard](images/LEDbuild7.jpg)

--- /task ---

Your finished LED scale should look something like this:

![Image showing LEDs lined up on a breadboard, with resistors joining the rows and jumper cables trailing from the breadboard](images/LEDbuild8.jpg)

The next step is to connect it to the GPIO pins on the Raspberry Pi. 

--- save ---

