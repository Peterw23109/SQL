import sqlite3
db = sqlite3.connect('internal.db')


def print_all():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat;'
    cursor.execute(sql)
    result = cursor.fetchall()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()


def print_legend_rare():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Rarity = "Legend Rare";'
    cursor.execute(sql)
    result = cursor.fetchall()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()


def print_against():
    against = input("What type is your cat good against? ").title()
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Against = ?;'
    cursor.execute(sql, (against,))
    result = cursor.fetchall()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()


def this_does_everything():
    Rarity = input("What rarity is your cat?").title()
    against = input("What type is your cat good against? ").title()
    Banner = input("What banner is your cat from?").title()
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Rarity = ? AND Cat_against = ? AND Banner = ?;'
    cursor.execute(sql, (Rarity, against, Banner))
    result = cursor.fetchall()
    print(f"The type is {against}")
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[3]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()


while True:
    print("\nWhat would you like to do?")
    print("1. Display all data")
    print("2. Display Legend Rare cats")
    print("3. Certin type")
    print("4. This does everything")
    print("5. Exit")
    user_input = input("Enter a number (1-5): ")

    if user_input == "1":
        print_all()
    elif user_input == "2":
        print_legend_rare()
    elif user_input == "3":
        print_against()
    elif user_input == "4":
        this_does_everything()
    elif user_input == "5":
        print("Exiting the program.")
        break
    
    else:
        print("That was not an option.")