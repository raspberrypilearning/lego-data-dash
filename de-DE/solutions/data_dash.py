from buildhat import Motor
from buildhat import Motor
from datetime import datetime, timedelta
import requests

no2_motor = Motor('A')            # einrichten des Motors für die Linearanzeige
no2_motor.run_to_position(0,100)  # Linearanzeige zurücksetzen
pm25_motor = Motor('B')           # einrichten des Motors für das Zeigerinstrument
pm25_motor.run_to_position(0,100) # Zeigerinstrument zurücksetzen

no2_min_wert = 0          # der niedrigste NO2-Wert, den du erwartest  (hoffentlich ca. 0)
no2_max_wert = 60          # der höchste NO2-Wert, den du erwartest 
no2_min_winkel = 175       # minimale Motorposition
no2_max_winkel = -175      # maximale Motorposition


pm25_min_wert = 0          # der niedrigste PM2.5-Wert, den du erwartest  (hoffentlich ca. 0)
pm25_max_wert = 100        # der höchste PM2.5-Wert, den du erwartest 
pm25_min_winkel = 175      # minimale Motorposition
pm25_max_winkel = -175     # maximale Motorposition

basis_url = 'https://docs.openaq.org/v2/measurements'

nutzlast = {                    # erstelle ein dictionary für die API-Abfrage
    'date_from':'',
    'date_to':'',
    'location_id':'2480',       # das sollte die ID-Nummer des Ortes sein, die du früher aufgeschrieben hast
    'order_by':'datetime',
    'sort':'asc',
    'has_geo':'true',
    'limit':'100',
    'offset':'0',
}

verschmutzung = {              # erstelle ein dictionary für die Verschmutzungs-Messwerte
    'no2' : 0,
    'pm25': 0,
    }

def luft_messen():
    jetzt = datetime.now()           # holt die aktuelle Zeit
    delta = datetime.now() - timedelta(days=1)         # erzeugt eine Zeitdifferenz von einem Tag
    
    nutzlast['date_from'] = f'{delta:%Y-%m-%d}T{delta:%H:%M:%S}+00:00'  # fügt das Datum und die Zeit in das obige dictionary ein
    nutzlast['date_to'] = f'{jetzt:%Y-%m-%d}T{jetzt:%H:%M:%S}+00:00'
    
    antwort = requests.get(basis_url, params=nutzlast)          # fragt die Datenbank mittels des API ab
    
    if antwort.status_code != 200:          # prüfe, ob das API erreicht wurde
        print('Keine Antwort vom Server')
        return
    
    daten = antwort.json()
        
    for messwert in daten['results']:
        if messwert['parameter'] == 'no2':       #This will depend upon what pollutant you are measuring
            verschmutzung['no2'] = messwert['value']
        if messwert['parameter'] == 'pm25':      #This will depend upon what pollutant you are measuring
            verschmutzung['pm25'] = messwert['value']

    ergebnis_ausgabe()   
    sleep(1)

def umwandlung(min_wert, max_wert, min_winkel, max_winkel, sensor_wert):      # Funktion erstellen
    werte_bereich = (max_wert - min_wert)               # bestimme, wie groß dein Wertebereich ist
    motor_bereich = (max_winkel - min_winkel)             #  berechne, wie groß dein Motorbereich ist
    gewandelt = (((sensor_wert - min_wert) * motor_bereich) / werte_bereich) + min_winkel     # strecke den Wertebereich über den Motorbereich
    return int(gewandelt)                                           # gib eine Zahl zurück, die den Wert als Winkel auf dem Motor anzeigt
   
def ergebnis_ausgabe():
    print(f'NO2 = {verschmutzung['no2']}')
    no2_winkel_jetzt = no2_motor.get_aposition()
    no2_sensor_daten = int(verschmutzung['no2'])
    no2_winkel_neu = umwandlung(no2_min_wert, no2_max_wert, no2_min_winkel, no2_max_winkel, no2_sensor_daten)
    if no2_winkel_neu > no2_winkel_jetzt:
        no2_motor.run_to_position(no2_winkel_neu, 100, direction='anticlockwise')
    elif no2_winkel_neu < no2_winkel_jetzt:
        no2_motor.run_to_position(no2_winkel_neu, 100, direction='clockwise')
    sleep(0.1)
    pm25_sensor_daten = int(verschmutzung['pm25'])
    print(f"PM2.5 = {verschmutzung['pm25']}")
    pm25_winkel_jetzt = pm25_motor.get_aposition()
    pm25_winkel_neu = umwandlung(pm25_min_wert, pm25_max_wert, pm25_min_winkel, pm25_max_winkel, pm25_sensor_daten)
    pm25_motor.run_to_position(pm25_winkel_neu, 100)

while True:
    luft_messen()
    sleep(3600)              # ich warte jetzt eine Stunde vor dem nächsten Abruf der Daten (zum Testen kannst du diese Zeit kleiner machen)