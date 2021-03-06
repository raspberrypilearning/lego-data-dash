## Mache eine LEGO® Anzeige

Eine andere Möglichkeit, Daten schnell anzuzeigen, ist die Verwendung von **Zifferblättern**, auch bekannt als **Anzeigen**. Du hast sie definitiv schon einmal gesehen; Sie sind normalerweise rund oder halbkreisförmig und haben zwei sichtbare Hauptteile:

+ Das Zifferblatt, auf dem die Skala abgebildet ist
+ Die Nadel, die sich entlang der Skala bewegt, um den Messwert anzuzeigen

![Animiertes Bild mit sich bewegendem Zeiger.](https://media.giphy.com/media/uozBSFuz99USA/giphy.gif)

Ein Messgerät oder ein Zifferblatt ist die einfachste Art der Datenanzeige, die du mit LEGO® erstellen kannst, da du nur ein Zifferblatt und eine Nadel benötigst. Da die Nadel und das Zifferblatt direkt mit deinem Motor verbunden sind, ist der Aufbau sehr einfach:

--- task ---

Bevor du den Motor an der Rückseite des Messgeräts auf der Achse anbringst, stelle sicher, dass er „genullt“ ist, indem du die beiden Lutschersymbole an der Kante des Motors ausrichtest:

![Bild zeigt den Motor "genullt" mit ausgerichteten Symbolen.](images/aligned_symbols.jpg)

--- /task ---

### Erstelle eine Skala

Um das Messgerät fertig zu bauen, musst du eine Skala aus Papier, Karton oder anderem Künstlerzubehör erstellen. Die Mechanik und das Programm sind genau gleich, aber du musst dir jetzt überlegen, wie dein Messgerät aussehen soll.

 --- task ---

 **Wähle** welche Art von Anzeige du machen möchtest.

 Es gibt zwei einfache Typen, die du mit LEGO® erstellen kannst:

+ Ein Messgerät, bei dem sich die Nadel dreht, um einen Punkt auf der Skala anzuzeigen: ![Ein Bild, das ein Messgerät mit einem Zeiger und einer Skala zeigt.](images/dial2.gif)

+ Eine Anzeige, bei der sich das gesamte Zifferblatt dreht, um einen Punkt oben mit einem stationären Indikator anzuzeigen: ![Ein Bild, das ein Messgerät mit einer beweglichen Skala zeigt.](images/dial1.gif)

--- /task ---

--- task ---

Zeichne auf einem leeren Blatt Papier einen schönen Kreis in der Größe, die dein Messgerät haben soll. Markiere die Mitte und schneide sie mit einer Schere aus.

--- /task --- 

--- task ---

Teile den Kreis in gleich große Segmente (eines für jeden Messwert), indem du Linien durch die Mitte ziehst, oder zeichne deine Skala um den Rand herum.

--- /task ---

--- task ---

Zeichne Symbole oder schreibe in jedes Segment, was es anzeigt.

--- /task ---

Sobald du mit der Erstellung deines Messgeräts fertig bist, musst du es an deinem Armaturenbrett montieren.

--- collapse ---
---
title: Wenn du eine Anzeige mit Zeiger erstellst
---

Um dein Zeigerinstrument fertig zu stellen:

--- task ---

Schiebe das Zifferblatt über deine Achse und kleben sie mit Blu Tack oder Klebeband auf das Armaturenbrett dahinter. Achte darauf, dass es beim Drehen der Achse nicht rutscht. ![Bild, das eine LEGO® Achse zeigt, die durch das Zifferblatt eines Messgeräts ragt.](images/needle-gauge1.jpg)

--- /task ---

--- task ---

Stecke ein 90-Grad-Winkelstück auf die Achse und stecke eine weitere Achse hinein. Stelle sicher, dass sie lang genug ist um deine Skala zu erreichen und die Messwerte deutlich anzuzeigen.

![Bild, das die LEGO®-Achse zeigt, die durch das Zifferblatt des Messgeräts ragt und, mit der ein 90°-Winkelstück und eine senkrechte Achse verbunden sind.](images/needle-gauge2.jpg)

Es hilft später, wenn deine Achse beim Montieren gerade nach oben zeigt (und dein Motor auf Null gestellt ist), da dies die Berechnung der für die Anzeige erforderlichen Drehung erleichtert.

--- /task ---

--- /collapse ---

--- collapse ---
---
title: Wenn du ein sich drehendes Zifferblatt machst
---

Um deine Drehskala fertig zu stellen:

--- task ---

Montiere ein einzelnes Zahnrad als Abstandshalter hinter deinem Zifferblatt, damit es nicht an deinem Armaturenbrett hängen bleibt. Verwende etwas Blu Tack, um das Zifferblatt an dieses Zahnrad zu kleben. Wenn du eine inkrementelle Skala um das Zifferblatt herum erstellt hast, montiere es mit der Mitte der Skala oben (bei den 'genullten' Lutschersymbolen) und den minimalen und maximalen Werten unten.

![Bild, das ein schwarzes LEGO® Zahnrad zeigt, das auf einer Achse mit etwas Tack montiert ist.](images/dial-gauge1.jpg)

![Bild, das die Anzeige zeigt, die auf einem schwarzen LEGO® Zahnrad montiert ist.](images/dial-gauge2.jpg)

--- /task ---

--- /collapse ---

### Teste dein Messgerät

--- task ---

Verbinde den Motor deiner Anzeige mit Port A deines Build HAT.

--- /task ---

--- task ---

Du benötigst die BuildHAT Python-Bibliothek, stelle also sicher, dass sie installiert ist:

--- collapse ---
---
title: Installation der buildhat Python-Bibliothek
---

Öffne ein Terminalfenster auf deinem Raspberry Pi, indem du <kbd>Strg</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> drückst.

Gib an der Eingabeaufforderung `pip3 install buildhat` ein

Drücke <kbd>Enter</kbd> und warte auf die Meldung "Installation abgeschlossen".

--- /collapse ---

--- /task ---

--- task ---

Öffne **Thonny** uf deinem Raspberry Pi aus dem Menü **Entwicklung**.

Gib den folgenden Code in eine leere Registerkarte ein:

--- code ---
---
language: python 
filename: gauge_test.py 
line_numbers: true 
line_number_start: 1
line_highlights:
---
from buildhat import Motor 
from time import sleep 
from random import randint

motor_zeiger = Motor('A')

motor_zeiger.run_to_position(0,100)

while True:
    winkel = randint(-180, 180)
    motor_zeiger.run_to_position(winkel, 100)
    sleep(0.3)

--- /code ---

Speichere deine Arbeit als `gauge_test.py` und klicke auf **Run**. Du wirst sehen, wie sich deine Anzeige zu bewegen beginnt!

--- /task ---
