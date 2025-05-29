import sqlite3
db = sqlite3.connect('internal.db')
Trait = ["Red", "Alien", "Black", "Traitless", "Non-Metal", "Floating", "Angel", "All", "Metal", "Zombies", "Aku"]
Rarity_Type = ["Legend Rare", "Uber Rare"]

#Function that print every data


def print_header():
    print(f"\n{'Name':<25}{'Type':<15}{'Rarity':<15}{'AOE attack':<15}{'Single Attack':<15}{'Banner':<15}")
    print("-" * 100)


def print_all():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat;'
    cursor.execute(sql)
    result = cursor.fetchall()
    print_header()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()

#Function that print Legend Rare only
"""
def print_legend_rare():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Rarity = "Legend Rare";'
    cursor.execute(sql)
    result = cursor.fetchall()
    print_header()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()
"""
#Function that ask the user and display the type 
"""r
def print_against():
    against = input("What type is your cat good against? ").title()
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Against = ?;'
    cursor.execute(sql, (against,))
    result = cursor.fetchall()
    print_header()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()
"""
#Fuction that ask the user rarity, against and banner.
def Rarirty_and_type():
    while True:
        Rarity = input("What rarity is your cat? ").title()
        if Rarity in Rarity_Type:
            break
        else:
            print("Invalid rarity. Please try again.")

    while True:
        against = input("What type is your cat good against? ").title()
        if against in Trait:
            break
        else:
            print("Invalid trait. Please try again.")
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Rarity = ? AND Cat_against = ?;'
    cursor.execute(sql, (Rarity, against))
    result = cursor.fetchall()
    print_header()
    for Cat in result:
        print(f"\n{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()

def search():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Name = ?;'

    while True:
        user_cat = input("Cat name: ").title()
        cursor.execute(sql, (user_cat,))
        result = cursor.fetchall()

        if result:
            print_header()
            for cat in result:
                print(f"{cat[0]:<25}{cat[1]:<15}{cat[2]:<15}{cat[3]:<15}{cat[4]:<15}{cat[5]:<15}")
            break  
        else:
            print("No cat found with that name. Please try again.")
    
    db.close()
while True:
    #A menu that display what to do
    print("1. Display all data")
    print("2. Sort data by rarity and type")
    print("3. Search for cat's data")
    print("4. Exit")
    user_input = input("Enter a number (1-3): ")
    if user_input == "1":
        print_all()
    elif user_input == "2":
        Rarirty_and_type()
    elif user_input == "3":
        search()
    elif user_input == "4":
        print("Exiting the program.")
        break
    else:
        print("That was not an option.")