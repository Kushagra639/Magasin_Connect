| [Français 🇫🇷](/FR%20🇨🇵/README_fr.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本 🇯🇵](/JP%20🇯🇵/README_jp.md) |
|-|-|-|-|-|-|-| 
# 🛍️ Magasin Connect

**Magasin Connect** is a Python-based **shop management system** with a beautiful, modern GUI built using `CustomTkinter`. It allows shopkeepers to manage their inventory, log purchase and sale transactions, and track profits—all while storing data securely in a MySQL database.

> 💡 Developed as a Class 12 Computer Science Project.

---

## ✨ Features

- 🔐 **Secure Shop Login & Registration** (with `bcrypt` password hashing)
- 📦 **Inventory Management** – Add, edit, and view items
- 📊 **Transaction Recording** – Log sales/purchases with real-time stock update
- 💰 **Profit/Loss Calculation** – Total or between any two dates
- 🎨 **Theme Toggle** – Light & Dark mode support with a custom pastel UI
- 🛢️ **MySQL Database Integration** – All shop data is stored persistently
- 🧹 **Data Validation & Error Handling** – For better reliability and user experience

---

## 🛠️ Technologies Used

| Tool / Library       | Purpose                                           |
|----------------------|---------------------------------------------------|
| `Python 3`           | Core programming language                         |
| `MySQL`              | Database to store inventory and transactions      |
| `mysql-connector-python` | Connect Python with MySQL                      |
| `bcrypt`             | Secure password hashing                           |
| `CustomTkinter`      | Modern GUI framework for Python (with theming)    |
| `tkinter.messagebox` | Pop-up messages for errors/info                   |

---
## ⚙️ Setup
### Install dependencies
Make sure to install the dependencies by running the following code in *powershell* :
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### Set up MySQL
Make sure you have MySQL Server installed and running.
Create a database named:
```MySQl
CREATE DATABASE magasin_connect;
```

### Make changes in the code
**Update** your MySQL *username* and *password* in the MagasinConnectGUI.py file
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="magasin_connect"
)
```
**Update** the theme's path in MagasinConnectGUI.py file to the path in your system
```Python
ctk.set_appearance_mode("system") # Sets the appearance mode to system default (light or dark based on system settings)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system
```

### Run the app
```bash
python MagasinConnectGUI.py
```
---

## Code
| [Code in English 🇬🇧](/MagasinConnectGUI.py) | [Le Code en Français 🇫🇷](FR%20🇨🇵/MagasinConnectGUI_fr.py) |
|-|-|
Just *Copy* and *Paste* the code in **"VS Code"** or **"Python IDLE"** and run it after making the above changes.
---

## 🙋‍♂️ Author - 
Kushagra Aggarwal
- Student, Class 12
- Dr. B. R. Ambedkar SoSE, Plot No. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

This project was built with passion for Computer Science and real-world application.

---

📄 License :

This project is open for educational use.

For other uses, please contact the author.

---

📌 Notes :

- ⚠️ Do not name your shop shops (it's a reserved table).
- 🎨 Theme path in the code may need to be updated depending on your system.

---

Feel free to ⭐ the repository if you find it useful!
