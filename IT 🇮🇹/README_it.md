| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [English 🇬🇧](/README.md) | [Português 🇵🇹](/PT%20🇵🇹/README_pt.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) | [中文 🇨🇳](/CN%20🇨🇳/README_cn.md) | [한국어 🇰🇷](/KR%20🇰🇷/README_kr.md) |
|-|-|-|-|-|-|-|-|-| 

# 🛍️ Magasin Connect

**Magasin Connect** è un **sistema di gestione del negozio** basato su Python con un'interfaccia utente grafica moderna e accattivante, realizzata con `CustomTkinter`. Permette ai negozianti di gestire il proprio inventario, registrare le transazioni di acquisto e vendita e monitorare i profitti, il tutto archiviando i dati in modo sicuro in un database MySQL.

> 💡 Sviluppato come progetto di informatica per la classe 12.

---

## ✨ Funzionalità

- 🔐 **Accesso e registrazione sicuri al negozio** (con hashing della password `bcrypt`)
- 📦 **Gestione inventario** – Aggiungi, modifica e visualizza articoli
- 📊 **Registrazione transazioni** – Registra vendite/acquisti con aggiornamento delle scorte in tempo reale
- 💰 **Calcolo profitti/perdite** – Totale o tra due date qualsiasi
- 🎨 **Toggle tema** – Supporto modalità chiara e scura con un'interfaccia utente pastello personalizzata
- 🛢️ **Integrazione con database MySQL** – Tutti i dati del negozio vengono archiviati in modo permanente
- 🧹 **Convalida dati e gestione errori** – Per una migliore affidabilità e un'esperienza utente migliore

---

## 🛠️ Tecnologie utilizzate

| Strumento/Libreria | Scopo |
|----------------------|---------------------------------------------------|
| `Python 3` | Linguaggio di programmazione principale |
| `MySQL` | Database per l'archiviazione di inventario e transazioni |
| `mysql-connector-python` | Connessione Python con MySQL |
| `bcrypt` | Hashing sicuro delle password |
| `CustomTkinter` | Framework GUI moderno per Python (con temi) |
| `tkinter.messagebox` | Messaggi pop-up per errori/informazioni |

---
## ⚙️ Configurazione
### Installa le dipendenze
Assicurati di installare le dipendenze eseguendo il seguente codice in *PowerShell*:
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### Configura MySQL
Assicurati che MySQL Server sia installato e in esecuzione. Crea un database denominato:
```MySQL
CREATE DATABASE magasin_connect;
```

### Apporta modifiche al codice
- **Aggiorna** il tuo *nome utente* e la tua *password* MySQL nel file MagasinConnectGUI.py
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your password",
    database="magasin_connect"
)
```

- **Aggiorna** il percorso del tema nel file MagasinConnectGUI.py con il percorso del tuo sistema.
```Python
ctk.set_appearance_mode("system") # Imposta la modalità di aspetto predefinita del sistema (chiara o scura in base alle impostazioni di sistema)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Imposta il tema colore predefinito su un tema pastello personalizzato (fornito insieme a questo codice). Modifica il percorso del file del tema in base al tuo sistema.
```

### Esegui l'applicazione
```bash
python MagasinConnectGUI.py
```
---

## 👨🏻‍💻 Il codice
È sufficiente *copiare* e *incollare* il codice in **"VS Code"** o **"Python IDLE"** ed eseguirlo dopo aver apportato le modifiche sopra indicate.
| [Code in English](/MagasinConnectGUI.py) 🇬🇧 | [Le Code en Français](FR%20🇨🇵/MagasinConnectGUI_fr.py) 🇫🇷 |
|-|-|

[Fascicolo del tema](/pastel_theme.json) 🎨

---

## 🙋‍♂️ Autore - 
Kushagra Aggarwal
- Studente, 12° anno
- Dr. B. R. Ambedkar, SoSE, Plot no. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

Questo progetto è stato ideato con la passione per l'informatica e le sue applicazioni pratiche.

---

## 📜 Licenza

Questo progetto è distribuito con licenza MIT.

Consulta il file LICENSE per i dettagli.

---

📌 Note:

- ⚠️ Non chiamare il tuo negozio "shops" (è una tabella riservata).
- 🎨 Il percorso del tema nel codice potrebbe dover essere aggiornato a seconda del sistema.

---

Sentiti libero di ⭐ il repository se lo trovi utile!
