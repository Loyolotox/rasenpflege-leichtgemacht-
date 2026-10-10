<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rasenpflege leicht gemacht!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
            background-color: #f4f6f8;
        }
        h1, h2, h3 {
            color: #2e7d32;
        }
        h1 {
            border-bottom: 3px solid #2e7d32;
            padding-bottom: 10px;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        .info-box {
            background: #e8f5e9;
            border-left: 5px solid #4caf50;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }
        .warning-box {
            background: #fff3e0;
            border-left: 5px solid #ff9800;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }
        code {
            background: #eee;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
            background: #272822;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #2e7d32;
            color: white;
        }
    </style>
</head>
<body>

    <h1>Rasenpflege leicht gemacht!</h1>

    <div class="card">
        <h2>Kurzfassung</h2>
        <p>In unserem Projekt erweitern wir einen Rasenmähroboter, damit dieser nicht nur den Rasen selbstständig mäht, sondern zusätzlich auch die Bewässerung bzw. Düngung des Gartens übernehmen kann.</p>
        <p>Dadurch soll weniger manueller Aufwand entstehen. Der Roboter soll mithilfe verschiedener Sensoren die Umgebung erkennen. Dazu ist der Aufbau des Mähroboters so geplant, dass der Roboter die Feuchtigkeit des Rasens messen kann, anschließend falls benötigt den Rasen versorgt und schneidet, sodass ein gepflegter Rasen entsteht. Unser Fokus liegt darauf, dass der Roboter wassersparend und leicht zu bedienen ist.</p>
    </div>

    <div class="card">
        <h2>Projekt-Plan & Aufgaben</h2>
        <h3>Was der Rasenmäher machen muss:</h3>
        <ul>
            <li>Selbstständiges Mähen des Rasens</li>
            <li>Automatische Düngung / Bewässerung des Gartens</li>
            <li>Feuchtigkeitssensoren erkennen, ob der Boden Wasser braucht</li>
            <li>Integrierter Tank für Dünger/Wasser (Kommt später dazu)</li>
        </ul>

        <div class="warning-box">
            <strong>Noch unklar / In Planung:</strong>
            <ul>
                <li>Automatisches Nachfüllen des Tanks</li>
                <li>Nach dem Mähen wird der Rasen gedüngt</li>
            </ul>
        </div>

        <h3>Was wir noch machen wollen:</h3>
        <ul>
            <li>ESP32 soll jede Sekunde Daten schicken</li>
            <li>Raspberry Pi soll Live-Tabelle + Diagramm in einer Web-App anzeigen</li>
            <li>Umstieg auf den <strong>Raspberry Pi Zero W</strong></li>
            <li>Alles soll einfach, übersichtlich und stabil laufen</li>
            <li>Später vielleicht eine App daraus machen</li>
        </ul>

        <h3>Zukunftskonzept: Intelligente Rasenpflege mit externer Station</h3>
        <p>Unser System geht deutlich über die ursprüngliche Idee hinaus:</p>
        <ul>
            <li>Exakte Feuchtigkeitsmessung über eine externe Station auf dem Rasen</li>
            <li>Die Bewässerung wird von einem Wassersprinkler übernommen, der nur dort Wasser ausbringt, wo es notwendig ist.</li>
        </ul>
        
        <h4>Was die externe Station leisten soll:</h4>
        <ul>
            <li><strong>Zentrale Datensammlung:</strong> Alle Feuchtigkeitswerte, GPS-Positionen und Statusmeldungen laufen hier zusammen.</li>
            <li><strong>Live-Web-App:</strong> Übersichtliche Anzeige aller Pflanzen, Feuchtigkeitskarten, Warnungen und Wasserverbrauch.</li>
            <li><strong>Steuerung des Wassersprinklers:</strong> Die Station entscheidet, welche Stelle gegossen wird.</li>
            <li><strong>Automatische Feuchtigkeitskarte:</strong> Aus GPS-Daten + Feuchtigkeitsmessungen entsteht eine trockene/feuchte Karte.</li>
        </ul>
    </div>

    <div class="card">
        <h2>Hintergrund: Düngen & Biologie</h2>
        <p>Rasen braucht vor allem drei Nährstoffe: Stickstoff (N), Phosphor (P) und Kalium (K).</p>
        <div class="info-box">
            <strong>Wie viele Messstationen braucht man?</strong>
            <p>Für ein durchschnittliches Grundstück (400–600 m²) reicht eine zentrale externe Station völlig aus. Der Roboter fährt die Fläche ab, misst unterwegs, und die Station steuert den Sprinkler gezielt an. (Quelle: ChatGPT)</p>
        </div>
    </div>

    <div class="card">
        <h2>Sensoren & Hardware</h2>
        <h3>AS7263 NIR Spektralsensor</h3>
        <table>
            <tr>
                <th>Kriterien</th>
                <th>AS7263 (NIR)</th>
                <th>MLX90614 (IR-Temp)</th>
            </tr>
            <tr>
                <td>Messprinzip</td>
                <td>NIR-Reflexion (6 Kanäle)</td>
                <td>Oberflächentemperatur</td>
            </tr>
            <tr>
                <td>Eignung für Feuchtigkeit</td>
                <td>sehr gut</td>
                <td>bedingt</td>
            </tr>
            <tr>
                <td>Einfluss Sonne/Wind</td>
                <td>gering</td>
                <td>hoch</td>
            </tr>
        </table>
        <p><strong>Der Haken am Tag:</strong> Sonnenlicht, Schatten und IR-Anteile stören. Wir nutzen den AS7263 NIR und setzen auf Verhältnisse (z. B. 760/860 nm), da Wasser in diesem Bereich Licht stärker absorbiert.</p>
    </div>

    <div class="card">
        <h2>Erreichte Meilensteine</h2>
        <div class="info-box">
            <ul>
                <li>Pumpe wird mit dem ESP32 angesteuert</li>
                <li>Wasserstandssensor wird vom ESP32 angesteuert (liefert alle 0,75s Messwerte)</li>
                <li>WLAN-Verbindung und Server-Datenübertragung zum Raspberry Pi eingerichtet</li>
            </ul>
        </div>
    </div>

</body>
</html>
