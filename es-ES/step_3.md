## Make a LEGO® sliding indicator

Now it's time to make a LEGO® sliding indicator! If you don't want to include a sliding indicator, you can skip to the next step, which shows you how to create rotating LEGO dials.

This is what a vertical slider looks like:

![Image showing a vertical LEGO® slider acting as a thermometer.](images/slider.jpg)

Sliding indicators can also run horizontally if you prefer, by rotating the build 90 degrees anti-clockwise.

--- task ---

Follow these build instructions to create a vertical sliding indicator:

To construct this model, follow our handy building guide here or [download it.](resources/lego-data-dash-slider.pdf)
<embed src="resources/lego-data-dash-slider.pdf" width="600" height="500" alt="pdf" pluginspage="https://www.adobe.com/products/acrobat/readstep2.html">
  </p> 
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Take a yellow plate element and attach two blue beams using 90 degree stud brackets. <img src="images/sliderbuild1.jpg" alt="Image showing a Build Plate with blue legs." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Attach two grey straight brackets, one column apart. <img src="images/sliderbuild2.jpg" alt="Image showing the Build Plate with two straight brackets." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Attach two grey double length studs with spacers on one end to the plate element above the brackets. <img src="images/sliderbuild3.jpg" alt="Image showing the Build Plate with two straight brackets and studs." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Attach two yellow (three-hole) beams horizontally between the two straight brackets. <img src="images/sliderbuild4.jpg" alt="Image showing the Build Plate with two straight brackets and studs." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Take a small black gear and a short axle, and join them together. <img src="images/sliderbuild5.jpg" alt="Image showing the Build Plate with two straight brackets and studs, and an axle and gear." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Insert the axle through the Build Plate above the right bracket as shown: <img src="images/sliderbuild6.jpg" alt="Image showing the Build Plate with two straight brackets and studs, and an axle and gear mounted on the plate." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Take a toothed bar, a red axle, and an indicator arrow. Insert the axle into one end of the toothed bar, with the indicator arrow pointing toward the toothed side: <img src="images/sliderbuild11.jpg" alt="Image showing the toothed bar, axle, and indicator arrow." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Slide the toothed bar down into the top of the mechanism.
  </p>
  
  <p spaces-before="0">
    You will have to pull the gear forward to allow it past, then push the gear back in to fit between the teeth. The mechanism will slide easily up and down while the gear and axle are free. Connecting a motor will hold it steady. <img src="images/sliderbuild8.jpg" alt="Image showing the Build Plate with two straight brackets and studs, and an axle and gear mounted on the plate with the slider bar inserted." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Take a motor and add two studs to the flat side, in the top two holes. <img src="images/sliderbuild9.jpg" alt="Image showing the Build Plate with two straight brackets and studs, and an axle and gear mounted on the plate with the slider bar inserted, and a motor on the table." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Before attaching the motor to the rear of the slider's axle, make sure that it is 'zeroed in', by lining up the two lollipop symbols on the motor's edge:
  </p>
  
  <p spaces-before="0">
    <img src="images/aligned_symbols.jpg" alt="Image showing motor 'zeroed in' with aligned symbols." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    --- task ---
  </p>
  
  <p spaces-before="0">
    Adjust your toothed bar so the gear sits about halfway along it, then mount the motor behind the board using the two studs while holding the toothed bar in place. Make sure the axle fits into the hole on the <strong x-id="1">flat side</strong> of the motor. It should keep the slider held steady now, around halfway along the bar. <img src="images/sliderbuild10.jpg" alt="Image showing the Build Plate with a motor mounted on the back." />
  </p>
  
  <p spaces-before="0">
    --- /task ---
  </p>

<h3 spaces-before="0">
  Test the sliding indicator
</h3>

<p spaces-before="0">
  To program your sliding indicator, you can reuse some of the code written in the <a href="https://projects.raspberrypi.org/en/projects/lego-plotter">LEGO® Data plotter</a> project, as they use the same mechanism.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Connect the motor of your slider to port A on your Build HAT.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  You will use the BuildHAT Python library, so make sure it is installed:
</p>

<p spaces-before="0">
  --- collapse ---
</p>
<hr />
<h2 spaces-before="0">
  title: Install the BuildHAT Python library
</h2>

<p spaces-before="0">
  Open a terminal window on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.
</p>

<p spaces-before="0">
  At the prompt type: <code>pip3 install buildhat</code>
</p>

<p spaces-before="0">
  Press <kbd>Enter</kbd> and wait for the "installation completed" message.
</p>

<p spaces-before="0">
  --- /collapse ---
</p>

<p spaces-before="0">
  --- /task ---
</p>

<h3 spaces-before="0">
  Create the scale for your sliding indicator
</h3>

<p spaces-before="0">
  Now you know it works, you will need to create a scale for the sliding indicator, so you know what it means.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Get a piece of card about as long as your toothed bar. Stick it next to the sliding indicator, under the pointer. Have a marker or pencil ready.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Open <strong x-id="1">Thonny</strong> on your Raspberry Pi from the <strong x-id="1">Programming menu</strong>.
</p>

<p spaces-before="0">
  In the <strong x-id="1">Shell</strong> (the window at the bottom), next to the three arrows, type: <code>from buildhat import Motor</code> and press <kbd>Enter</kbd>. You should see a new line appear with three more arrows.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Now type: <code>motor = = Motor('A')</code> and press <kbd>Enter</kbd>. --- /task ---
</p>

<p spaces-before="0">
  Now you've set up your slider motor to run, you should send it to the maximum and minimum readings to see how far it can travel — then mark those places on the card.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Type: <code>motor.run_to_position(-180, 100)</code> and press <kbd>Enter</kbd>. Mark the card at the place the arrow indicates. This is your minimum possible readout.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Type: <code>motor.run_to_position(180, 100, direction=clockwise)</code> and press <kbd>Enter</kbd>. Mark the card at the place the arrow indicates. This is your maximum possible readout.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  You now know where your minumum and maximum possible readings are. Once you link the slider to some data, you will be able to create an accurate scale.
</p>

<h3 spaces-before="0">
  Program your sliding indicator to show live data
</h3>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Enter the following code in a blank tab:
</p>

<p spaces-before="0">
  --- code ---
</p>
<hr />

<p spaces-before="0">
  language: python filename: slider_test.py line_numbers: true line_number_start: 1
</p>
<h2 spaces-before="0">
  line_highlights:
</h2>

<p spaces-before="0">
  from buildhat import Motor from time import sleep from random import randint
</p>

<p spaces-before="0">
  motor_slider = Motor('A')
</p>

<p spaces-before="0">
  motor_slider.run_to_position(0,100)
</p>

<p spaces-before="0">
  while True: current_angle = motor_slider.get_aposition() new_angle = randint(-175, 175) print(sensor_data) if new_angle > current_angle: motor_slider.run_to_position(new_angle, 100, direction="clockwise") print('Turning CW') elif new_angle < current_angle: motor_slider.run_to_position(new_angle, 100, direction="anticlockwise") print('Turning ACW') sleep(0.1)
</p>

<p spaces-before="0">
  --- /code ---
</p>

<p spaces-before="0">
  Save your work as <code>slider_test.py</code> and click <strong x-id="1">Run</strong>. You should see your slider move up and down (or back and forth!)
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- save ---
</p>
