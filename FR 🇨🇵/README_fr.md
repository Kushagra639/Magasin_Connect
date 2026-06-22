| [English 🇬🇧](/README.md) | [Español 🇪🇸](/ES%20🇪🇸/README_es.md) | [Italiano 🇮🇹](/IT%20🇮🇹/README_it.md) | [Português 🇵🇹](/PT%20🇵🇹/README_pt.md) | [Deutsch 🇩🇪](/DE%20🇩🇪/README_de.md) | [Nederlands 🇳🇱](/NL%20🇳🇱/README_nl.md) | [Русский 🇷🇺](/RU%20🇷🇺/README_ru.md) | [日本語 🇯🇵](/JP%20🇯🇵/README_jp.md) | [中文 🇨🇳](/CN%20🇨🇳/README_cn.md) | [한국어 🇰🇷](/KR%20🇰🇷/README_kr.md) |
|-|-|-|-|-|-|-|-|-|-| 

# 🛍️ Magasin Connect

**Magasin Connect** est un **système de gestion de magasin** basé sur Python, doté d'une interface utilisateur graphique élégante et moderne, développée avec `CustomTkinter`. Il permet aux commerçants de gérer leurs stocks, d'enregistrer leurs transactions d'achat et de vente, et de suivre leurs profits, tout en stockant leurs données de manière sécurisée dans une base de données MySQL.

> 💡 Développé dans le cadre d'un projet informatique de terminale.

---

## ✨ Fonctionnalités

- 🔐 **Connexion et inscription sécurisées à la boutique** (avec hachage de mot de passe `bcrypt`)
- 📦 **Gestion des stocks** – Ajouter, modifier et consulter des articles
- 📊 **Enregistrement des transactions** – Enregistrer les ventes/achats avec mise à jour des stocks en temps réel
- 💰 **Calcul des profits/pertes** – Total ou entre deux dates
- 🎨 **Basculement du thème** – Prise en charge des modes clair et foncé avec une interface utilisateur pastel personnalisée
- 🛢️ **Intégration de base de données MySQL** – Toutes les données de la boutique sont stockées de manière permanente
- 🧹 **Validation des données et gestion des erreurs** – Pour une fiabilité et une expérience utilisateur optimales

---

## 🛠️ Technologies utilisées

| Outil / Bibliothèque     | Objectif                                                      |
|--------------------------|---------------------------------------------------------------|
| `Python 3`               | Langage de programmation principal                            |
| `MySQL`                  | Base de données pour stocker l'inventaire et les transactions |
| `mysql-connector-python` | Connexion Python à MySQL                                      |
| `bcrypt`                 | Hachage de mot de passe sécurisé                              |
| `CustomTkinter`          | Interface graphique moderne pour Python (avec thème)          |
| `tkinter.messagebox`     | Messages contextuels d'erreur/informations                    |

---
## ⚙️ Configuration
### Installer les dépendances
Assurez-vous d'installer les dépendances en exécutant le code suivant dans *powershell* :
```bash
pip install mysql-connector-python bcrypt customtkinter
```

### Configurer MySQL
Assurez-vous que MySQL Server est installé et opérationnel. Créer une base de données nommée :
```MySQL
CREATE DATABASE magasin_connect;
```

### Apporter des modifications au code
- **Mettez à jour** votre *nom d'utilisateur* et votre *mot de passe* MySQL dans le fichier MagasinConnectGUI_fr.py
```Python
MagasinConnect = SQL.connect(
    host="localhost",
    user="root",
    password="votre mot de passe",
    database="magasin_connect"
)
```

- **Mettez à jour** le chemin du thème dans le fichier MagasinConnectGUI_fr.py vers le chemin de votre système
```Python
ctk.set_appearance_mode("system") # Sets the appearance mode to system default (light or dark based on system settings)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system
```

### Exécuter l'application
```bash
python MagasinConnectGUI_fr.py
```
---

## 👨🏻‍💻 Le Code
*Copiez* et *collez* le code dans **« VS Code »** ou **« Python IDLE »** et exécutez-le après avoir effectué les modifications ci-dessus.
| [Code in English](/MagasinConnectGUI.py) 🇬🇧 | [Le Code en Français](FR%20🇨🇵/MagasinConnectGUI_fr.py) 🇫🇷 |
|-|-|

[Fichier de thème](/pastel_theme.json) 🎨

---

## 🙋‍♂️ Auteur - 
Kushagra Aggarwal
- Élève, classe de Terminale
- Dr. B. R. Ambedkar SoSE, Plot no. 1, Link Road, Karol Bagh
- Delhi Board of School Education (DBSE)

Ce projet a été conçu avec passion pour l'informatique et ses applications concrètes.

---

## 📜 Licence

Ce projet est sous licence MIT.

Consultez le fichier LICENSE pour plus de détails.

---

📌 Remarques :

- ⚠️ Ne nommez pas votre boutique **« shops »** (c'est une table réservée).
- 🎨 Le chemin du thème dans le code peut nécessiter une mise à jour selon votre système.

---

N'hésitez pas à ⭐ le dépôt si vous le trouvez utile !
