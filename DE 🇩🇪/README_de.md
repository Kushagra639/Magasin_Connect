| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [English 🇬🇧](/README.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) |
|-|-|-|-|-|-|-| 
# 🛍️ Magasin Connect

**Magasin Connect** ist ein Python-basiertes **Store-Management-System** mit einer eleganten und modernen grafischen Benutzeroberfläche, entwickelt mit `CustomTkinter`. Es ermöglicht Händlern, ihren Bestand zu verwalten, ihre Kauf- und Verkaufstransaktionen zu erfassen und ihre Gewinne zu verfolgen. Die Daten werden dabei sicher in einer MySQL-Datenbank gespeichert.

> 💡 Entwickelt im Rahmen eines IT-Abschlussprojekts.

---

## ✨ Funktionen

- 🔐 **Sichere Shop-Anmeldung und -Registrierung** (mit `bcrypt`-Passwort-Hashing)
- 📦 **Lagerverwaltung** – Artikel hinzufügen, bearbeiten und anzeigen
- 📊 **Transaktionsaufzeichnung** – Erfassung von Verkäufen/Käufen mit Echtzeit-Lageraktualisierungen
- 💰 **Gewinn-/Verlustberechnung** – Gesamt oder zwischen zwei Daten
- 🎨 **Designwechsel** – Unterstützung für Hell- und Dunkelmodus mit einer benutzerdefinierten pastellfarbenen Benutzeroberfläche
- 🛢️ **MySQL-Datenbankintegration** – Alle Shop-Daten werden dauerhaft gespeichert
- 🧹 **Datenvalidierung und Fehlerbehandlung** – Für optimale Zuverlässigkeit und Benutzerfreundlichkeit

---

## 🛠️ Verwendete Technologien

| Tool / Bibliothek        | Zweck                                                         |
|--------------------------|---------------------------------------------------------------|
| `Python 3`               | Primäre Programmiersprache                                    |
| `MySQL`                  | Datenbank zur Speicherung von Inventar und Transaktionen      |
| `mysql-connector-python` | Python-zu-MySQL-Verbindung                                    |
| `bcrypt`                 | Sicheres Passwort-Hashing                                     |
| `CustomTkinter`          | Moderne Python-GUI (thematisch)                               |
| `tkinter.messagebox`     | Fehler-/Info-Popup-Meldungen                                  |

---
## ⚙️ Konfiguration
### Abhängigkeiten installieren
Stellen Sie sicher, dass Sie Ihre Abhängigkeiten installieren, indem Sie den folgenden Code in *PowerShell* ausführen:
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### MySQL konfigurieren
Stellen Sie sicher, dass MySQL Server installiert und ausgeführt wird. Erstellen Sie eine Datenbank mit dem Namen:
```MySQL
CREATE DATABASE magasin_connect;
```

### Codeänderungen vornehmen
- **Aktualisieren** Sie Ihren MySQL-Benutzernamen und Ihr MySQL-Passwort in der Datei MagasinConnectGUI.py.
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your Password",
    database="magasin_connect"
)
```

- **Aktualisieren** Sie den Designpfad in der Datei MagasinConnectGUI.py entsprechend Ihrem Systempfad.
```Python
ctk.set_appearance_mode("system") # Setzt den Anzeigemodus auf den Systemstandard (hell oder dunkel, abhängig von den Systemeinstellungen).
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Setzt das Standardfarbdesign auf ein benutzerdefiniertes Pastelldesign (wird neben diesem Code angegeben). Bitte ändern Sie den Pfad zur Designdatei entsprechend Ihrem System.
```

### Führen Sie die Anwendung aus
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 Der Code
Kopieren Sie den Code einfach und fügen Sie ihn in **"VS Code"** oder **"Python IDLE"** ein. Führen Sie ihn anschließend nach den oben genannten Änderungen aus.
| [Code in English 🇬🇧](/MagasinConnectGUI.py) | [Le Code en Français 🇫🇷](FR%20🇨🇵/MagasinConnectGUI_fr.py) |
|-|-|
---

## 🙋‍♂️ Autor - 
Kushagra Aggarwal
- Schüler, 12. Klasse
- Dr. B. R. Ambedkar SoSE, Plot no. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

Dieses Projekt wurde mit Leidenschaft für Informatik und ihre praktischen Anwendungen entwickelt.

---

📄 Lizenz:

Dieses Projekt ist für Bildungszwecke freigegeben.

Für andere Zwecke wenden Sie sich bitte an den Autor.

---

📌 Hinweise:

- ⚠️ Nennen Sie Ihren Shop nicht „shops“ (es handelt sich um einen reservierten Tisch).
- 🎨 Der Themenpfad im Code muss je nach System möglicherweise aktualisiert werden.

---

Bei Interesse können Sie das Repository gerne ⭐ nutzen!
