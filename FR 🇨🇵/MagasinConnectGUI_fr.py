import mysql.connector as SQL # Vous devrez peut-être installer ce module en exécutant pip install mysql-connector-python dans le terminal
import bcrypt # Vous devrez peut-être installer ce module en exécutant pip install bcrypt dans le terminal
import customtkinter as ctk # Vous devrez peut-être installer ce module en exécutant pip install customtkinter dans le terminal
from tkinter import messagebox # Ce module est préinstallé avec Python
from datetime import datetime # Pour la validation des dates
import re

def is_valid_shop_name(name):
    return re.match(r'^[A-Za-z0-9_]+$', name) is not None

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def hash_password(password):  # Convertit un mot de passe de chaîne en hachage
    try:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    except Exception as e:
        print(f" ❌ Erreur de hachage du mot de passe : {e}")
        messagebox.showerror("Erreur de hachage", f"Erreur de hachage du mot de passe : {e}")
        return None

def check_password(password, hashed): # Correspond au mot de passe haché dans la base de données
    try:
        return bcrypt.checkpw(password.encode(), hashed)
    except Exception as e:
        print(f" ❌ Erreur de la vérification du mot de passe : {e}")
        messagebox.showerror("Erreur de Vérification", f"Erreur de la vérification du mot de passe : {e}")
        return False

MagasinConnect = SQL.connect(
    host="localhost", # Entrez votre hôte MySQL ici (localhost par défaut)
    user="root", # Entrez votre nom d'utilisateur MySQL ici (root par défaut)
    password="Votre Mot de Passe", # Entrez ici votre mot de passe MySQL (créé lors de l'installation)
    database="magasin_connect" # Créez une base de données MySQL et entrez son nom ici
)

if MagasinConnect.is_connected(): # Vérifie si l'objet connecteur est correctement connecté à la base de données MySQL
    print(" ✅ Connexion réussie à la base de données")
else:
    print(" ❌ Échec de la connexion à la base de données")

MagasinCursor = MagasinConnect.cursor(dictionary=True) # Dictionary = True lui permet de renvoyer des lignes sous la forme d'un dictionnaire

def DataIntable(name): # Extrait toutes les données présentes dans une table donnée
    try:
        MagasinCursor.execute(f'SELECT * FROM `{name}`')
        rows = MagasinCursor.fetchall()
        return rows
    except SQL.Error as e:
        print(f" ❌ Erreur lors de la récupération des données de la table {name}: {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la récupération des données de la table {name}: {e}")
        return {}
    
def IfTableExists(Nom): # Checks whether the table exists in the MySQL database
    try:
        MagasinCursor.execute(f'''SELECT COUNT(*) 
                            FROM information_schema.tables 
                            WHERE table_schema = 'magasin_connect'
                            AND table_name = '{Nom}' ''')
        if MagasinCursor.fetchone()[0] == 1:
            print(f" ✅ Table {Nom} existe déjà")
            return True
        else:
            print(f" ❌ Table {Nom} n'existe pas")
            return False
    except Exception as e:
        print(f" ❌ Erreur lors de la vérification de l'existence de la table {Nom} : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la vérification de l'existence de la table {Nom} : {e}")
        return False

def NouvMagasinTable(Nom): # Crée un ensemble de 2 tables pour la boutique, à savoir <nom de la boutique> et <nom de la boutique>_transactions, cette dernière étant une table enfant connectée via l'attribut de clé étrangère
    try:
        if Nom.lower() != 'shops':
            MagasinCursor.execute(f'''CREATE TABLE IF NOT EXISTS `{Nom}` (
                                item_no INT AUTO_INCREMENT PRIMARY KEY, 
                                item_name VARCHAR(255) NOT NULL, 
                                cost_price DECIMAL(10,2) NOT NULL, 
                                retail_sales_price DECIMAL(10,2) NOT NULL, 
                                stock_number INT NOT NULL)''')
        
            MagasinCursor.execute(f'''CREATE TABLE IF NOT EXISTS `{Nom}_transactions` (
                                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                                item_no INT,
                                item_name VARCHAR(255) NOT NULL,
                                date DATE NOT NULL,
                                amount_sold INT DEFAULT 0,
                                amount_purchased INT DEFAULT 0,
                                discount DECIMAL(5,2) DEFAULT 0.00,
                                selling_price DECIMAL(10,2),
                                buying_price DECIMAL(10,2),
                                FOREIGN KEY (item_no) REFERENCES `{Nom}`(item_no)
                                )''')
            MagasinConnect.commit()
            print(f" ✅ Table {Nom} créé avec succès")
        else :
            print(" ❌ Impossible de créer une table nommée « shops », veuillez choisir un autre nom.")
            messagebox.showerror("Erreur de nom","Le nom de la boutique ne peut pas être « shops » ! Veuillez réessayer avec un nom différent.")
            login_screen()
    except SQL.Error as e:
        print(f" ❌ Erreur lors de la création de la table : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la création de la table {Nom} : {e}")
        MagasinConnect.rollback()

def MagasinTableFill(name, item_name, cost_price, retail_sales_price, stock_number): # Remplit les données dans une ligne de la table <nom de la boutique>
    try :
        MagasinCursor.execute(f'''INSERT INTO `{name}` 
            (item_name, cost_price, retail_sales_price, stock_number) 
            VALUES (%s, %s, %s, %s)''', (item_name, cost_price, retail_sales_price, stock_number))
        MagasinConnect.commit()
        print(f" ✅ L'élément {item_name} a été ajouté avec succès au tableau")
    except SQL.Error as e:
        print(f" ❌ Erreur lors de l'ajout d'un élément au tableau {name}: {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de l'ajout d'un élément au tableau {name}: {e}")
        MagasinConnect.rollback()
    
def MagasinTableEdit(name, item_no, item_name=None, cost_price=None, retail_sales_price=None, stock_number=None): # Modifie les données présentes dans l'une des lignes de la table <nom de la boutique>
    try :
        updates = []
        if item_name is not None:
            updates.append(f"item_name = '{item_name}'")
        if cost_price is not None:
            updates.append(f"cost_price = {cost_price}")
        if retail_sales_price is not None:
            updates.append(f"retail_sales_price = {retail_sales_price}")
        if stock_number is not None:
            updates.append(f"stock_number = {stock_number}")

        if updates:
            update_query = ", ".join(updates)
            MagasinCursor.execute(f'''UPDATE `{name}` SET {update_query} WHERE item_no = {item_no}''')
            MagasinConnect.commit()
            print(f" ✅ Numéro d'article {item_no} mis à jour avec succès dans le tableau")
        else:
            print(" ❌ Aucun champ à mettre à jour")
        MagasinConnect.commit()
    except Exception as e:
        print(f" ❌ Erreur lors de la mise à jour de l'élément dans le tableau {name}: {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la mise à jour de l'élément dans le tableau {name}: {e}")
        MagasinConnect.rollback()

def MagasinTransactionTableEdit(name, transaction_id, item_name=None, date=None, amount_sold=None, amount_purchased=None, discount=None, selling_price=None, buying_price=None): # Modifie les données présentes dans l'une des lignes de la table <shop name>_transactions
    try:
        updates = []
        if item_name is not None:
            updates.append(f"item_name = '{item_name}'")
        if date is not None:
            if date.strip() == '':
                print(" ❌ La date ne peut pas être vide.")
                messagebox.showerror("Erreur", "La date ne peut pas être vide.")
                return
            elif not is_valid_date(date):
                print(" ❌ Format de date non valide. Utilisez AAAA-MM-JJ.")
                messagebox.showerror("Erreur", "Format de date non valide. Utilisez AAAA-MM-JJ.")
                return
            else:
                updates.append(f"date = '{date}'")
        if amount_sold is not None:
            updates.append(f"amount_sold = {amount_sold}")
        if amount_purchased is not None:
            updates.append(f"amount_purchased = {amount_purchased}")
        if discount is not None:
            updates.append(f"discount = {discount}")
        if selling_price is not None:
            updates.append(f"selling_price = {selling_price}")
        if buying_price is not None:
            updates.append(f"buying_price = {buying_price}")

        if updates:
            update_query = ", ".join(updates)
            MagasinCursor.execute(f'''UPDATE `{name}_transactions` SET {update_query} WHERE transaction_id = {transaction_id}''')
            MagasinConnect.commit()
            print(f" ✅ La transaction pour l'ID de transaction {transaction_id} a été mise à jour avec succès dans la table des transactions")
        else:
            print(" ❌ Aucun champ à mettre à jour")
        MagasinConnect.commit()
    except Exception as e:
        print(f" ❌ Erreur lors de la mise à jour de la transaction dans la table {name}_transactions : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la mise à jour de la transaction dans la table {name}_transactions : {e}")
        MagasinConnect.rollback()

def MagasinTransactionFill(name, no, itemname, date, amount_sold, amount_purchased, discount, selling_price, buying_price): # Remplit les données dans une ligne de la table <nom de la boutique>_transactions
    try :
        MagasinCursor.execute(
            f'''INSERT INTO `{name}_transactions` 
            (item_no, item_name, date, amount_sold, amount_purchased, discount, selling_price, buying_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
            (no, itemname, date, amount_sold, amount_purchased, discount, selling_price, buying_price)
        )
        if amount_sold < 0 or amount_purchased < 0: # Si le montant vendu ou le montant acheté est négatif, l'utilisateur est invité à réessayer
            print(" ❌ Le montant vendu ou acheté ne peut pas être négatif")
            messagebox.showerror("Erreur", "Le montant vendu ou acheté ne peut pas être négatif.")
            MagasinConnect.rollback()
            return
        elif amount_sold < 0 and amount_purchased > 0: # Si le montant vendu est négatif et le montant acheté est positif, il invite l'utilisateur à réessayer
            print(" ❌ Vous ne pouvez pas vendre une quantité négative d'un article")
            messagebox.showerror("Erreur", "Vous ne pouvez pas vendre une quantité négative d'un article.")
            MagasinConnect.rollback()
            return
        elif amount_purchased < 0 and amount_sold > 0: # Si le montant acheté est négatif et le montant vendu est positif, il invite l'utilisateur à réessayer
            print(" ❌ Vous ne pouvez pas acheter une quantité négative d'un article")
            messagebox.showerror("Erreur", "Vous ne pouvez pas acheter une quantité négative d'un article.")
            MagasinConnect.rollback()
        elif amount_sold > 0 and amount_purchased > 0: # Si le montant vendu et le montant acheté sont tous deux supérieurs à 0, l'utilisateur est invité à réessayer
            print(" ❌ Vous ne pouvez pas vendre et acheter le même article en même temps")
            messagebox.showerror("Erreur", "Vous ne pouvez pas vendre et acheter le même article en même temps.")
            MagasinConnect.rollback()
        elif amount_sold < 0 and amount_purchased == 0: # Si le montant vendu est négatif et le montant acheté est 0, il invite l'utilisateur à réessayer
            print(" ❌ Vous ne pouvez pas vendre une quantité négative d'un article")
            messagebox.showerror("Erreur", "Vous ne pouvez pas vendre une quantité négative d'un article.")
            MagasinConnect.rollback()
            return
        elif amount_purchased < 0 and amount_sold == 0: # Si le montant acheté est négatif et le montant vendu est 0, il invite l'utilisateur à réessayer
            print(" ❌ Vous ne pouvez pas acheter une quantité négative d'un article")
            messagebox.showerror("Erreur", "Vous ne pouvez pas acheter une quantité négative d'un article.")
            MagasinConnect.rollback()
            return
        elif amount_sold > 0 and amount_purchased == 0: # Si le montant vendu est supérieur à 0 et le montant acheté est 0, il met à jour le numéro de stock dans la table de la boutique
            MagasinCursor.execute(
                f"UPDATE `{name}` SET stock_number = stock_number - %s WHERE item_no = %s", (amount_sold, no))
        elif amount_purchased > 0 and amount_sold == 0: # Si le montant acheté est supérieur à 0 et le montant vendu est 0, il met à jour le numéro de stock dans la table de la boutique
            MagasinCursor.execute(
                f"UPDATE `{name}` SET stock_number = stock_number + %s WHERE item_no = %s", (amount_purchased, no))
        MagasinConnect.commit()
        print(f" ✅ Transaction for item no. {no} added successfully to the transactions table")
    except SQL.Error as e:
        print(f" ❌ Erreur lors de l'ajout de la transaction à la table {name}_transactions : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de l'ajout de la transaction à la table {name}_transactions : {e}")
        MagasinConnect.rollback()

def CréerCompteMagasin(shop_name, password): # Crée une ligne avec le nom de la boutique et le mot de passe dans la table des boutiques pour vérifier ultérieurement le mot de passe
    try:
        MagasinCursor.execute('''CREATE TABLE IF NOT EXISTS shops (
            shop_name VARCHAR(255) PRIMARY KEY,
            password_hash BLOB NOT NULL)''')
        hashed = hash_password(password)
        MagasinCursor.execute("INSERT INTO shops (shop_name, password_hash) VALUES (%s, %s)", (shop_name, hashed))
        MagasinConnect.commit()
    except SQL.Error as e:
        print(f" ❌ Erreur lors de la création du compte boutique : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la création du compte boutique : {e}")
        MagasinConnect.rollback()
    except Exception as e:
        print(f" ❌ Erreur lors de la création du compte boutique : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la création du compte boutique : {e}")
        MagasinConnect.rollback()

def VérifierMagasinMdP(shop_name, password): # Vérifie le mot de passe saisi par l'utilisateur par rapport à celui présent dans la table shops de la base de données
    try:
        MagasinCursor.execute("SELECT password_hash FROM shops WHERE shop_name = %s", (shop_name,))
        row = MagasinCursor.fetchone()
        if row and check_password(password, row['password_hash']): # type: ignore
            return True
        else:
            return False
    except SQL.Error as e:
        print(f" ❌ Erreur lors de la vérification du mot de passe de la boutique : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la vérification du mot de passe de la boutique : {e}")
        return False
    except Exception as e:
        print(f" ❌ Erreur lors de la vérification du mot de passe de la boutique : {e}")
        messagebox.showerror("Erreur de base de données", f"Erreur lors de la vérification du mot de passe de la boutique : {e}")
        return False

ctk.set_appearance_mode("system") # Définit le mode d'apparence par défaut du système (clair ou foncé selon les paramètres du système)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Définit le thème de couleur par défaut sur un thème pastel personnalisé (fourni avec ce code), veuillez modifier le chemin d'accès au fichier de thème en fonction de votre système

app = ctk.CTk() # Crée la fenêtre principale de l'application à l'aide de customtkinter
app.title("Magasin Connect 🛍️") # Définit le titre de la fenêtre de l'application
app.geometry("900x700") # Définit la taille initiale de la fenêtre
app.resizable(width=True, height=True) # Permet à la fenêtre d'être redimensionnable

shop_name = ctk.StringVar() # Variable pour stocker le nom de la boutique saisi par l'utilisateur
passwrd = ctk.StringVar() # Variable pour stocker le mot de passe saisi par l'utilisateur

def change_theme(): # Fonction permettant de basculer entre les thèmes clairs et sombres
    try:
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")
    except Exception as e:
        print(f" ❌ Erreur lors du changement de thème : {e}")
        messagebox.showerror("Erreur de thème", f"Erreur lors du changement de thème : {e}")

def clear_screen(): # Fonction permettant d'effacer l'écran actuel en détruisant tous les widgets de la fenêtre principale de l'application
    try:
        for widget in app.winfo_children():
            widget.destroy()
    except Exception as e:
        print(f" ❌ Erreur lors de l'effacement de l'écran : {e}")
        messagebox.showerror("Erreur d'écran", f"Erreur lors de l'effacement de l'écran : {e}")

def login(): # Fonction pour gérer la connexion des utilisateurs
    try:
        MagasinCursor.execute('''CREATE TABLE IF NOT EXISTS shops (
            shop_name VARCHAR(255) PRIMARY KEY,
            password_hash BLOB NOT NULL)''')
        name = shop_name.get().strip()
        pwd = passwrd.get().strip()

        if not name or not pwd: # Vérifie si les deux champs sont remplis
            messagebox.showerror("Erreur", "Veuillez saisir les deux champs.")
            return
        MagasinCursor.execute("SELECT shop_name FROM shops WHERE shop_name = %s", (name,))
        shop_exists = MagasinCursor.fetchone() # Vérifie si la boutique existe dans la base de données
        if not shop_exists:
            messagebox.showerror("Introuvable", "Boutique non enregistrée. Veuillez d'abord vous inscrire.")
            return
        if not VérifierMagasinMdP(name, pwd): # Vérifie le mot de passe saisi par l'utilisateur
            messagebox.showerror("Erreur", "Mot de passe incorrect.")
            return
        MagasinCursor.execute(f'''SELECT COUNT(*) as count FROM information_schema.tables 
                                WHERE table_schema = 'magasin_connect' 
                                AND table_name = %s''', (name,)) # Vérifie si la table principale de la boutique existe
        items_table = MagasinCursor.fetchone()['count'] # type: ignore
        MagasinCursor.execute(f'''SELECT COUNT(*) as count FROM information_schema.tables 
                                WHERE table_schema = 'magasin_connect' 
                                AND table_name = %s''', (name + "_transactions",)) # Vérifie si la table des transactions de la boutique existe
        transactions_table = MagasinCursor.fetchone()['count'] # type: ignore
        if items_table != 1 or transactions_table != 1: # Vérifiez si la table des transactions de la boutique existe
            MagasinCursor.execute("DELETE FROM shops WHERE shop_name = %s", (name,))
            MagasinConnect.commit()
            messagebox.showerror(
                "Corrupted Shop",
                f"Shop '{name}' had missing data tables.\n It has been removed.\nPlease register again."
            )
            return
        messagebox.showinfo("Succès", f"Bienvenue à nouveau à {name}!")
        main_menu(name)
    except SQL.Error as e:
        print(f" ❌ Erreur lors de la connexion : {e}")
        messagebox.showerror("Erreur de connexion", f"Erreur lors de la connexion : {e}")
    except Exception as e:
        print(f" ❌ Erreur lors de la connexion : {e}")
        messagebox.showerror("Erreur de connexion", f"Erreur lors de la connexion : {e}")

def register(): # Fonction pour gérer l'enregistrement des utilisateurs
    try:
        MagasinCursor.execute('''CREATE TABLE IF NOT EXISTS shops (
            shop_name VARCHAR(255) PRIMARY KEY,
            password_hash BLOB NOT NULL)''')
        name = shop_name.get().strip()
        pwd = passwrd.get().strip()
        if name.lower() == 'shops': # Empêche l'utilisateur d'enregistrer une boutique avec le nom « shops »
            messagebox.showerror("Erreur de nom", "Le nom de la boutique ne peut pas être « shops » ! Veuillez réessayer avec un autre nom.")
            return
        elif not is_valid_shop_name(name):
            messagebox.showerror("Erreur de nom", "Le nom de la boutique ne peut contenir que des lettres, des chiffres et des traits de soulignement!")
            return
        elif not name or not pwd:
            messagebox.showerror("Erreur", "Veuillez remplir les deux champs.")
            return
        MagasinCursor.execute("SELECT shop_name FROM shops WHERE shop_name = %s", (name,))
        if MagasinCursor.fetchone(): # Vérifie si la boutique existe déjà dans la base de données
            messagebox.showwarning("Existe", "La boutique existe déjà. Essayez de vous connecter.")
        else:
            CréerCompteMagasin(name, pwd) # Crée un nouveau compte de boutique avec le nom et le mot de passe donnés
            NouvMagasinTable(name) # Crée la table principale et la table des transactions pour la nouvelle boutique
            messagebox.showinfo("Inscrite", f"Boutique « {name} » enregistrée.")
            main_menu(name) # Redirige vers le menu principal après une inscription réussie
    except SQL.Error as e:
        print(f" ❌ Erreur lors de l'inscription : {e}")
        messagebox.showerror("Erreur d'enregistrement", f"Erreur lors de l'inscription : {e}")
    except Exception as e:
        print(f" ❌ Erreur lors de l'inscription : {e}")
        messagebox.showerror("Erreur d'enregistrement", f"Erreur lors de l'inscription : {e}")

def main_menu(name): # Fonction permettant d'afficher le menu principal après une connexion ou une inscription réussie
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text=f"Bienvenue à {name}!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        options = [
            "Ajouter un article", "Ajouter une transaction", "Bénéfice/perte total",
            "Bénéfice/perte dans la plage de dates", "Afficher les articles", "Afficher les transactions",
            "Modifier l'élément", "Modifier la transaction", "Déconnexion"
        ] # Liste des options du menu principal
        for idx, opt in enumerate(options, 1):
            ctk.CTkButton(app, text=f"{idx}. {opt}", command=lambda i=idx: option_selected(i)).pack(pady=4) # Crée des boutons pour chaque option du menu principal
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans le menu principal : {e}")
        messagebox.showerror("Erreur de menu", f"Erreur dans le menu principal : {e}")

def add_item_screen(): # Fonction permettant d'afficher l'écran d'ajout d'un nouvel article à la boutique
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Ajouter un article", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        item_name = ctk.StringVar()
        cost_price = ctk.DoubleVar()
        retail_sales_price = ctk.DoubleVar()
        stock_number = ctk.IntVar()

        ctk.CTkLabel(app, text="Nom de l'article :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Nom de l'article", textvariable=item_name).pack(pady=5)
        ctk.CTkLabel(app, text="Prix ​​de revient :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Prix ​​de revient", textvariable=cost_price).pack(pady=5)
        ctk.CTkLabel(app, text="Prix ​​de vente au détail :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Prix ​​de vente au détail", textvariable=retail_sales_price).pack(pady=5)
        ctk.CTkLabel(app, text="Numéro d'inventaire :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Numéro d'inventaire", textvariable=stock_number).pack(pady=5)

        def add_item(): # Fonction permettant de gérer l'ajout d'un nouvel article à la boutique
            if item_name.get() and cost_price.get() >= 0 and retail_sales_price.get() >= 0 and stock_number.get() >= 0: # Vérifie si tous les champs sont correctement remplis
                MagasinTableFill(shop_name.get().strip(), item_name.get(), cost_price.get(), retail_sales_price.get(), stock_number.get())
                messagebox.showinfo("Succès", "Article ajouté avec succès.")
                main_menu(shop_name.get().strip())
            else: # Si un champ n'est pas rempli correctement, un message d'erreur s'affiche
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")
                main_menu(shop_name.get().strip())

        ctk.CTkButton(app, text="Ajouter l'article", command=add_item).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Retour au Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran d'ajout d'élément : {e}")
        messagebox.showerror("Erreur d'ajout d'élément", f"Erreur dans l'écran d'ajout d'élément : {e}")

def add_transaction_screen(): # Fonction permettant d'afficher l'écran d'ajout d'une nouvelle transaction à la boutique
    try :
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Ajouter une transaction", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        rows = DataIntable(shop_name.get().strip()) # Récupère tous les éléments de la table principale de la boutique
        if not rows: # S'il n'y a aucun article dans la boutique, un message d'erreur s'affiche et redirige vers le menu principal
            messagebox.showerror("Erreur", "Aucun article trouvé dans la boutique. Veuillez d'abord ajouter des articles.")
            main_menu(shop_name.get().strip())
            return
        item_options = [f"{row['item_no']} - {row['item_name']}" for row in rows] # type: ignore

        ctk.CTkLabel(app, text="\n".join(item_options), font=ctk.CTkFont(size=12)).pack(pady=10) # Affiche la liste des articles de la boutique

        item_no = ctk.IntVar()
        item_name = ctk.StringVar()
        date = ctk.StringVar()
        amount_sold = ctk.IntVar()
        amount_purchased = ctk.IntVar()
        discount = ctk.DoubleVar()
        selling_price = ctk.DoubleVar()
        buying_price = ctk.DoubleVar()
        discount.set(0.0) # Définit la remise par défaut à 0,0
        amount_purchased.set(0) # Définit le montant par défaut acheté à 0
        amount_sold.set(0) # Définit le montant par défaut vendu à 0

        ctk.CTkLabel(app, text="Numéro d'article (voir dans la liste ci-dessus) :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Numéro d'article", textvariable=item_no).pack(pady=5)
        ctk.CTkLabel(app, text="Date (AAAA-MM-JJ):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Date (AAAA-MM-JJ)", textvariable=date).pack(pady=5)
        ctk.CTkLabel(app, text="Montant vendu :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Montant vendu", textvariable=amount_sold).pack(pady=5)
        ctk.CTkLabel(app, text="Montant acheté :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Montant acheté", textvariable=amount_purchased).pack(pady=5)
        ctk.CTkLabel(app, text="Rabais (%):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Rabais (%)", textvariable=discount).pack(pady=5)
        def add_transaction(): # Fonction permettant de gérer l'ajout d'une nouvelle transaction à la boutique
            for row in rows: # Remplit le champ du nom de l'élément en fonction du numéro d'élément sélectionné
                if row['item_no'] == item_no.get(): # type: ignore
                    item_name.set(row['item_name']) # type: ignore
                    selling_price.set(float(row['retail_sales_price']) * (100 - discount.get())/100) # type: ignore
                    buying_price.set(float(row['cost_price']) - (float(row['cost_price']) * discount.get()/100)) # type: ignore
            if amount_purchased.get() < 0: # Si le montant acheté est négatif, un message d'erreur s'affiche
                print(" ❌ Le montant acheté ne peut pas être négatif")
                messagebox.showerror("Erreur", "Le montant acheté ne peut pas être négatif.")
                return
            elif amount_sold.get() < 0: # Si le montant vendu est négatif, un message d'erreur s'affiche
                print(" ❌ Le montant vendu ne peut pas être négatif")
                messagebox.showerror("Erreur", "Le montant vendu ne peut pas être négatif.")
                return
            elif amount_purchased.get() == 0 and amount_sold.get() == 0: # Si les deux montants sont nuls, un message d'erreur s'affiche
                print(" ❌ Veuillez saisir le montant vendu ou le montant acheté.")
                messagebox.showerror("Erreur", "Veuillez saisir le montant vendu ou le montant acheté.")
                return
            elif amount_sold.get() > 0 and amount_purchased.get() > 0: # Si les deux montants sont supérieurs à zéro, un message d'erreur s'affiche
                print(" ❌ Veuillez saisir soit le montant vendu, soit le montant acheté, mais pas les deux.")
                messagebox.showerror("Erreur", "Veuillez saisir soit le montant vendu, soit le montant acheté, mais pas les deux.")
                return
            elif date.get().strip() == '' :
                print(" ❌ Veuillez entrer une date.")
                messagebox.showerror("Erreur", "Veuillez entrer une date.")
                return
            elif date.get().strip() == '':
                print(" ❌ Le champ Date ne peut pas être vide. Remplissez-le.")
                messagebox.showerror("Erreur", "Le champ Date ne peut pas être vide. Remplissez-le.")
                return
            elif not is_valid_date(date.get().strip()): # Si la date n'est pas dans un format valide, un message d'erreur s'affiche
                print(" ❌ Format de date ou date non valide. Utilisez AAAA-MM-JJ.")
                messagebox.showerror("Erreur", "Format de date ou date non valide. Utilisez AAAA-MM-JJ.")
                return
            elif (item_no.get() > 0 and
                discount.get() >= 0.0 and
                discount.get() < 100.0 and
                item_name.get().strip() != ""): # Vérifie si tous les champs sont correctement remplis
                MagasinTransactionFill(shop_name.get().strip(), item_no.get(), item_name.get(), date.get(),
                                    amount_sold.get(), amount_purchased.get(), discount.get(),
                                    selling_price.get(), buying_price.get())
                messagebox.showinfo("Succès", "Transaction ajoutée avec succès.")
                main_menu(shop_name.get().strip())
            else: # Si un champ n'est pas rempli correctement, un message d'erreur s'affiche
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs correctement.")
                main_menu(shop_name.get().strip())
        ctk.CTkButton(app, text="Ajouter une transaction", command=add_transaction).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de Thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran d'ajout de transaction : {e}")
        messagebox.showerror("Ajouter une erreur de transaction", f"Erreur dans l'écran d'ajout de transaction : {e}")

def total_profit_loss_screen(): # Fonction pour afficher l'écran total des profits/pertes
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Bénéfice/perte total", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        MagasinCursor.execute(f'''SELECT SUM(selling_price * amount_sold) - SUM(buying_price * amount_purchased) AS total_profit_loss
                                FROM `{shop_name.get().strip()}_transactions`''')
        result = MagasinCursor.fetchone() # Récupère le bénéfice/la perte total à partir de la table des transactions
        total_profit_loss = result['total_profit_loss'] if result['total_profit_loss'] is not None else 0 # type: ignore
        ctk.CTkLabel(app, text=f"Bénéfice/perte total : {total_profit_loss:.2f}").pack(pady=10) # Affiche le bénéfice/la perte total calculé à partir du tableau des transactions
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran de profit/perte total : {e}")
        messagebox.showerror("Erreur de profit/perte", f"Erreur dans l'écran de profit/perte total : {e}")

def profit_loss_date_range_screen(): # Fonction permettant d'afficher le profit/la perte dans un écran de plage de dates spécifique
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Bénéfice/perte dans la plage de dates", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        start_date = ctk.StringVar()
        end_date = ctk.StringVar()
        ctk.CTkLabel(app, text="Date de début (AAAA-MM-JJ) :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Date de début (AAAA-MM-JJ) :", textvariable=start_date).pack(pady=5)
        ctk.CTkLabel(app, text="Date de fin (AAAA-MM-JJ) :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Date de fin (AAAA-MM-JJ) :", textvariable=end_date).pack(pady=5)
        def calculate_profit_loss(): # Fonction pour calculer le profit/la perte dans la plage de dates spécifiée
            if start_date.get().strip() == "" or end_date.get().strip() == "": # Si l'un des champs de date est vide, un message d'erreur s'affiche
                messagebox.showerror("Erreur", "Veuillez remplir les deux champs de date.")
                main_menu(shop_name.get().strip())
            elif not is_valid_date(start_date.get().strip()) or not is_valid_date(end_date.get().strip()): # Si l'un des champs de date n'est pas dans un format valide, un message d'erreur s'affiche
                messagebox.showerror("Erreur", "Format de date non valide. Utilisez AAAA-MM-JJ.")
                main_menu(shop_name.get().strip())
            elif is_valid_date(start_date.get().strip()) and is_valid_date(end_date.get().strip()): # Vérifie si les deux champs de date sont remplis
                MagasinCursor.execute(f'''SELECT SUM(selling_price * amount_sold) - SUM(buying_price * amount_purchased) AS profit_loss
                                        FROM `{shop_name.get().strip()}_transactions`
                                        WHERE date BETWEEN '{start_date.get()}' AND '{end_date.get()}' ''')
                result = MagasinCursor.fetchone()
                profit_loss = result['profit_loss'] if result['profit_loss'] is not None else 0 # type: ignore
                messagebox.showinfo("Bénéfice/Perte", f"Bénéfice/perte de {start_date.get()} à {end_date.get()} : {profit_loss:.2f}")
            else: # Si l'un des champs de date n'est pas rempli, un message d'erreur s'affiche
                messagebox.showerror("Erreur", "Veuillez remplir les deux champs de date.")
                main_menu(shop_name.get().strip())
        ctk.CTkButton(app, text="Calculer le bénéfice/la perte", command=calculate_profit_loss).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran de plage de dates de profit/perte : {e}")
        messagebox.showerror("Erreur de plage de dates de profit/perte", f"Erreur dans l'écran de plage de dates de profit/perte : {e}")

def view_items_screen(): # Fonction pour afficher l'écran des éléments de vue
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Afficher les articles", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        items = DataIntable(shop_name.get().strip())
        if not items: # S'il n'y a aucun article dans la boutique, un message d'erreur s'affiche
            ctk.CTkLabel(app, text="Aucun élément trouvé.").pack(pady=10)
        else: # S'il y a des éléments, il les affiche sous forme de liste
            for item in items:
                ctk.CTkLabel(app, text=f"Numéro d'article : {item['item_no']}, Nom: {item['item_name']}, " # type: ignore
                                    f"Prix ​​de revient: {item['cost_price']}, Prix ​​en détail : {item['retail_sales_price']}, " # type: ignore
                                    f"Action : {item['stock_number']}").pack(pady=5) # type: ignore
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran d'affichage des éléments : {e}")
        messagebox.showerror("Erreur d'affichage des éléments", f"Erreur dans l'écran d'affichage des éléments : {e}")

def view_transactions_screen(): # Fonction pour afficher l'écran de visualisation des transactions
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Afficher les transactions", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        transactions = DataIntable(f"{shop_name.get().strip()}_transactions")
        if not transactions: # S'il n'y a aucune transaction dans la boutique, un message d'erreur s'affiche
            ctk.CTkLabel(app, text="Aucune transaction trouvée.").pack(pady=10)
        else: # S'il y a des transactions, il les affiche sous forme de liste
            for transaction in transactions:
                ctk.CTkLabel(app, text=f"Identifiant de transaction : {transaction['transaction_id']}, Numéro d'article : {transaction['item_no']}, " # type: ignore
                                    f"Nom : {transaction['item_name']}, Date : {transaction['date']}, " # type: ignore
                                    f"Vendu(e) : {transaction['amount_sold']}, Acheté(e) : {transaction['amount_purchased']}, " # type: ignore
                                    f"Rabais : {transaction['discount']}, Prix ​​de vente : {transaction['selling_price']}, " # type: ignore
                                    f"Prix ​​d'achat : {transaction['buying_price']}").pack(pady=5) # type: ignore
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran d'affichage des transactions : {e}")
        messagebox.showerror("Erreur d'affichage des transactions", f"Erreur dans l'écran d'affichage des transactions : {e}")

def edit_item_screen(): # Fonction permettant d'afficher l'écran de modification d'un article existant dans la boutique
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        shop = shop_name.get()
        ctk.CTkLabel(app, text="Modifier l'élément", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        MagasinCursor.execute(f"SELECT item_no, item_name FROM `{shop}`")
        items = MagasinCursor.fetchall()
        if not items: # S'il n'y a aucun article dans la boutique, un message d'erreur s'affiche et redirige vers le menu principal
            messagebox.showinfo("Vide", "Aucun article trouvé dans la boutique.")
            main_menu(shop)
            return
        item_options = [f"{item['item_no']} - {item['item_name']}" for item in items] # type: ignore
        selected_item = ctk.StringVar(value=item_options[0])
        ctk.CTkOptionMenu(app, values=item_options, variable=selected_item).pack(pady=5)
        field_var = ctk.StringVar(value="nom_élément")
        value_var = ctk.StringVar()
        ctk.CTkOptionMenu(app, values=["nom_élément", "prix_de_revient", "prix_de_vente_au_détail"], variable=field_var).pack(pady=5)
        ctk.CTkLabel(app, text="Entrez une nouvelle valeur :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Nouvelle valeur", textvariable=value_var).pack(pady=5)

        def submit_edit(): # Fonction permettant de gérer la soumission de la modification de l'élément sélectionné
            selection = selected_item.get().split(" - ")[0]
            item_no = int(selection)
            field = field_var.get()
            new_value = value_var.get().strip()
            if not new_value: # Vérifie si la nouvelle valeur est fournie
                messagebox.showerror("Erreur", "Veuillez saisir une nouvelle valeur.")
                return
            try:
                if field == "nom_élément":
                    MagasinCursor.execute(f"UPDATE `{shop}` SET item_name = %s WHERE item_no = %s", (new_value, item_no))
                elif field == "prix_de_revient":
                    MagasinCursor.execute(f"UPDATE `{shop}` SET cost_price = %s WHERE item_no = %s", (float(new_value), item_no))
                elif field == "prix_de_vente_au_détail":
                    MagasinCursor.execute(f"UPDATE `{shop}` SET retail_sales_price = %s WHERE item_no = %s", (float(new_value), item_no))
                else:
                    messagebox.showerror("Champ invalide", "Champ non pris en charge sélectionné.")
                    return
            except Exception as e:
                messagebox.showerror("Erreur", f"Échec de la mise à jour : {e}")
                return
            MagasinConnect.commit()
            messagebox.showinfo("Succès", f"L'élément {item_no} a été mis à jour avec succès.")
            main_menu(shop)
        ctk.CTkButton(app, text="Soumettre Modifier", command=submit_edit).pack(pady=8)
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop)).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran d'édition de l'élément : {e}")
        messagebox.showerror("Erreur d'édition d'élément", f"Erreur dans l'écran d'édition de l'élément : {e}")

def edit_transaction_screen(): # Fonction permettant d'afficher l'écran de modification d'une transaction existante dans la boutique
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        shop = shop_name.get()
        table = f"{shop}_transactions"
        ctk.CTkLabel(app, text="Modifier la transaction", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        MagasinCursor.execute(f"SELECT transaction_id, item_name FROM `{table}`")
        transactions = MagasinCursor.fetchall()
        if not transactions: # S'il n'y a aucune transaction dans la boutique, un message d'erreur s'affiche et redirige vers le menu principal
            messagebox.showinfo("Vide", "Aucune transaction trouvée.")
            main_menu(shop)
            return
        transaction_options = [f"{t['transaction_id']} - {t['item_name']}" for t in transactions] # type: ignore
        selected_transaction = ctk.StringVar(value=transaction_options[0])
        ctk.CTkOptionMenu(app, values=transaction_options, variable=selected_transaction).pack(pady=5)
        field_var = ctk.StringVar(value="nom_article")
        value_var = ctk.StringVar()
        ctk.CTkOptionMenu(app, values=[
            "date", "montant_vendu", "montant_acheté", "rabais"
        ], variable=field_var).pack(pady=5)
        ctk.CTkLabel(app, text="Entrez une nouvelle valeur :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Nouvelle valeur", textvariable=value_var).pack(pady=5)

        def submit_edit_transaction(): # Fonction permettant de gérer la soumission de la modification pour la transaction sélectionnée
            try:
                transaction_id = int(selected_transaction.get().split(" - ")[0])
                field = field_var.get()
                new_value = value_var.get().strip()
                if not new_value: # Vérifie si la nouvelle valeur est fournie
                    messagebox.showerror("Erreur", "Veuillez saisir une nouvelle valeur.")
                    return
                elif field == "date": # Valide le format de date et met à jour la date de transaction
                    if not is_valid_date(new_value): # Valide le format de date
                        messagebox.showerror("Date invalide", "Saisissez la date au format AAAA-MM-JJ.")
                        return
                    MagasinCursor.execute(f"UPDATE `{table}` SET date = %s WHERE transaction_id = %s",
                                        (new_value, transaction_id))
                elif field in ["montant_vendu", "montant_acheté"]: # Valide le montant et met à jour le montant de la transaction
                    amount = int(new_value)
                    if amount < 0:
                        messagebox.showerror("Montant invalide", "Le montant ne peut pas être négatif.")
                        return
                    elif field == "montant_vendu" :
                        MagasinCursor.execute(f"UPDATE `{table}` SET amount_sold = %s WHERE transaction_id = %s",
                                        (amount, transaction_id))
                    elif field == "montant_vendu" :
                        MagasinCursor.execute(f"UPDATE `{table}` SET amount_purchased = %s WHERE transaction_id = %s",
                                        (amount, transaction_id))
                elif field == "rabais": # Valide le pourcentage de remise et met à jour la remise de transaction
                    discount = float(new_value)
                    if discount < 0 or discount > 100: # Vérifie si la remise est comprise entre 0 et 100
                        messagebox.showerror("Remise invalide", "La remise doit être comprise entre 0 et 100.")
                        return
                    MagasinCursor.execute(f"SELECT amount_sold, amount_purchased, selling_price, buying_price FROM `{table}` WHERE transaction_id = %s",
                                        (transaction_id,))
                    row = MagasinCursor.fetchone()
                    MagasinCursor.execute(f"SELECT item_no FROM `{table}` WHERE transaction_id = %s", (transaction_id,))
                    item_no = MagasinCursor.fetchone()['item_no'] # type: ignore
                    MagasinCursor.execute(f"SELECT retail_sales_price, cost_price FROM `{shop}` WHERE item_no = %s", (int(item_no),)) # type: ignore
                    base = MagasinCursor.fetchone()
                    if row["amount_sold"] > 0: # type: ignore
                        new_selling_price = float(base["retail_sales_price"]) * (1 - (discount / 100)) # type: ignore
                        MagasinCursor.execute(f"UPDATE `{table}` SET discount = %s, selling_price = %s WHERE transaction_id = %s", (discount, new_selling_price, transaction_id))
                    elif row["amount_purchased"] > 0: # type: ignore
                        new_buying_price = float(base["cost_price"]) * (1 - (discount / 100)) # type: ignore
                        MagasinCursor.execute(f"UPDATE `{table}` SET discount = %s, buying_price = %s WHERE transaction_id = %s", (discount, new_buying_price, transaction_id))
                    else: # Si la transaction n'a aucun article vendu ou acheté, elle met simplement à jour la remise
                        MagasinCursor.execute(f"UPDATE `{table}` SET discount = %s WHERE transaction_id = %s",
                                            (discount, transaction_id))
                else: # Si le champ n'est pas pris en charge, un message d'erreur s'affiche
                    messagebox.showerror("Champ invalide", "Champ non pris en charge.")
                    return
                MagasinConnect.commit()
                messagebox.showinfo("Succès", "Transaction mise à jour avec succès.")
                main_menu(shop)
            except Exception as e:
                messagebox.showerror("Erreur", f"Échoué : {e}")
        ctk.CTkButton(app, text="Soumettre Modifier", command=submit_edit_transaction).pack(pady=8)
        ctk.CTkButton(bottom_frame, text="Retour au menu", command=lambda: main_menu(shop)).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Changer de Thème", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran d'édition de transaction : {e}")
        messagebox.showerror("Modifier l'erreur de transaction", f"Erreur dans l'écran d'édition de transaction : {e}")

def option_selected(option): # Fonction permettant de gérer l'option sélectionnée par l'utilisateur dans le menu principal
    try:
        if option == 1:
            add_item_screen()
        elif option == 2:
            add_transaction_screen()
        elif option == 3:
            total_profit_loss_screen()
        elif option == 4:
            profit_loss_date_range_screen()
        elif option == 5:
            view_items_screen()
        elif option == 6:
            view_transactions_screen()
        elif option == 7:
            edit_item_screen()
        elif option == 8:
            edit_transaction_screen()
        elif option == 9:
            login_screen()
        else:
            messagebox.showerror("Erreur", "Option non valide sélectionnée.")
            main_menu(shop_name.get().strip())
    except Exception as e:
        print(f" ❌ Erreur dans la sélection des options : {e}")
        messagebox.showerror("Erreur de sélection d'option", f"Erreur dans la sélection des options : {e}")

def login_screen(): # Fonction pour afficher l'écran de connexion
    try:
        clear_screen()
        
        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Magasin Connect", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        ctk.CTkLabel(app, text="Nom de la boutique (uniquement des lettres, des chiffres et un trait de soulignement) :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Nom de la boutique", textvariable=shop_name).pack(pady=10)
        ctk.CTkLabel(app, text="Mot de Passe :", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Mot de Passe", show="*", textvariable=passwrd).pack(pady=10)
        ctk.CTkButton(app, text="Se connecter", command=login).pack(pady=5)
        ctk.CTkButton(app, text="Registre", command=register).pack()
        ctk.CTkButton(bottom_frame, text="Changer de thème", command=change_theme).pack(side='right', pady=5)
        ctk.CTkButton(bottom_frame, text="Sortie", command=app.quit).pack(side='left', pady=5)
    except Exception as e:
        print(f" ❌ Erreur dans l'écran de connexion : {e}")
        messagebox.showerror("Erreur d'écran de connexion", f"Erreur dans l'écran de connexion : {e}")

login_screen()
app.mainloop()
