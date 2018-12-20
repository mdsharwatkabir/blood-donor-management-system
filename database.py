from database_connection import DatabaseConnection


def create_connection():
    with DatabaseConnection('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS donor (id INTEGER PRIMARY KEY,Name TEXT,blood_group Text,City Text,Contact Text)")


def insert_table(name, blood_group, city, contact):
    with DatabaseConnection('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO donor VALUES (NULL, ?, ?, ?, ?)", (name, blood_group, city, contact))


def show():
    with DatabaseConnection('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM donor")
        database_value = cursor.fetchall()
    return database_value


def delete(id):
    with DatabaseConnection('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM donor WHERE id=?", (id,))


def update_table(id, name, blood_group, city, contact):
    with DatabaseConnection('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE donor SET name=?,blood_group=?,city=?,contact=? WHERE id=?", (name, blood_group, city, contact, id))


def search(name="", blood_group="", city="", contact=""):
    with DatabaseConnection('Data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM  donor WHERE name=? OR blood_group=? OR City=? OR Contact=?", (name, blood_group, city, contact))
        database_value = cursor.fetchall()
    return database_value
