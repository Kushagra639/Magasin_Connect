| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [English 🇬🇧](/README.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) |
|-|-|-|-|-|-|-| 
# 🛍️ Magasin Connect

**Magasin Connect** is een Python-gebaseerd **winkelbeheersysteem** met een strakke en moderne grafische gebruikersinterface, ontwikkeld met `CustomTkinter`. Het stelt winkeliers in staat hun voorraad te beheren, hun aan- en verkooptransacties te registreren en hun winst bij te houden, terwijl hun gegevens veilig worden opgeslagen in een MySQL-database.

> 💡 Ontwikkeld als onderdeel van een afstudeerproject in de IT.

---

## ✨ Functies

- 🔐 **Veilig inloggen en registreren in de winkel** (met `bcrypt`-wachtwoordhashing)
- 📦 **Voorraadbeheer** – Artikelen toevoegen, bewerken en bekijken
- 📊 **Transactieregistratie** – Verkopen/aankopen registreren met realtime voorraadupdates
- 💰 **Winst-/verliesberekening** – Totaal of tussen twee datums
- 🎨 **Themawisseling** – Ondersteuning voor lichte en donkere modi met een aangepaste pastelkleurige gebruikersinterface
- 🛢️ **MySQL-database-integratie** – Alle winkelgegevens worden permanent opgeslagen
- 🧹 **Gegevensvalidatie en foutverwerking** – Voor optimale betrouwbaarheid en gebruikerservaring

---

## 🛠️ Gebruikte technologieën

| Tool / Bibliotheek       | Doel                                                    |
|--------------------------|---------------------------------------------------------|
| `Python 3`               | Primaire programmeertaal                                |
| `MySQL`                  | Database voor het opslaan van inventaris en transacties |
| `mysql-connector-python` | Python-naar-MySQL-verbinding                            |
| `bcrypt`                 | Veilige wachtwoordhash                                  |
| `CustomTkinter`          | Moderne Python GUI (thema)                              |
| `tkinter.messagebox`     | Fout-/info-pop-upberichten                              |

---
## ⚙️ Configuratie
### Afhankelijkheden installeren
Zorg ervoor dat u uw afhankelijkheden installeert door de volgende code uit te voeren in *powershell*:
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### MySQL configureren
Zorg ervoor dat de MySQL-server is geïnstalleerd en actief is. Maak een database met de naam:
```MySQL
CREATE DATABASE magasin_connect;
```

### Wijzigingen aanbrengen in de code
- **Werk** je MySQL *gebruikersnaam* en *wachtwoord* bij in het bestand MagasinConnectGUI.py
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your password",
    database="magasin_connect"
)
```

- **Werk** het themapad in het bestand MagasinConnectGUI.py bij naar het pad van je systeem
```Python
ctk.set_appearance_mode("systeem") # Stelt de weergavemodus in op de standaardinstelling van het systeem (licht of donker, afhankelijk van de systeeminstellingen)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Stelt het standaardkleurenthema in op een aangepast pastelthema (zie deze code). Wijzig het pad naar het themabestand indien nodig voor je systeem.
```

### Voer de applicatie uit
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 De code
*Kopieer* en *plak* de code in **"VS Code"** of **"Python IDLE"** en voer deze uit nadat u de bovenstaande wijzigingen hebt aangebracht.
| [Code in English 🇬🇧](/MagasinConnectGUI.py) | [Le Code en Français 🇫🇷](FR%20🇨🇵/MagasinConnectGUI_fr.py) |
|-|-|
---

## 🙋‍♂️ Auteur - 
Kushagra Aggarwal
- Leerling, 12e klas
- Dr. B. R. Ambedkar SoSE, Plot no. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

Dit project is ontworpen met een passie voor computerwetenschappen en de toepassingen ervan in de praktijk.

---

📄 Licentie:

Dit project is open voor educatief gebruik.

Voor ander gebruik kunt u contact opnemen met de auteur.

---

📌 Opmerkingen:

- ⚠️ Noem uw winkel niet "shops" (het is een gereserveerde tafel).
- 🎨 Het themapad in de code moet mogelijk worden bijgewerkt, afhankelijk van uw systeem.

---

Voel je vrij om de repository te ⭐ als je het nuttig vindt!
