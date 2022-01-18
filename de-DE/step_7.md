## Zeige Verschmutzungsdaten mit deiner Instrumententafel an

Im Moment verwenden deine Anzeigen zufällige ganze Zahlen zwischen -175 und 175; diese Zahlen werden verwendet, weil sie die Bewegungsgrenzen des Motors in jede Richtung darstellen. (Wir gehen nicht auf 180, da dies zu Problemen beim Bewegen um eine volle Umdrehung führen kann.) Die von deiner API eingehenden Daten haben nicht denselben Bereich, daher musst du sie an die Motoren anpassen.

**Kalibrieren** der Anzeigen bedeutet, dass die maximal und minimal möglichen Datenwerte von deiner API auf Werte zwischen -175° und 175° auf deinem Motor abgebildet werden. Der höchstmögliche Messwert liegt bei -175°, während der niedrigste Messwert bei 175° liegt. (Weil du die Motoren umgekehrt montiert hast!)

In unserem Beispiel zeigen wir den **Feinstaub (PM2,5)** auf dem Messgerät an, während die Linearanzeige den Stickstoffdioxidgehalt (NO2) anzeigt. Der Begriff **Feinstaub**oder Feinstaub 2,5 (PM2,5) bezieht sich auf winzige Partikel oder Tröpfchen in der Luft, die zweieinhalb Mikrometer (oder weniger) groß sind. Die von PM2,5 gemessenen Partikel sind die Hauptbestandteile von Rauch und Smog und erschweren die Sicht.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Wie Zoll, Meter und Millimeter ist ein <span style="color: #0faeb0">Mikron</span> eine Maßeinheit für Entfernung. Ein Zentimeter entspricht 10.000 Mikrometer. Der Durchmesser der größeren Partikel im Größenbereich PM2,5 wäre etwa dreißigmal kleiner als die Dicke eines menschlichen Haares. Diese Teilchen sind so klein, dass mehrere Tausend von ihnen auf den Punkt am Ende dieses Satzes passen.</p>

In unserem Beispiel zeigt die Linearanzeige den Stickstoffdioxidgehalt (NO2) an. Der maximal mögliche Messwert auf deiner Linearanzeige hängt vom gewählten Standort ab, da städtische Gebiete immer höhere Messwerte aufweisen als ländliche. Der minimal mögliche Messwert ist natürlich 0, aber du solltest den normalen Bereich für das, was du misst, berücksichtigen und dazu ein wenig hinzufügen.

Um den wahrscheinlich höchsten Messwert zu ermitteln, kannst du die historischen Daten von deinem ausgewählten Standort auf der zuvor geöffneten Webseite anzeigen:

![Bild, das historische NO2-Daten von Sandy am Straßenrand, grafisch dargestellt, zeigt.](images/historicaldata_no2.jpg)

Hier kannst du sehen, dass, obwohl es einige große Ausreißer gibt, etwa 60 µg/m³ mehr als genug als maximaler Wert für die meisten Messwerte der Sandy Roadside-Luftqualitätsstation sein sollten. (Wenn du deine Skala einfach von 0 bis 000 machen möchtest, kannst du das auch tun – mache einfach `max_wert = 100`.)

--- task ---

Verbinde deinen Linearanzeigemotor mit Port A des Build HAT. Schließe deinen Anzeigermotor an Port B an.

--- /task ---

--- task ---

Gib in einem neuen Thonny-Fenster Folgendes ein:

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

no2_motor = Motor('A')           #einrichten des Motors für die Linearanzeige 
no2_motor.run_to_position(0,100) #Linearanzeige zurücksetzen 
pm25_motor = Motor('B')           #einrichten des Motors für das Zeigerinstrument 
pm25_motor.run_to_position(0,100) #Zeigerinstrument zurücksetzen

no2_min_wert = 0  der niedrigste NO2-Wert, den du erwartest  (hoffentlich ca. 0) 
no2_max_wert = 0  der höchste NO2-Wert, den du erwartest 
no2_min_winkel = 175       # minimale Motorposition 
no2_max_winkel = -175      # maximale Motorposition

pm25_min_wert = 0 #  der niedrigste PM2.5-Wert, den du erwartest  (hoffentlich ca. 0) 
pm25_max_wert = 100 #  der höchste PM2.5-Wert, den du erwartest 
pm25_min_winkel = 175 # minimale Motorposition 
pm25_max_winkel = -175 # maximale Motorposition

--- /code ---

--- /task ---

Da du jetzt die erforderlichen Bibliotheken importiert und Ihre Messdetails eingerichtet hast, kannst du deine Abfrage an die API einrichten, indem du einige **dictionaries** mit von dir verwendeten Begriffe erstellst.

--- task ---

Füge diesen Code in deinem Thonny-Fenster am Ende deines Skripts hinzu:

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 21
line_highlights:
---
basis_url = 'https://docs.openaq.org/v2/measurements'

nutzlast = {                    # erstelle ein dictionary für die API-Abfrage 
    'date_from':'', 
    'date_to':'', 
    'location_id':'2480',      # das sollte die ID-Nummer des Ortes sein, die du früher aufgeschrieben hastr 
    'order_by':'datetime', 
    'sort':'asc', 
    'has_geo':'true', 
    'limit':'100', 
    'offset':'0', 
    }

verschmutzung = {                  # erstelle ein dictionary für die Verschmutzungs-Messwerte 
    'no2' : 0,                 # hier bereiten wir NO2 und PM2.5 vor - könnte bei dir anders sein! 
    'pm25': 0, 
    }

--- /code ---

--- /task ---

Die nächste Funktion, die du schreiben musst, fragt die API mit den von dir eingerichteten Parametern ab.

--- task ---

Füge am Ende deines Skripts diesen Code hinzu:

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 39
line_highlights:
---
def luft_messen(): 
    jetzt = datetime.now()           # holt die aktuelle Zeit 
    delta = datetime.now() - timedelta(days=1)         # erzeugt eine Zeitdifferenz von einem Tag

    nutzlast['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00'  # fügt das Datum und die Zeit in das obige directory 
    nutzlast['date_to'] = f'{jetzt:%Y-%m-%d}T{jetzt:%H:%M:%S}+00:00'
    
    antwort = requests.get(basis_url, params=nutzlast)          # fragt die Datenbank mittels der API ab
    
    if antwort.status_code != 200:          # prüfe, ob die API erreicht wurde
        print('Keine Antwort vom Server')
        return
    
    daten = antwort.json()
    
    for messwert in daten['results']:
        if messwert['parameter'] == 'no2':       # das hängt vom gemessenen Schadstoff ab
            verschmutzung['no2'] = messwert['value']
            print(verschmutzung['no2'])
        if messwert['parameter'] == 'pm25':      # das hängt vom gemessenen Schadstoff ab
            verschmutzung['pm25'] = messwert['value']
            print(verschmutzung['pm25'])
    
    output_results()   
    sleep(1)

 --- /code ---

 --- /task ---

Der nächste Teil, den du schreiben wirst, wird einige clevere Berechnungen durchführen, um deinen Datenbereich über den gesamten Motorbereich abzubilden. (Es ist im Grunde die gleiche Funktion, die im [LEGO Data Plotterprojekt](https://learning-admin.raspberrypi.org/de-DE/projects/lego-plotter/6) verwendet wird.)

--- task ---

Füge diese Funktion unter deinem vorhandenen Code hinzu:

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 65
line_highlights:
---
def umwandlung(min_wert, max_wert, min_winkel, max_winkel, sensor_wert): # erstelle Funktion 
    werte_bereich = (max_wert - min_wert) # bestimme, wie groß dein Wertebereich ist 
    motor_bereich = (max_winkel - min_winkelangle) # berechne, wie groß dein Motorbereich ist 
    gewandelt = (((sensor_wert - min_wert) * motor_bereich) / werte_bereich) + min_winkel # strecke deinen Wertebereich über deinen Motorbereich return int(gewandelt) # gib eine Zahl zurück, die den Wert als Winkel auf dem Motor anzeigt

--- /code ---

--- /task ---

Nachdem deine Funktionen erstellt wurden, musst du eine Schleife erstellen, die Folgendes bewirkt:

+ Den Winkel, in dem sich der Motor derzeit befindet, herausfinden
+ Die Schadstoffdaten mit der Funktion `umwandlung` in Winkelpositionen für deine Motoren umrechnen
+ Zum neuen Winkel gehen, um den Messwert anzuzeigen

--- task ---

Füge am Ende deines Skripts in einer neuen Zeile den folgenden Code hinzu:

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 73
line_highlights:
---
def ergebnis_ausgabe(): 
    print(f'NO2 = {verschmutzung['no2']}') 
    no2_winkel_jetzt = no2_motor.get_aposition() 
    no2_sensor_daten = int(verschmutzung['no2']) 
    no2_winkel_neu = umwandlung(no2_min_wert, no2_max_wert, no2_min_winkel, no2_max_winkel, no2_sensor_daten) 
    print(no2_winkel_neu) 
    if no2_winkel_neu > no2_winkel_jetzt: 
        no2_motor.run_to_position(no2_winkel_neu, 100, direction='anticlockwise') 
        print('im Uhrzeigersinn') 
    elif no2_winkel_neu < no2_winkel_jetzt: 
        no2_motor.run_to_position(no2_winkel_neu, 100, direction='clockwise') 
        print('gegen den Uhrzeigersinn') 
        sleep(0.1) 
        pm25_sensor_daten = int(verschmutzung['pm25']) 
        print(f"PM2.5 = {verschmutzung['pm25']}") 
        pm25_winkel_jetzt = pm25_motor.get_aposition() 
        print(pm25_winkel_jetzt) 
        pm25_winkel_neu = umwandlung(pm25_min_wert, pm25_max_wert, pm25_min_winkel, pm25_max_winkel, pm25_sensor_daten) 
        pm25_motor.run_to_position(pm25_winkel_neu, 100)

--- /code ---

--- /task ---

Der letzte Teil deines Codes muss jetzt deine Funktion `luft_messen()` aufrufen, um alles zum Laufen zu bringen, und die API regelmäßig auf aktualisierte Daten überprüfen.

--- task ---

Gib am Ende deines Skripts, in einer neuen Zeile (stelle sicher, dass sie nicht eingerückt ist) folgendes ein:

--- code ---
---
language: python 
filename: data_dash.py 
line_numbers: true 
line_number_start: 93
line_highlights:
---
while True: 
    luft_messen() 
    sleep(3600)   # warte eine Stunde vor dem nächsten Abruf der Daten(zum Testen kannst du diese Zeit kleiner machen)
--- /code ---

--- /task ---

--- task ---

Speichere deine Arbeit als `data_test.py` und klicke auf **Run**. Der Linearanzeiger sollte sich bewegen, um den aktuellen NO2-Messwert der gewählten OpenAQ-Station anzuzeigen, und dein Zeigermessgerät sollte sich bewegen, um den PM2,5-Messwert anzuzeigen. Gut gemacht!

--- /task ---

--- save ---
