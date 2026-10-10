# Rasenpflege leicht gemacht!

## 📌 Kurzfassung

In unserem Projekt erweitern wir einen Rasenmähroboter, damit dieser nicht nur den Rasen selbstständig mäht, sondern zusätzlich auch die Bewässerung bzw. Düngung des Gartens übernehmen kann.

Dadurch soll weniger manueller Aufwand entstehen. Der Roboter soll mithilfe verschiedener Sensoren die Umgebung erkennen. Dazu ist der Aufbau des Mähroboters so geplant, dass der Roboter die Feuchtigkeit des Rasens messen kann, anschließend falls benötigt den Rasen versorgt und schneidet, sodass ein gepflegter Rasen entsteht. Unser Fokus liegt darauf, dass der Roboter wassersparend und leicht zu bedienen ist.

---

## 📋 Projekt-Plan & Aufgaben

### 💡 Was der Rasenmäher machen muss:
- Selbstständiges Mähen des Rasens
- Automatische ~~Bewässerung~~ --> **Düngung** des Gartens
- Feuchtigkeitssensoren erkennen, ob der Boden Wasser braucht
- Integrierter ~~Wassertank für die Bewässerung~~ --> **Tank mit Dünger** (kommt aber erst später dazu)

> **Hinweis:** 
> - Automatisches Nachfüllen des Tanks ist noch unklar.
> - Nach dem Mähen wird der Rasen gedüngt.

### 🛠️ Was wir noch machen wollen:
- ESP32 soll jede Sekunde Daten schicken.
- Raspberry Pi soll Live-Tabelle + Diagramm in einer Web-App anzeigen.
- Wir schauen, dass wir auf den **Raspberry Pi Zero W** umsteigen.
- Alles soll einfach, übersichtlich und stabil laufen.
- Später vielleicht eine App daraus machen.

### 🚀 Zukunftskonzept: Intelligente Rasenpflege
Unser System geht deutlich über die ursprüngliche Idee hinaus. Der Roboter, die externe Station und ein externer Wassersprinkler arbeiten zusammen:
- **Exakte Feuchtigkeitsmessung:** Über eine externe Station, die auf dem Rasen frei platziert ist (nicht direkt auf dem Mähroboter).
- **Präzisionsbewässerung:** Ein Wassersprinkler übernimmt die Bewässerung und bringt nur dort Wasser aus, wo es wirklich notwendig ist.

#### Was die externe Station leisten soll:
* **Zentrale Datensammlung:** Alle Feuchtigkeitswerte, GPS-Positionen und Statusmeldungen laufen hier zusammen.
* **Live-Web-App:** Übersichtliche Anzeige aller Werte, Feuchtigkeitskarten, Warnungen und Wasserverbrauch.
* **Steuerung des Wassersprinklers:** Die Station entscheidet, welche Stelle gegossen wird – nicht der Sprinkler selbst.
* **Automatische Feuchtigkeitskarte:** Aus GPS-Daten + Feuchtigkeitsmessungen entsteht eine Karte, die trockene Bereiche zeigt.

---

## 🌟 Hintergrund: Biologie des Düngens
Rasen braucht vor allem drei Nährstoffe:
- **Stickstoff (N)** → Wachstum, Farbe
- **Phosphor (P)** → Wurzelbildung
- **Kalium (K)** → Stressresistenz, Trockenheit, Hitze

> **Wie viele Messstationen braucht man?**
> Für ein durchschnittliches Grundstück in der Größe von 400 bis 600 m² reicht eine zentrale externe Station völlig aus. Der Roboter fährt die Fläche ab, misst unterwegs und die Station steuert den Sprinkler gezielt an *(Info via ChatGPT)*.

---

## 🔌 Benötigte Hardware & Komponenten
- 🔌 [Raspberry Pi - Kabel, Micro-USB](https://www.reichelt.de/de/de/shop/produkt/raspberry_pi_-_kabel_micro-usb_m_auf_usb_typ_a_f_otg_10cm_-316284)
- ⚡ [Thing Plus - ESP32-S3](https://www.antratek.de/thing-plus-esp32-s3)
- 🌡️ [Spectral Sensor Breakout - AS7263 NIR (Qwiic)](https://www.antratek.de/spectral-sensor-breakout-as7263-nir)
- 🌡️ [Feuchtesensor für Bodenfeuchte](https://www.reichelt.de/de/de/shop/produkt/arduino_-_feuchtesensor_fuer_bodenfeuchte-282511)
- 🛰️ [ZED-F9P-15B GPS Modul](https://www.digikey.de/de/products/detail/u-blox/ZED-F9P-15B/20838269)
- 🤖 [Mähroboter Smart SILENO max (800 m²)](https://www.gardena.com/de/produkte/rasenpflege/maehroboter/maehroboter-smart-sileno-max-800-m/970620803.html)

---

## 📊 Sensoren-Vergleich

| Kriterien | AS7263 (NIR) | MLX90614 (IR-Temp) |
| :--- | :--- | :--- |
| **Messprinzip** | NIR-Reflexion (6 Kanäle) | Oberflächentemperatur |
| **Eignung für Feuchtigkeit** | Sehr gut | Bedingt |
| **Einfluss von Sonne/Wind** | Gering | Hoch |
| **Datenmenge** | Viel (6 Werte) | Wenig (1 Wert) |
| **Preis** | Höher (~40,40 $) \vert{} Niedriger (~16,79$) |

> **Der Haken am Tag:** Sonnenlicht, Schatten und IR-Anteile stören die Messung. 
> Wir nutzen den **AS7263 NIR** und setzen auf Wellenlängen-Verhältnisse (z. B. 760/860 nm), weil Wasser in diesem Bereich Licht stärker absorbiert.

---

## ✅ Bisherige Erfolge (Meilensteine)
1. **Pumpe** wird mit dem ESP32 angesteuert.
2. **Wasserstandssensor** wird vom ESP32 angesteuert und liefert alle 0,75 s Messwerte.
3. **WLAN & Server:** Verbindung zwischen ESP32 und Raspberry Pi steht.

---

