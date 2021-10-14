## Access the OpenAQ API

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">API stands for <span style="color: #0faeb0">**Application Programming Interface**</span>; this is software that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.</p> 

Whenever you use an app on your phone, the app connects to the internet and sends data about what you want to know to a server. The server then finds and retrieves the data you want, interprets it, and sends it back to your phone. The app then takes the data that has been returned and presents you with the information you wanted in a readable way. This is what an API is: a way to control other machines over the internet — all of this happens through the **API**.

The cool part is, you can write your own apps that investigate online databases of information and return the desired data to your LEGO® dashboard instead of a phone — you'll use your Raspberry Pi as the brains to get that data, then display it on your hand-made, custom LEGO indicators!

To do that, you'll need to decide on a few things: you'll need to pick the location where you will find out about the air quality — you can choose anywhere in the world! — and you'll need to decide which markers of air quality you want to represent. 

### OpenAQ — the open-source air quality database

In your example dashboard, you're going to be using the API for [**OpenAQ**](https://openaq.org/#/){:target="_blank"}, an open-source, global air quality data project. OpenAQ allows you to look at lots of different air pollution data from all over the globe, collected by thousands of measurement stations around the world. 

If you're already a wizard with APIs, you can use any data you like to represent on your dashboard. If you want to follow along with us and use OpenAQ for your first try, you'll need to find out which measurement station you want to investigate and which measurements you are able to view.

--- task ---

**Navigate** to the OpenAQ map by [clicking here](https://openaq.org/#/map){:target="_blank"}. A webpage showing a world map covered in dots should appear.

--- /task --- 

--- task ---

**Decide** where in the world you would like to gather data about air quality from. This could be the area near where you live, somewhere that interests you, or somewhere that you think might have interesting data.

--- /task --- 

As our headquarters are in Cambridge, in the United Kingdom, we will use that as the example here.  

There are many different measurements taken by air quality monitoring stations. The OpenAQ database has information on the following types of air pollution:

 + PM2.5 and PM10 (particulate matter): microscopic particles floating in the air (smoke, smog)
 + NO2 (nitrogen dioxide): causes ozone creation, causes asthma in children
 + CO (carbon monoxide): deadly to humans, side effect of burning fossil fuels
 + SO2 (sulfur dioxide): smells bad, can cause breathing problems, creates acid rain, side effect of industrial treatments
 + O3 (ozone): created when NO2 reacts to sunlight, causes smog, harmful to plants
 + BC (black carbon): not measured in many places (US and Poland), caused by inefficient fuel burning, adds to global warming, dangerous to humans

--- task ---

**Decide** upon what kind of air pollution you are most interested in measuring. You can choose different options from the pulldown menu near the coloured scale on the left of the screen.
![Image showing the pulldown menu in the OpenAQ map.](images/mapscale.jpg)

**Note:** Round markers represent more substantial air quality stations which are likely to measure more varied pollutants. 

--- /task ---

--- task ---

**Zoom in** to your chosen area on the map, and find the dot closest to the place you would like to measure. Click on that nearest dot to see the location details. In the pop-up that appears, click the button that says **View Location**.  
![Image showing a world map zoomed in on the eastern UK.](images/mapscroll.gif)

--- /task ---

--- task ---

When the new webpage loads showing the details of the measurements taken at the location, **make a note** of the number in the URL of the new page. This is the OpenAQ identification number for your chosen air quality station. (In this example, it is the Sandy Roadside measurement station, with ID number **2480**.)
![Image showing the OpenAQ URL with a number for the location ID.](images/openaq_id.jpg)

--- /task ---

--- task ---

On the location page, you will see the different types of pollutants measured at that location. **Choose** two from the list that you would like to represent on your data dashboard.
![Image showing a pollutant list from a location on the OpenAQ map.](images/openaq_msmt.jpg)
This measurement station near Sandy can show NO2, PM10, and PM2.5 — so we'll use NO2 and PM2.5 in the example.  

--- /task ---

