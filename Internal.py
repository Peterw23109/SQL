import sqlite3
db = sqlite3.connect('internal.db')
def print_all():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat;'
    cursor.execute(sql)
    result = cursor.fetchall()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()
def print_legend_rare():
    cursor = db.cursor()
    sql = 'SELECT * FROM Cat WHERE Cat_Rarity = "Legend Rare";'
    cursor.execute(sql)
    result = cursor.fetchall()
    for Cat in result:
        print(f"{Cat[0]:<25}{Cat[1]:<15}{Cat[2]:<15}{Cat[4]:<15}{Cat[5]:<15}")
    db.close()
while true:
    print("1: Print all data")
    print("2: Print legend rare only")
    print("3: exit")
    user_input = input("What would you like to do")
    