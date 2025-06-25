import mysql.connector as SQL # You may need to install this module by running pip install mysql-connector-python in terminal
import bcrypt # You may need to install this module by running pip install bcrypt in terminal
import customtkinter as ctk # You may need to install this module by running pip install customtkinter in terminal
from tkinter import messagebox # This module comes preinstalled with Python
from datetime import datetime # For date validation
import re

def is_valid_shop_name(name):
    return re.match(r'^[A-Za-z0-9_]+$', name) is not None

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def hash_password(password):  # Converts a password from String to Hash
    try:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    except Exception as e:
        print(f" ❌ Error hashing password: {e}")
        messagebox.showerror("Hashing Error", f"Error hashing password: {e}")
        return None

def check_password(password, hashed): # Matches password with the hashed one in the Database
    try:
        return bcrypt.checkpw(password.encode(), hashed)
    except Exception as e:
        print(f" ❌ Error checking password: {e}")
        messagebox.showerror("Checking Error", f"Error checking password: {e}")
        return False

MagasinConnect = SQL.connect(
    host="localhost", # Enter your MySQL Host here (localhost by default)
    user="root", # Enter your MySQL user name here (root by default)
    password="your password", # Enter your MySQL password here (made during setup)
    database="magasin_connect" # Create a MySQL database and enter its name here
)

if MagasinConnect.is_connected(): # Checks if connector object is successfuly connected to MySQL databse
    print(" ✅ Successfully connected to the database")
else:
    print(" ❌ Failed to connect to the database")

MagasinCursor = MagasinConnect.cursor(dictionary=True) # Dictionary = True lets it return rows in the form of a dictionary

def DataIntable(name): # Extracts all data present in a given table
    try:
        MagasinCursor.execute(f'SELECT * FROM `{name}`')
        rows = MagasinCursor.fetchall()
        return rows
    except SQL.Error as e:
        print(f" ❌ Error fetching data from table {name}: {e}")
        messagebox.showerror("Database Error", f"Error fetching data from table {name}: {e}")
        return {}
    
def IfTableExists(Nom): # Checks whether the table exists in the MySQL database
    try:
        MagasinCursor.execute(f'''SELECT COUNT(*) 
                            FROM information_schema.tables 
                            WHERE table_schema = 'magasin_connect'
                            AND table_name = '{Nom}' ''')
        if MagasinCursor.fetchone()[0] == 1: # type: ignore
            print(f" ✅ Table {Nom} already exists")
            return True
        else:
            print(f" ❌ Table {Nom} does not exist")
            return False
    except Exception as e:
        print(f" ❌ Error checking if table {Nom} exists: {e}")
        messagebox.showerror("Database Error", f"Error checking if table {Nom} exists: {e}")
        return False

def NouvMagasinTable(Nom): # Creates a set of 2 tables for the shop namely, <shop name> and <shop name>_transactions, the later being a child table connected through the foreign key attribute
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
            print(f" ✅ Table {Nom} created successfully")
        else :
            print(" ❌ Can't create a table named shops, please choose another name.")
            messagebox.showerror("Name Error","Shop name can't be shops ! Please try again with a different name.")
            login_screen()
    except SQL.Error as e:
        print(f" ❌ Error creating table: {e}")
        messagebox.showerror("Database Error", f"Error creating table {Nom}: {e}")
        MagasinConnect.rollback()

def MagasinTableFill(name, item_name, cost_price, retail_sales_price, stock_number): # Fills data in one row of the <shop name> table
    try :
        MagasinCursor.execute(f'''INSERT INTO `{name}` 
            (item_name, cost_price, retail_sales_price, stock_number) 
            VALUES (%s, %s, %s, %s)''', (item_name, cost_price, retail_sales_price, stock_number))
        MagasinConnect.commit()
        print(f" ✅ Item {item_name} added successfully to the table")
    except SQL.Error as e:
        print(f" ❌ Error adding item to table {name}: {e}")
        messagebox.showerror("Database Error", f"Error adding item to table {name}: {e}")
        MagasinConnect.rollback()
    
def MagasinTableEdit(name, item_no, item_name=None, cost_price=None, retail_sales_price=None, stock_number=None): # Edits data present in one of the rows of the <shop name> table
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
            print(f" ✅ Item no. {item_no} updated successfully in the table")
        else:
            print(" ❌ No fields to update")
        MagasinConnect.commit()
    except Exception as e:
        print(f" ❌ Error updating item in table {name}: {e}")
        messagebox.showerror("Database Error", f"Error updating item in table {name}: {e}")
        MagasinConnect.rollback()

def MagasinTransactionTableEdit(name, transaction_id, item_name=None, date=None, amount_sold=None, amount_purchased=None, discount=None, selling_price=None, buying_price=None): # Edits data present in one of the rows of the <shop name>_transactions table
    try:
        updates = []
        if item_name is not None:
            updates.append(f"item_name = '{item_name}'")
        if date is not None:
            if date.strip() == '':
                print(" ❌ Date cannot be empty.")
                messagebox.showerror("Error", "Date cannot be empty.")
                return
            elif not is_valid_date(date):
                print(" ❌ Invalid date format. Use YYYY-MM-DD.")
                messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
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
            print(f" ✅ Transaction for transaction id {transaction_id} updated successfully in the transactions table")
        else:
            print(" ❌ No fields to update")
        MagasinConnect.commit()
    except Exception as e:
        print(f" ❌ Error updating transaction in table {name}_transactions: {e}")
        messagebox.showerror("Database Error", f"Error updating transaction in table {name}_transactions: {e}")
        MagasinConnect.rollback()

def MagasinTransactionFill(name, no, itemname, date, amount_sold, amount_purchased, discount, selling_price, buying_price): # Fills data in one row of the <shop name>_transactions table
    try :
        MagasinCursor.execute(
            f'''INSERT INTO `{name}_transactions` 
            (item_no, item_name, date, amount_sold, amount_purchased, discount, selling_price, buying_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
            (no, itemname, date, amount_sold, amount_purchased, discount, selling_price, buying_price)
        )
        if amount_sold < 0 or amount_purchased < 0: # If either amount sold or amount purchased is negative, it prompts the user to try again
            print(" ❌ Amount sold or purchased cannot be negative")
            messagebox.showerror("Error", "Amount sold or purchased cannot be negative.")
            MagasinConnect.rollback()
            return
        elif amount_sold < 0 and amount_purchased > 0: # If amount sold is negative and amount purchased is positive, it prompts the user to try again
            print(" ❌ You cannot sell a negative amount of an item")
            messagebox.showerror("Error", "You cannot sell a negative amount of an item.")
            MagasinConnect.rollback()
            return
        elif amount_purchased < 0 and amount_sold > 0: # If amount purchased is negative and amount sold is positive, it prompts the user to try again
            print(" ❌ You cannot purchase a negative amount of an item")
            messagebox.showerror("Error", "You cannot purchase a negative amount of an item.")
            MagasinConnect.rollback()
        elif amount_sold > 0 and amount_purchased > 0: # If both amount sold and amount purchased are greater than 0, it prompts the user to try again
            print(" ❌ You cannot sell and purchase the same item at the same time")
            messagebox.showerror("Error", "You cannot sell and purchase the same item at the same time.")
            MagasinConnect.rollback()
        elif amount_sold < 0 and amount_purchased == 0: # If amount sold is negative and amount purchased is 0, it prompts the user to try again
            print(" ❌ You cannot sell a negative amount of an item")
            messagebox.showerror("Error", "You cannot sell a negative amount of an item.")
            MagasinConnect.rollback()
            return
        elif amount_purchased < 0 and amount_sold == 0: # If amount purchased is negative and amount sold is 0, it prompts the user to try again
            print(" ❌ You cannot purchase a negative amount of an item")
            messagebox.showerror("Error", "You cannot purchase a negative amount of an item.")
            MagasinConnect.rollback()
            return
        elif amount_sold > 0 and amount_purchased == 0: # If amount sold is greater than 0 and amount purchased is 0, it updates the stock number in the shop table
            MagasinCursor.execute(
                f"UPDATE `{name}` SET stock_number = stock_number - %s WHERE item_no = %s", (amount_sold, no))
        elif amount_purchased > 0 and amount_sold == 0: # If amount purchased is greater than 0 and amount sold is 0, it updates the stock number in the shop table
            MagasinCursor.execute(
                f"UPDATE `{name}` SET stock_number = stock_number + %s WHERE item_no = %s", (amount_purchased, no))
        MagasinConnect.commit()
        print(f" ✅ Transaction for item no. {no} added successfully to the transactions table")
    except SQL.Error as e:
        print(f" ❌ Error adding transaction to table {name}_transactions: {e}")
        messagebox.showerror("Database Error", f"Error adding transaction to table {name}_transactions: {e}")
        MagasinConnect.rollback()

def CréerCompteMagasin(shop_name, password): # Creates a row with the name of the shop and password in the shops table to later verify the password
    try:
        MagasinCursor.execute('''CREATE TABLE IF NOT EXISTS shops (
            shop_name VARCHAR(255) PRIMARY KEY,
            password_hash BLOB NOT NULL)''')
        hashed = hash_password(password)
        MagasinCursor.execute("INSERT INTO shops (shop_name, password_hash) VALUES (%s, %s)", (shop_name, hashed))
        MagasinConnect.commit()
    except SQL.Error as e:
        print(f" ❌ Error creating shop account: {e}")
        messagebox.showerror("Database Error", f"Error creating shop account: {e}")
        MagasinConnect.rollback()
    except Exception as e:
        print(f" ❌ Error creating shop account: {e}")
        messagebox.showerror("Database Error", f"Error creating shop account: {e}")
        MagasinConnect.rollback()

def VérifierMagasinMdP(shop_name, password): # Verifies the password entered by the user to the one present in the table shops in the database
    try:
        MagasinCursor.execute("SELECT password_hash FROM shops WHERE shop_name = %s", (shop_name,))
        row = MagasinCursor.fetchone()
        if row and check_password(password, row['password_hash']): # type: ignore
            return True
        else:
            return False
    except SQL.Error as e:
        print(f" ❌ Error verifying shop password: {e}")
        messagebox.showerror("Database Error", f"Error verifying shop password: {e}")
        return False
    except Exception as e:
        print(f" ❌ Error verifying shop password: {e}")
        messagebox.showerror("Database Error", f"Error verifying shop password: {e}")
        return False

ctk.set_appearance_mode("system") # Sets the appearance mode to system default (light or dark based on system settings)
ctk.set_default_color_theme("C:/Users/username/Desktop/pastel_theme.json") # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system

app = ctk.CTk() # Creates the main application window using customtkinter
app.title("Magasin Connect 🛍️") # Sets the application window title
app.geometry("900x700") # Sets the initial size of the window
app.resizable(width=True, height=True) # Allows the window to be resizable

shop_name = ctk.StringVar() # Variable to store the shop name entered by the user
passwrd = ctk.StringVar() # Variable to store the password entered by the user

def change_theme(): # Function to toggle between light and dark themes
    try:
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")
    except Exception as e:
        print(f" ❌ Error changing theme: {e}")
        messagebox.showerror("Theme Error", f"Error changing theme: {e}")

def clear_screen(): # Function to clear the current screen by destroying all widgets in the main application window
    try:
        for widget in app.winfo_children():
            widget.destroy()
    except Exception as e:
        print(f" ❌ Error clearing screen: {e}")
        messagebox.showerror("Screen Error", f"Error clearing screen: {e}")

def login(): # Function to handle user login
    try:
        MagasinCursor.execute('''CREATE TABLE IF NOT EXISTS shops (
            shop_name VARCHAR(255) PRIMARY KEY,
            password_hash BLOB NOT NULL)''')
        name = shop_name.get().strip()
        pwd = passwrd.get().strip()

        if not name or not pwd: # Checks if both fields are filled
            messagebox.showerror("Error", "Please enter both fields.")
            return
        MagasinCursor.execute("SELECT shop_name FROM shops WHERE shop_name = %s", (name,))
        shop_exists = MagasinCursor.fetchone() # Checks if the shop exists in the database
        if not shop_exists:
            messagebox.showerror("Not Found", "Shop not registered. Please register first.")
            return
        if not VérifierMagasinMdP(name, pwd): # Verifies the password entered by the user
            messagebox.showerror("Error", "Incorrect password.")
            return
        MagasinCursor.execute(f'''SELECT COUNT(*) as count FROM information_schema.tables 
                                WHERE table_schema = 'magasin_connect' 
                                AND table_name = %s''', (name,)) # Checks if the shop's main table exists
        items_table = MagasinCursor.fetchone()['count'] # type: ignore
        MagasinCursor.execute(f'''SELECT COUNT(*) as count FROM information_schema.tables 
                                WHERE table_schema = 'magasin_connect' 
                                AND table_name = %s''', (name + "_transactions",)) # Checks if the shop's transactions table exists
        transactions_table = MagasinCursor.fetchone()['count'] # type: ignore
        if items_table != 1 or transactions_table != 1: # If either of the tables is missing, it indicates corruption
            MagasinCursor.execute("DELETE FROM shops WHERE shop_name = %s", (name,))
            MagasinConnect.commit()
            messagebox.showerror(
                "Corrupted Shop",
                f"Shop '{name}' had missing data tables.\n It has been removed.\nPlease register again."
            )
            return
        messagebox.showinfo("Success", f"Welcome back to {name}!")
        main_menu(name)
    except SQL.Error as e:
        print(f" ❌ Error during login: {e}")
        messagebox.showerror("Login Error", f"Error during login: {e}")
    except Exception as e:
        print(f" ❌ Error during login: {e}")
        messagebox.showerror("Login Error", f"Error during login: {e}")

def register(): # Function to handle user registration
    try:
        MagasinCursor.execute('''CREATE TABLE IF NOT EXISTS shops (
            shop_name VARCHAR(255) PRIMARY KEY,
            password_hash BLOB NOT NULL)''')
        name = shop_name.get().strip()
        pwd = passwrd.get().strip()
        if name.lower() == 'shops': # Prevents the user from registering a shop with the name 'shops'
            messagebox.showerror("Name Error", "Shop name can't be 'shops'! Please try again with a different name.")
            return
        elif not is_valid_shop_name(name):
            messagebox.showerror("Name Error", "Shop name can only contain letters, numbers, and underscores!")
            return
        elif not name or not pwd:
            messagebox.showerror("Error", "Please fill both fields.")
            return
        MagasinCursor.execute("SELECT shop_name FROM shops WHERE shop_name = %s", (name,))
        if MagasinCursor.fetchone(): # Checks if the shop already exists in the database
            messagebox.showwarning("Exists", "Shop already exists. Try logging in.")
        else:
            CréerCompteMagasin(name, pwd) # Creates a new shop account with the given name and password
            NouvMagasinTable(name) # Creates the main table and transactions table for the new shop
            messagebox.showinfo("Registered", f"Shop '{name}' registered.")
            main_menu(name) # Redirects to the main menu after successful registration
    except SQL.Error as e:
        print(f" ❌ Error during registration: {e}")
        messagebox.showerror("Registration Error", f"Error during registration: {e}")
    except Exception as e:
        print(f" ❌ Error during registration: {e}")
        messagebox.showerror("Registration Error", f"Error during registration: {e}")

def main_menu(name): # Function to display the main menu after successful login or registration
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text=f"Welcome to {name}!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        options = [
            "Add Item", "Add Transaction", "Total Profit/Loss",
            "Profit/Loss in Date Range", "View Items", "View Transactions",
            "Edit Item", "Edit Transaction", "Logout"
        ] # List of options for the main menu
        for idx, opt in enumerate(options, 1):
            ctk.CTkButton(app, text=f"{idx}. {opt}", command=lambda i=idx: option_selected(i)).pack(pady=4) # Creates buttons for each option in the main menu
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in main menu: {e}")
        messagebox.showerror("Menu Error", f"Error in main menu: {e}")

def add_item_screen(): # Function to display the screen for adding a new item to the shop
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Add Item", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        item_name = ctk.StringVar()
        cost_price = ctk.DoubleVar()
        retail_sales_price = ctk.DoubleVar()
        stock_number = ctk.IntVar()

        ctk.CTkLabel(app, text="Item Name:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Item Name", textvariable=item_name).pack(pady=5)
        ctk.CTkLabel(app, text="Cost Price:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Cost Price", textvariable=cost_price).pack(pady=5)
        ctk.CTkLabel(app, text="Retail Sales Price:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Retail Sales Price", textvariable=retail_sales_price).pack(pady=5)
        ctk.CTkLabel(app, text="Stock Number:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Stock Number", textvariable=stock_number).pack(pady=5)

        def add_item(): # Function to handle adding a new item to the shop
            if item_name.get() and cost_price.get() >= 0 and retail_sales_price.get() >= 0 and stock_number.get() >= 0: # Checks if all fields are filled correctly
                MagasinTableFill(shop_name.get().strip(), item_name.get(), cost_price.get(), retail_sales_price.get(), stock_number.get())
                messagebox.showinfo("Success", "Item added successfully.")
                main_menu(shop_name.get().strip())
            else: # If any field is not filled correctly, it shows an error message
                messagebox.showerror("Error", "Please fill all fields correctly.")
                main_menu(shop_name.get().strip())

        ctk.CTkButton(app, text="Add Item", command=add_item).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back to Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in add item screen: {e}")
        messagebox.showerror("Add Item Error", f"Error in add item screen: {e}")

def add_transaction_screen(): # Function to display the screen for adding a new transaction to the shop
    try :
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Add Transaction", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        rows = DataIntable(shop_name.get().strip()) # Fetches all items from the shop's main table
        if not rows: # If there are no items in the shop, it shows an error message and redirects to the main menu
            messagebox.showerror("Error", "No items found in the shop. Please add items first.")
            main_menu(shop_name.get().strip())
            return
        item_options = [f"{row['item_no']} - {row['item_name']}" for row in rows] # type: ignore

        ctk.CTkLabel(app, text="\n".join(item_options), font=ctk.CTkFont(size=12)).pack(pady=10) # Displays the list of items in the shop

        item_no = ctk.IntVar()
        item_name = ctk.StringVar()
        date = ctk.StringVar()
        amount_sold = ctk.IntVar()
        amount_purchased = ctk.IntVar()
        discount = ctk.DoubleVar()
        selling_price = ctk.DoubleVar()
        buying_price = ctk.DoubleVar()
        discount.set(0.0) # Sets the default discount to 0.0
        amount_purchased.set(0) # Sets the default amount purchased to 0
        amount_sold.set(0) # Sets the default amount sold to 0

        ctk.CTkLabel(app, text="Item No (See from the List above):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Item No", textvariable=item_no).pack(pady=5)
        ctk.CTkLabel(app, text="Date (YYYY-MM-DD):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Date (YYYY-MM-DD)", textvariable=date).pack(pady=5)
        ctk.CTkLabel(app, text="Amount Sold:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Amount Sold", textvariable=amount_sold).pack(pady=5)
        ctk.CTkLabel(app, text="Amount Purchased:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Amount Purchased", textvariable=amount_purchased).pack(pady=5)
        ctk.CTkLabel(app, text="Discount (%):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Discount (%)", textvariable=discount).pack(pady=5)
        def add_transaction(): # Function to handle adding a new transaction to the shop
            for row in rows: # Populates the item name field based on the selected item number
                if row['item_no'] == item_no.get(): # type: ignore
                    item_name.set(row['item_name']) # type: ignore
                    selling_price.set(float(row['retail_sales_price']) * (100 - discount.get())/100) # type: ignore
                    buying_price.set(float(row['cost_price']) - (float(row['cost_price']) * discount.get()/100)) # type: ignore
            if amount_purchased.get() < 0: # If the amount purchased is negative, it shows an error message
                print(" ❌ Amount purchased cannot be negative")
                messagebox.showerror("Error", "Amount purchased cannot be negative.")
                return
            elif amount_sold.get() < 0: # If the amount sold is negative, it shows an error message
                print(" ❌ Amount sold cannot be negative")
                messagebox.showerror("Error", "Amount sold cannot be negative.")
                return
            elif amount_purchased.get() == 0 and amount_sold.get() == 0: # If both amounts are zero, it shows an error message
                print(" ❌ Please enter either amount sold or amount purchased.")
                messagebox.showerror("Error", "Please enter either amount sold or amount purchased.")
                return
            elif amount_sold.get() > 0 and amount_purchased.get() > 0: # If both amounts are greater than zero, it shows an error message
                print(" ❌ Please enter either amount sold or amount purchased, not both.")
                messagebox.showerror("Error", "Please enter either amount sold or amount purchased, not both.")
                return
            elif date.get().strip() == '' :
                print(" ❌ Please enter a date.")
                messagebox.showerror("Error", "Please enter a date.")
                return
            elif date.get().strip() == '':
                print(" ❌ Date field can't be empty. Fill it.")
                messagebox.showerror("Error", "Date field can't be empty. Fill it.")
                return
            elif not is_valid_date(date.get().strip()): # If the date is not in valid format, it shows an error message
                print(" ❌ Invalid date format or date. Use YYYY-MM-DD.")
                messagebox.showerror("Error", "Invalid date format or date. Use YYYY-MM-DD.")
                return
            elif (item_no.get() > 0 and
                discount.get() >= 0.0 and
                discount.get() < 100.0 and
                item_name.get().strip() != ""): # Checks if all fields are filled correctly
                MagasinTransactionFill(shop_name.get().strip(), item_no.get(), item_name.get(), date.get(),
                                    amount_sold.get(), amount_purchased.get(), discount.get(),
                                    selling_price.get(), buying_price.get())
                messagebox.showinfo("Success", "Transaction added successfully.")
                main_menu(shop_name.get().strip())
            else: # If any field is not filled correctly, it shows an error message
                messagebox.showerror("Error", "Please fill all fields correctly.")
                main_menu(shop_name.get().strip())
        ctk.CTkButton(app, text="Add Transaction", command=add_transaction).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back to Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in add transaction screen: {e}")
        messagebox.showerror("Add Transaction Error", f"Error in add transaction screen: {e}")

def total_profit_loss_screen(): # Function to display the total profit/loss screen
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Total Profit/Loss", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        MagasinCursor.execute(f'''SELECT SUM(selling_price * amount_sold) - SUM(buying_price * amount_purchased) AS total_profit_loss
                                FROM `{shop_name.get().strip()}_transactions`''')
        result = MagasinCursor.fetchone() # Fetches the total profit/loss from the transactions table
        total_profit_loss = result['total_profit_loss'] if result['total_profit_loss'] is not None else 0 # type: ignore
        ctk.CTkLabel(app, text=f"Total Profit/Loss: {total_profit_loss:.2f}").pack(pady=10) # Displays the total profit/loss calculated from the transactions table
        ctk.CTkButton(bottom_frame, text="Back to Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in total profit/loss screen: {e}")
        messagebox.showerror("Profit/Loss Error", f"Error in total profit/loss screen: {e}")

def profit_loss_date_range_screen(): # Function to display the profit/loss in a specific date range screen
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Profit/Loss in Date Range", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        start_date = ctk.StringVar()
        end_date = ctk.StringVar()
        ctk.CTkLabel(app, text="Start Date (YYYY-MM-DD):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Start Date (YYYY-MM-DD)", textvariable=start_date).pack(pady=5)
        ctk.CTkLabel(app, text="End Date (YYYY-MM-DD):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="End Date (YYYY-MM-DD)", textvariable=end_date).pack(pady=5)
        def calculate_profit_loss(): # Function to calculate profit/loss in the specified date range
            if start_date.get().strip() == "" or end_date.get().strip() == "": # If either date field is empty, it shows an error message
                messagebox.showerror("Error", "Please fill both date fields.")
                main_menu(shop_name.get().strip())
            elif not is_valid_date(start_date.get().strip()) or not is_valid_date(end_date.get().strip()): # If either date field is not in valid format, it shows an error message
                messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
                main_menu(shop_name.get().strip())
            elif is_valid_date(start_date.get().strip()) and is_valid_date(end_date.get().strip()): # Checks if both date fields are filled
                MagasinCursor.execute(f'''SELECT SUM(selling_price * amount_sold) - SUM(buying_price * amount_purchased) AS profit_loss
                                        FROM `{shop_name.get().strip()}_transactions`
                                        WHERE date BETWEEN '{start_date.get()}' AND '{end_date.get()}' ''')
                result = MagasinCursor.fetchone()
                profit_loss = result['profit_loss'] if result['profit_loss'] is not None else 0 # type: ignore
                messagebox.showinfo("Profit/Loss", f"Profit/Loss from {start_date.get()} to {end_date.get()}: {profit_loss:.2f}")
            else: # If either date field is not filled, it shows an error message
                messagebox.showerror("Error", "Please fill both date fields.")
                main_menu(shop_name.get().strip())
        ctk.CTkButton(app, text="Calculate Profit/Loss", command=calculate_profit_loss).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back to Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in profit/loss date range screen: {e}")
        messagebox.showerror("Profit/Loss Date Range Error", f"Error in profit/loss date range screen: {e}")

def view_items_screen(): # Function to display the view items screen
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="View Items", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        items = DataIntable(shop_name.get().strip())
        if not items: # If there are no items in the shop, it shows an error message
            ctk.CTkLabel(app, text="No items found.").pack(pady=10)
        else: # If there are items, it displays them in a list format
            for item in items:
                ctk.CTkLabel(app, text=f"Item No: {item['item_no']}, Name: {item['item_name']}, " # type: ignore
                                    f"Cost Price: {item['cost_price']}, Retail Price: {item['retail_sales_price']}, " # type: ignore
                                    f"Stock: {item['stock_number']}").pack(pady=5) # type: ignore
        ctk.CTkButton(bottom_frame, text="Back to Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in view items screen: {e}")
        messagebox.showerror("View Items Error", f"Error in view items screen: {e}")

def view_transactions_screen(): # Function to display the view transactions screen
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="View Transactions", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        transactions = DataIntable(f"{shop_name.get().strip()}_transactions")
        if not transactions: # If there are no transactions in the shop, it shows an error message
            ctk.CTkLabel(app, text="No transactions found.").pack(pady=10)
        else: # If there are transactions, it displays them in a list format
            for transaction in transactions:
                ctk.CTkLabel(app, text=f"Transaction ID: {transaction['transaction_id']}, Item No: {transaction['item_no']}, " # type: ignore
                                    f"Name: {transaction['item_name']}, Date: {transaction['date']}, " # type: ignore
                                    f"Sold: {transaction['amount_sold']}, Purchased: {transaction['amount_purchased']}, " # type: ignore
                                    f"Discount: {transaction['discount']}, Selling Price: {transaction['selling_price']}, " # type: ignore
                                    f"Buying Price: {transaction['buying_price']}").pack(pady=5) # type: ignore
        ctk.CTkButton(bottom_frame, text="Back to Menu", command=lambda: main_menu(shop_name.get().strip())).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in view transactions screen: {e}")
        messagebox.showerror("View Transactions Error", f"Error in view transactions screen: {e}")

def edit_item_screen(): # Function to display the screen for editing an existing item in the shop
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        shop = shop_name.get()
        ctk.CTkLabel(app, text="Edit Item", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        MagasinCursor.execute(f"SELECT item_no, item_name FROM `{shop}`")
        items = MagasinCursor.fetchall()
        if not items: # If there are no items in the shop, it shows an error message and redirects to the main menu
            messagebox.showinfo("Empty", "No items found in the shop.")
            main_menu(shop)
            return
        item_options = [f"{item['item_no']} - {item['item_name']}" for item in items] # type: ignore
        selected_item = ctk.StringVar(value=item_options[0])
        ctk.CTkOptionMenu(app, values=item_options, variable=selected_item).pack(pady=5)
        field_var = ctk.StringVar(value="item_name")
        value_var = ctk.StringVar()
        ctk.CTkOptionMenu(app, values=["item_name", "cost_price", "retail_sales_price"], variable=field_var).pack(pady=5)
        ctk.CTkLabel(app, text="Enter new value:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="New Value", textvariable=value_var).pack(pady=5)

        def submit_edit(): # Function to handle submitting the edit for the selected item
            selection = selected_item.get().split(" - ")[0]
            item_no = int(selection)
            field = field_var.get()
            new_value = value_var.get().strip()
            if not new_value: # Checks if the new value is provided
                messagebox.showerror("Error", "Please enter a new value.")
                return
            try:
                if field == "item_name":
                    MagasinCursor.execute(f"UPDATE `{shop}` SET item_name = %s WHERE item_no = %s", (new_value, item_no))
                elif field == "cost_price":
                    MagasinCursor.execute(f"UPDATE `{shop}` SET cost_price = %s WHERE item_no = %s", (float(new_value), item_no))
                elif field == "retail_sales_price":
                    MagasinCursor.execute(f"UPDATE `{shop}` SET retail_sales_price = %s WHERE item_no = %s", (float(new_value), item_no))
                else:
                    messagebox.showerror("Invalid Field", "Unsupported field selected.")
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update: {e}")
                return
            MagasinConnect.commit()
            messagebox.showinfo("Success", f"Item {item_no} updated successfully.")
            main_menu(shop)
        ctk.CTkButton(app, text="Submit Edit", command=submit_edit).pack(pady=8)
        ctk.CTkButton(bottom_frame, text="Back", command=lambda: main_menu(shop)).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in edit item screen: {e}")
        messagebox.showerror("Edit Item Error", f"Error in edit item screen: {e}")

def edit_transaction_screen(): # Function to display the screen for editing an existing transaction in the shop
    try:
        clear_screen()

        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        shop = shop_name.get()
        table = f"{shop}_transactions"
        ctk.CTkLabel(app, text="Edit Transaction", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        MagasinCursor.execute(f"SELECT transaction_id, item_name FROM `{table}`")
        transactions = MagasinCursor.fetchall()
        if not transactions: # If there are no transactions in the shop, it shows an error message and redirects to the main menu
            messagebox.showinfo("Empty", "No transactions found.")
            main_menu(shop)
            return
        transaction_options = [f"{t['transaction_id']} - {t['item_name']}" for t in transactions] # type: ignore
        selected_transaction = ctk.StringVar(value=transaction_options[0])
        ctk.CTkOptionMenu(app, values=transaction_options, variable=selected_transaction).pack(pady=5)
        field_var = ctk.StringVar(value="item_name")
        value_var = ctk.StringVar()
        ctk.CTkOptionMenu(app, values=[
            "item_name", "date", "amount_sold", "amount_purchased", "discount"
        ], variable=field_var).pack(pady=5)
        ctk.CTkLabel(app, text="Enter new value:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="New Value", textvariable=value_var).pack(pady=5)

        def submit_edit_transaction(): # Function to handle submitting the edit for the selected transaction
            try:
                transaction_id = int(selected_transaction.get().split(" - ")[0])
                field = field_var.get()
                new_value = value_var.get().strip()
                if not new_value: # Checks if the new value is provided
                    messagebox.showerror("Error", "Please enter a new value.")
                    return
                elif field == "date": # Validates the date format and updates the transaction date
                    if not is_valid_date(new_value): # Validates the date format
                        messagebox.showerror("Invalid Date", "Enter date in YYYY-MM-DD format.")
                        return
                    MagasinCursor.execute(f"UPDATE `{table}` SET date = %s WHERE transaction_id = %s",
                                        (new_value, transaction_id))
                elif field in ["amount_sold", "amount_purchased"]: # Validates the amount and updates the transaction amount
                    amount = int(new_value)
                    if amount < 0:
                        messagebox.showerror("Invalid Amount", "Amount cannot be negative.")
                        return
                    MagasinCursor.execute(f"UPDATE `{table}` SET {field} = %s WHERE transaction_id = %s",
                                        (amount, transaction_id))
                elif field == "discount": # Validates the discount percentage and updates the transaction discount
                    discount = float(new_value)
                    if discount < 0 or discount > 100: # Checks if the discount is between 0 and 100
                        messagebox.showerror("Invalid Discount", "Discount must be between 0 and 100.")
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
                    else: # If the transaction has no items sold or purchased, it just updates the discount
                        MagasinCursor.execute(f"UPDATE `{table}` SET discount = %s WHERE transaction_id = %s",
                                            (discount, transaction_id))
                elif field == "item_name": # Updates the item name in the transaction
                    MagasinCursor.execute(f"UPDATE `{table}` SET item_name = %s WHERE transaction_id = %s",
                                        (new_value, transaction_id))
                else: # If the field is not supported, it shows an error message
                    messagebox.showerror("Invalid Field", "Unsupported field.")
                    return
                MagasinConnect.commit()
                messagebox.showinfo("Success", "Transaction updated successfully.")
                main_menu(shop)
            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
        ctk.CTkButton(app, text="Submit Edit", command=submit_edit_transaction).pack(pady=8)
        ctk.CTkButton(bottom_frame, text="Back", command=lambda: main_menu(shop)).pack(side='left')
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in edit transaction screen: {e}")
        messagebox.showerror("Edit Transaction Error", f"Error in edit transaction screen: {e}")

def option_selected(option): # Function to handle the option selected by the user in the main menu
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
            messagebox.showerror("Error", "Invalid option selected.")
            main_menu(shop_name.get().strip())
    except Exception as e:
        print(f" ❌ Error in option selection: {e}")
        messagebox.showerror("Option Selection Error", f"Error in option selection: {e}")

def login_screen(): # Function to display the login screen
    try:
        clear_screen()
        
        bottom_frame = ctk.CTkFrame(master=app)
        bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)

        ctk.CTkLabel(app, text="Magasin Connect", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        ctk.CTkLabel(app, text="Shop name (Only letters, numbers, and underscore):", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Shop Name", textvariable=shop_name).pack(pady=10)
        ctk.CTkLabel(app, text="Password:", font=ctk.CTkFont(size=12)).pack(pady=0)
        ctk.CTkEntry(app, placeholder_text="Password", show="*", textvariable=passwrd).pack(pady=10)
        ctk.CTkButton(app, text="Login", command=login).pack(pady=5)
        ctk.CTkButton(app, text="Register", command=register).pack()
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
        ctk.CTkButton(bottom_frame, text="Exit", command=app.quit).pack(side='left', pady=5)
    except Exception as e:
        print(f" ❌ Error in login screen: {e}")
        messagebox.showerror("Login Screen Error", f"Error in login screen: {e}")

login_screen()
app.mainloop()
