# 🌱 Rasenpflege leicht gemacht!

## 📌 Kurzfassung

In unserem Projekt erweitern wir einen Rasenmähroboter, damit dieser nicht nur den Rasen selbstständig mäht, sondern zusätzlich auch die Bewässerung bzw. Düngung des Gartens übernehmen kann.

Dadurch soll weniger manueller Aufwand entstehen. Der Roboter soll mithilfe verschiedener Sensoren die Umgebung erkennen. Dazu ist der Aufbau des Systems so geplant, dass die Feuchtigkeit des Rasens gemessen werden kann. Anschließend soll der Rasen bei Bedarf versorgt und gepflegt werden, sodass ein gesunder Rasen entsteht. Unser Fokus liegt darauf, Wasser und Dünger sparsam einzusetzen und das System einfach zu bedienen.

---

## 📋 Projekt-Plan & Aufgaben

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
- Wir prüfen, ob wir auf den **Raspberry Pi Zero W** umsteigen können.
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
