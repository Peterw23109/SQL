import sqlite3


def print_pokemon():
    db = sqlite3.connect('pokemon.db')
    cursor = db.cursor()
    sql = 'SELECT pokemon_id FROM pokemon;'

    cursor.execute(sql)
    result = cursor.fetchall()
    for pokemon in result:
        print(pokemon)
    db.close()
    
print_pokemon()