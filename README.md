# 🌱 Rasenpflege leicht gemacht!

## 📌 Kurzfassung

In unserem Projekt erweitern wir einen Rasenmähroboter, damit dieser nicht nur den Rasen selbstständig mäht, sondern zusätzlich auch die Bewässerung bzw. Düngung des Gartens übernehmen kann.

Dadurch soll weniger manueller Aufwand entstehen. Der Roboter soll mithilfe verschiedener Sensoren die Umgebung erkennen. Dazu ist der Aufbau des Systems so geplant, dass die Feuchtigkeit des Rasens gemessen werden kann. Anschließend soll der Rasen bei Bedarf versorgt und gepflegt werden, sodass ein gesunder Rasen entsteht. Unser Fokus liegt darauf, Wasser und Dünger sparsam einzusetzen und das System einfach zu bedienen.

---

## 📋 Projekt-Plan & Aufgaben

<img width="1447" height="1087" alt="Intelligentes Rasenpflegesystem – Übersicht" src="https://github.com/user-attachments/assets/1184a4f6-4810-4271-8ab1-f6150bfe28aa" />

### 💡 Was der Rasenmäher machen muss

- Selbstständiges Mähen des Rasens
- Automatische ~~Bewässerung~~ → **Düngung** des Gartens
- Feuchtigkeitssensoren erkennen, ob der Boden Wasser benötigt
- Integrierter ~~Wassertank für die Bewässerung~~ → **Tank mit Dünger** (kommt erst später dazu)
- Optische Untersuchung des Rasens mithilfe von NIR-Sensoren und einer Kamera
- Messwerte erfassen und zur weiteren Auswertung übertragen

> **Hinweis:**
>
> - Automatisches Nachfüllen des Tanks ist noch unklar.
> - Die automatische Düngung ist ein späteres Entwicklungsziel.
> - Die gezielte Bewässerung soll langfristig über einen externen Wassersprinkler erfolgen.

### 🛠️ Was wir noch machen wollen

- ESP32 soll regelmäßig, zunächst etwa jede Sekunde, Daten schicken.
- Die Kamera des ESP32-S3-CAM soll Bilder des Rasens aufnehmen.
- Der Raspberry Pi soll eine Live-Tabelle und Diagramme in einer Web-App anzeigen.
- Wir prüfen, ob wir auf den **Raspberry Pi Zero W** umsteigen können.https://docs.freenove.com/projects/fnk0084/en/latest/fnk0084/codes/Python/30_Camera_Web_Server.html?utm_source=chatgpt.com
- Die Verbindung zwischen ESP32 und Raspberry Pi soll stabil laufen.
- Die aufgenommenen Bilder und Messwerte sollen später gemeinsam ausgewertet werden.
- Später vielleicht eine App daraus machen.

### 💻 Programmierung & Entwicklung

- Der ESP32 wird programmiert, um Sensoren auszulesen, die Kamera anzusteuern und Daten zu übertragen.
- Der Raspberry Pi dient als zentrale Plattform für die Datensammlung und Web-App.
- Über **SSH** können wir den Raspberry Pi ohne eigenen Bildschirm bedienen.
- Mit `esptool` können wir den ESP32-S3 über USB erkennen und Firmware übertragen.
- Für die Entwicklung können wir **VS Code Remote SSH** verwenden.
- Langfristig soll das System modular aufgebaut werden, damit weitere Sensoren und Funktionen ergänzt werden können.

### 🤖 Kamera & zukünftige KI-Auswertung

Die Kamera soll zusätzliche Informationen über den Zustand des Rasens liefern. In einem späteren Schritt möchten wir untersuchen, ob sich mithilfe einer Bildauswertung trockene, gesunde oder auffällige Rasenbereiche erkennen lassen.

Eine KI könnte zukünftig helfen, Bilder und Messwerte auszuwerten. Zunächst wollen wir jedoch eine einfache, nachvollziehbare Datenauswertung entwickeln und testen.

---

## 🚀 Zukunftskonzept: Intelligente Rasenpflege

Unser System geht deutlich über die ursprüngliche Idee hinaus. Der Mähroboter, eine externe Station und ein externer Wassersprinkler sollen zusammenarbeiten:

- **Exakte Feuchtigkeitsmessung:** Über geeignete Sensoren und eine externe Station, die frei auf dem Rasen platziert werden kann.
- **Präzisionsbewässerung:** Ein Wassersprinkler übernimmt die Bewässerung und bringt nur dort Wasser aus, wo es tatsächlich notwendig ist.
- **Optische Rasenanalyse:** Eine Kamera und ein NIR-Sensor erfassen zusätzliche Informationen über den Rasen.
- **Intelligente Datenauswertung:** Messwerte und Bilddaten werden zusammengeführt, um den Zustand des Rasens besser einschätzen zu können.

### Was die externe Station leisten soll

- **Zentrale Datensammlung:** Alle Feuchtigkeitswerte, GPS-Positionen und Statusmeldungen laufen hier zusammen.
- **Live-Web-App:** Übersichtliche Anzeige aller Werte, Diagramme, Feuchtigkeitskarten, Warnungen und später des Wasserverbrauchs.
- **Steuerung des Wassersprinklers:** Die Station entscheidet anhand der erfassten Daten, welche Stelle bewässert werden soll – nicht der Sprinkler selbst.
- **Automatische Feuchtigkeitskarte:** Aus Positionsdaten und Feuchtigkeitsmessungen entsteht eine Karte, die trockene Bereiche sichtbar macht.
- **Spätere KI-Auswertung:** Bild- und Sensordaten sollen kombiniert werden, um den Zustand des Rasens genauer einzuschätzen.

## Software: Optische Feuchtemessung mit dem AS7263

### Ziel

Das Programm untersucht, ob sich die Feuchtigkeit von Gras mithilfe optischer Messungen erkennen lässt. Dafür verwenden wir den **AS7263-NIR-Sensor**, der sechs Spektralkanäle im nahen Infrarot- und Rotbereich auswertet.

Zusätzlich misst ein LDR die Helligkeit. Abhängig vom gemessenen Lichtwert wird eine externe Beleuchtung gesteuert. Dadurch sollen die Messbedingungen möglichst reproduzierbar werden.

### Funktionsweise

1. Der ESP32 liest den Helligkeitswert des LDR aus.
2. Anhand des Wertes wird die Beleuchtung ausgeschaltet, reduziert oder auf volle Leistung gestellt.
3. Der AS7263 erfasst die optischen Messwerte.
4. Das Programm liest insbesondere die Kanäle bei 760 nm, 810 nm und 860 nm aus.
5. Aus den Messwerten bei 810 nm und 860 nm wird ein Verhältnis berechnet:

   **Feuchte-Index = Messwert bei 810 nm / Messwert bei 860 nm**

Dieser Index ist zunächst nur ein experimenteller Kennwert. Er ist kein direkt gemessener Feuchteprozentsatz und muss durch Vergleichsmessungen mit unterschiedlich feuchtem Gras überprüft werden.

### Bisherige Probleme

- **Sehr niedrige Messwerte:** Bei reduzierter Beleuchtung wurden teilweise Werte zwischen 0 und 3 beobachtet. Solche kleinen Werte können stark durch Rauschen und Umgebungslicht beeinflusst werden.
- **Messwert von 0 bei 860 nm:** Ist der Nenner null, kann kein gültiger Index berechnet werden. Das Programm muss diesen Fall erkennen.
- **Unterschiedliche Beleuchtung:** Änderungen der Beleuchtung können die Messwerte verändern, ohne dass sich die Grasfeuchtigkeit geändert hat.
- **Bewegung des Mähroboters:** Abstand, Neigung und Vibrationen können die Messung beeinflussen.
- **Noch keine Kalibrierung:** Bisherige Messwerte allein beweisen noch keinen Zusammenhang zwischen dem Index und der tatsächlichen Grasfeuchtigkeit.

### Nächste Schritte

Für belastbare Ergebnisse sollen trockene und feuchte Grasflächen mehrfach unter möglichst gleichen Bedingungen gemessen werden. Abstand, Beleuchtung und Messposition sollen konstant bleiben. Die Ergebnisse müssen mit einer unabhängigen Referenzmessung verglichen werden.

Langfristig soll die Messung auf einem fahrenden Rasenmähroboter eingesetzt werden, damit unterschiedliche Bereiche einer Rasenfläche untersucht und auf einer Karte dargestellt werden können.

### Hardware und Bibliothek

- ESP32 mit MicroPython
- AS7263-NIR-Sensor über I²C
- LDR zur Erfassung der Helligkeit
- Externe, passend angesteuerte Beleuchtung
- MicroPython-Treiber: [AS726X_LoPy auf GitHub](https://github.com/jajberni/AS726X_LoPy)
- [Anleitung für den eps 32 cam](https://docs.freenove.com/projects/fnk0084/en/latest/fnk0084/codes/Python/30_Camera_Web_Server.html?utm_source=chatgpt.com)

**Hinweis:** Die Messung ist ein Forschungsprototyp. Eine zuverlässige Bestimmung der Grasfeuchtigkeit ist erst nach systematischen Tests und einer Kalibrierung möglich.


---
## 🔌 Stückliste (BOM) und Kostenübersicht

Die folgende Stückliste dokumentiert die Hardware unseres Projekts **„Rasenpflege leicht gemacht!“**. Die meisten Komponenten wurden bereits angeschafft. Allerdings sind noch nicht alle programmiert, kalibriert, getestet oder vollständig in das Gesamtsystem integriert.

Wir entwickeln das System schrittweise: Zuerst testen wir die einzelnen Sensoren und Steuerungen. Anschließend verbinden wir diese mit dem ESP32 und dem Raspberry Pi. Darauf aufbauend sollen die Kameraauswertung, die zentrale Datensammlung und später die gezielte Bewässerung umgesetzt werden.

### 📦 Hardware und Komponenten

| Bauteil | Anzahl | Verwendungszweck | Produktlink | Status |
| :--- | :---: | :--- | :--- | :--- |
| **ESP32-S3-CAM** | 1 | Kamera und Verarbeitung von Bilddaten | [Zum Shop](https://store.freenove.com/products/fnk0086) | Vorhanden; Kamera und Software werden getestet |
| **Raspberry Pi 3 B+** | 1 | Zentrale Datenerfassung und Server | [Zum Shop](https://pip.raspberrypi.com/categories/532) | In Verwendung; Systemintegration läuft |
| **Wasserpumpen** | 2 | Steuerung der Wasserzufuhr | [Zum Shop](https://www.amazon.de/s?k=12V+Wasserpumpe+Arduino) | Vorhanden; Steuerung getestet |
| **Funduino-Wasserstandssensoren** | 3 | Messung des Wasserstands im Tank | [Zum Shop](https://funduino.com/collections/fuellstandssensoren) | Vorhanden; Messwerte getestet |
| **Bodenfeuchtesensoren** | 2 | Messung der Bodenfeuchtigkeit | [Zum Shop](https://www.reichelt.de/de/de/shop/produkt/arduino_-_feuchtesensor_fuer_bodenfeuchte-282511) | Vorhanden; Kalibrierung und Tests laufen |
| **AS7263-NIR-Sensor** | 1 | Optische Messungen im nahinfraroten Bereich | [Zum Shop](https://www.antratek.de/spectral-sensor-breakout-as7263-nir) | Vorhanden; Kalibrierung und Auswertung laufen |
| **GARDENA smart SILENO max 800 m²** | 1 | Mobile Plattform für das Rasenpflegekonzept | [Zum Shop](https://www.gardena.com/de/produkte/rasenpflege/maehroboter/maehroboter-smart-sileno-max-800-m/970620803.html) | Vorhanden; Integration muss getestet werden |
| **Weitere ESP32-S3-Boards** | 2 | Zusätzliche Steuerungs- und Sensorversuche | [Zum Shop](https://www.antratek.de/thing-plus-esp32-s3) | Vorhanden; weitere Tests geplant |
| **BME280-Sensormodule** | 2 | Messung von Temperatur, Luftdruck und Luftfeuchtigkeit | [Zum Shop](https://www.roboter-bausatz.de/p/digital-bme280-temperatur-sensor-luftdruck-feuchtigkeit-i2c-5v-barometer-arduino) | Vorhanden; Einsatz je nach Teilprojekt |
| **Raspberry Pi Zero W** | 2 | Kompakte Recheneinheiten für mögliche Erweiterungen | [Zum Shop](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) | Vorhanden; Einsatz für Erweiterungen offen |
| **VL53L0X-Abstandssensoren** | 2 | Entfernungsmessungen | [Zur Info](https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x) | Vorhanden |
| **Rasensprinkler** | 1 | Gezielte Bewässerung ausgewählter Rasenbereiche | *Noch offen* | Geplant; Produkt noch nicht bestätigt |
| **ZED-F9P-15B-GPS-Modul** | Noch offen | Mögliche zukünftige Erweiterung zur Positionsbestimmung | [Zum Shop](https://www.digikey.de/de/products/detail/u-blox/ZED-F9P-15B/20838269) | Zukünftige Erweiterung; Anschaffung nicht bestätigt |
| **Micro-USB-Kabel für Raspberry Pi** | 1 | Stromversorgung oder Verbindung, abhängig vom Einsatz | [Zum Shop](https://www.reichelt.de/de/de/shop/produkt/raspberry_pi_-_kabel_micro-usb_m_auf_usb_typ_a_f_otg_10cm_-316284) | Verfügbarkeit prüfen |


### 🧪 Entwicklungsstatus

Für die Dokumentation unterscheiden wir zwischen dem Besitz einer Komponente und ihrer technischen Integration.

| Status | Bedeutung |
|---|---|
| **Vorhanden** | Die Komponente wurde bereits angeschafft. |
| **In Entwicklung** | Programmierung, Kalibrierung oder Funktionstests laufen noch. |
| **In Verwendung** | Die Komponente funktioniert bereits in einem Teil des Prototyps. |
| **Geplant** | Die Komponente oder Funktion ist für eine spätere Entwicklungsphase vorgesehen. |

Bereits erfolgreich umgesetzt wurden unter anderem die Pumpenansteuerung, das Auslesen des Wasserstandssensors sowie die WLAN-Kommunikation zwischen ESP32 und Raspberry Pi. Andere Komponenten müssen noch einzeln getestet und anschließend in das Gesamtsystem eingebunden werden.

### 💶 Kostenübersicht

Die Gesamtkosten sollen anhand der tatsächlichen Anschaffungspreise berechnet werden. Da noch nicht alle Kaufpreise dokumentiert sind, wird vorerst keine Gesamtsumme angegeben.

| Kostenposition | Berechnung | Betrag |
|---|---|---:|
| Bereits angeschaffte Hardware | Summe der tatsächlichen Kaufpreise | Noch zu ermitteln |
| Zusätzliche ESP32-S3-Boards | 2 × tatsächlicher Kaufpreis | Noch zu ermitteln |
| BME280-Sensormodule | 2 × tatsächlicher Kaufpreis | Noch zu ermitteln |
| VL53L0X-ToF-Sensoren | 2 × tatsächlicher Kaufpreis | Noch zu ermitteln |
| Raspberry Pi Zero W | Tatsächlicher Kaufpreis, sofern bekannt | Noch zu ermitteln |
| Externer Wassersprinkler | Falls noch anzuschaffen | Noch offen |
| GPS-Modul | Nur falls tatsächlich angeschafft oder bestellt | Noch offen |
| Kabel und weitere Bauteile | Tatsächliche Mengen und Kaufpreise | Noch zu ermitteln |
| **Gesamtkosten des Projekts** | **Summe der bestätigten Anschaffungskosten** | **Noch zu ermitteln** |

Die Kostenübersicht wird ergänzt, sobald die tatsächlichen Kaufpreise bekannt sind. Bereits vorhandene Komponenten werden dabei nicht automatisch als kostenlose Teile gewertet: Auch ihre ursprünglichen Anschaffungskosten gehören zu den Projektkosten. Geplante, noch nicht gekaufte Erweiterungen werden separat aufgeführt.
 
---
## 🔌 Verkabelung & Anschlüsse (Pinout)

Da das System modular aufgebaut ist und auf Steckbörtern / per Jumper-Kabeln getestet wird, ist hier die Übersicht der wichtigsten Verbindungen:

* **ESP32-S3-CAM & Raspberry Pi:**
  * Verbindung erfolgt über USB (serielle Schnittstelle, erkannt unter `/dev/ttyACM0` am Raspberry Pi).
  * Datenübertragung / Serverkommunikation über WLAN (ESP32 sendet Sensordaten an den Flask-Server auf dem Raspberry Pi).

* **Wasserpumpe:**
  * Angesteuert über einen digitalen Ausgang des ESP32 (geschaltet via Transrelay/Relais-Modul).
  * Spannungsversorgung: 12V externe Stromquelle für die Pumpen, gesteuert über 3.3V/5V Logikpegel.

* **Sensoren (Wasserstand, Bodenfeuchte, NIR):**
  * Analog- und I2C-Anschlüsse (SDA/SCL) an den entsprechenden GPIOs des ESP32-S3.

### 🎯 Ziel der Stückliste

Die Stückliste schafft eine nachvollziehbare Übersicht über die verwendete Hardware, den Entwicklungsstand und die Kosten unseres Projekts. Sie wird während der Entwicklung aktualisiert, damit klar erkennbar bleibt, welche Komponenten bereits getestet wurden und welche Schritte noch ausstehen.


---

## 🌟 Hintergrund: Biologie des Düngens

Rasen braucht vor allem drei wichtige Nährstoffe:

- **Stickstoff (N)** → Wachstum und grüne Farbe
- **Phosphor (P)** → Energiestoffwechsel und Wurzelentwicklung
- **Kalium (K)** → Wasserhaushalt und Widerstandsfähigkeit gegen Stress

> **Wie viele Messstationen braucht man?**
>
> Für ein Grundstück von etwa 400 bis 600 m² könnte eine zentrale externe Station als Ausgangspunkt ausreichen, wenn der Mähroboter die Fläche abfährt und die Messwerte zuverlässig übermittelt. Ob eine Station genügt, hängt allerdings von der Grundstücksform, den Bodenunterschieden und der gewünschten Messgenauigkeit ab. Das muss praktisch getestet werden.

---

## 🔌 Benötigte Hardware & Komponenten

- 🔌 [Raspberry Pi – Kabel, Micro-USB](https://www.reichelt.de/de/de/shop/produkt/raspberry_pi_-_kabel_micro-usb_m_auf_usb_typ_a_f_otg_10cm_-316284)
- 🖥️ **Raspberry Pi 3 Model B+** – aktuell verwendete Entwicklungs- und Serverplattform
- 🔄 [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) – mögliche spätere, kompaktere Alternative
- ⚡ [Thing Plus – ESP32-S3](https://www.antratek.de/thing-plus-esp32-s3)
- 📷 **ESP32-S3-CAM** – Kameraboard mit 16 MB Flash und 8 MB PSRAM für Bildaufnahme und spätere Bildauswertung
- 🌡️ [Spectral Sensor Breakout – AS7263 NIR (Qwiic)](https://www.antratek.de/spectral-sensor-breakout-as7263-nir)
- 🌱 [Feuchtesensor für Bodenfeuchte](https://www.reichelt.de/de/de/shop/produkt/arduino_-_feuchtesensor_fuer_bodenfeuchte-282511)
- 🛰️ [ZED-F9P-15B GPS-Modul](https://www.digikey.de/de/products/detail/u-blox/ZED-F9P-15B/20838269)
- 💧 **Wasserstandssensor** zur Überwachung eines Tanks
- ⚙️ **Pumpe** für erste Funktionstests und spätere Dosieraufgaben
- 🤖 [Mähroboter smart SILENO max (800 m²)](https://www.gardena.com/de/produkte/rasenpflege/maehroboter/maehroboter-smart-sileno-max-800-m/970620803.html)
- 💦 **Externer Wassersprinkler** für die spätere gezielte Bewässerung

*Hinweis: Die endgültige Auswahl und der Anschluss der Komponenten werden während der Entwicklung weiter geprüft.*

---

## 📊 Sensoren-Vergleich

| Kriterien | AS7263 (NIR) | MLX90614 (IR-Temp) |
|---|---|---|
| **Messprinzip** | NIR-Reflexion mit 6 Spektralkanälen | Berührungslose Oberflächentemperatur |
| **Eignung zur Feuchtigkeitserkennung** | Indirekte Schätzung muss getestet und kalibriert werden | Nur indirekte Hinweise über Temperatur |
| **Einfluss von Sonne/Wind** | Beleuchtung, Schatten, Abstand und Oberfläche können die Messung beeinflussen | Umgebungstemperatur, Sonne und Wind beeinflussen die Temperaturmessung |
| **Datenmenge** | 6 Spektralkanäle | Temperaturwert |
| **Preis** | Höher (ca. 40,40 $ laut bisheriger Recherche) | Niedriger (ca. 16,79 $ laut bisheriger Recherche) |

> **Der Haken am Tag:** Sonnenlicht, Schatten und unterschiedliche Oberflächen können optische Messungen beeinflussen.
>
> Wir möchten den **AS7263 NIR** einsetzen und untersuchen, ob sich über Verhältnisse verschiedener Spektralkanäle Unterschiede zwischen trockenen und feuchten Rasenbereichen erkennen lassen. Dafür müssen wir die Messungen mit tatsächlichen Feuchtigkeitswerten vergleichen und kalibrieren.

---

## ✅ Bisherige Erfolge (Meilensteine)

1. **Pumpenansteuerung:** Die Pumpe kann über den ESP32 angesteuert werden.
2. **Wasserstandsmessung:** Der Wasserstandssensor liefert Messwerte in regelmäßigen Abständen von etwa 0,75 Sekunden.
3. **WLAN & Server:** Die Verbindung zwischen ESP32 und Raspberry Pi wurde erfolgreich hergestellt.
4. **SSH-Zugriff:** Der Raspberry Pi lässt sich über SSH bedienen.
5. **USB-Erkennung:** Der Raspberry Pi erkennt den USB-Seriell-Anschluss des ESP32-S3 unter `/dev/ttyACM0`.
6. **Chip-Erkennung:** Der ESP32-S3 wurde mit `esptool` erfolgreich erkannt. Die Ausgabe bestätigt 8 MB PSRAM; der Flash-Speicher ist laut Board-Spezifikation 16 MB groß.

---

## 🔜 Nächste Schritte

- [ ] Passende Firmware für das ESP32-S3-CAM installieren
- [ ] Kamera testen und erste Bilder aufnehmen
- [ ] Datenübertragung und regelmäßige Messwerterfassung stabilisieren
- [ ] Live-Tabelle und Diagramme in einer Web-App entwickeln
- [ ] NIR-Messungen durchführen und mit tatsächlichen Feuchtigkeitswerten vergleichen
- [ ] Messwerte für spätere Auswertungen speichern
- [ ] Positionsdaten und Messwerte zu einer Feuchtigkeitskarte verbinden
- [ ] Bild- und Sensordaten später gemeinsam auswerten
- [ ] Bedarfsgerechte Bewässerung und Düngung langfristig umsetzen

---

## 🎯 Ziel des Projekts

Unser Ziel ist ein **modular erweiterbares und intelligentes System zur Rasenpflege**, das Sensorik, Kamera, Datenauswertung und automatisierte Pflege verbindet. Dadurch soll der Pflegeaufwand sinken und Wasser sowie Dünger sollen möglichst effizient eingesetzt werden.

<img width="2397" height="2112" alt="grafik" src="https://github.com/user-attachments/assets/4c539276-b0d2-4964-bcd7-0d185c8e2141" />

