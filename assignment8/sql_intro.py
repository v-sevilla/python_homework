import sqlite3

#Task 1: Create a New SQLite Database
with sqlite3.connect("../db/magazine.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    print("Database created and connected successfully.")
    cursor = conn.cursor()

#Task 2: Define Database Structure
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publisher (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publisher (publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscriber_id INTEGER,
        magazine_id INTEGER,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        expiration_date TEXT NOT NULL,
        PRIMARY KEY (subscriber_id, magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
    )
    """)

    print("Tables created successfully.")

#Task 3: Populate Tables with Data
def add_publisher(cursor, publisher_id, name):
    try:
        cursor.execute("INSERT INTO Publisher (publisher_id, name) VALUES (?,?)", (publisher_id, name))
    except sqlite3.IntegrityError:
        print(f"id {publisher_id} is already in the database.")

def add_magazine(cursor, magazine_id, name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (magazine_id, name, publisher_id) VALUES (?,?,?)", (magazine_id, name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"id {magazine_id} is already in the database.")

def add_subscriber(cursor, subscriber_id, name, address):
    try:
        cursor.execute("INSERT INTO Subscribers (subscriber_id, name, address) VALUES (?,?,?)", (subscriber_id, name, address))
    except sqlite3.IntegrityError:
        print(f"{name} and the same address already exists in the database.")

def add_subscription(cursor, subscriber_id, magazine_id, name, address, expiration_date):
    try:
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, name, address, expiration_date) VALUES (?,?,?,?,?)", (subscriber_id, magazine_id, name, address, expiration_date))
    except sqlite3.IntegrityError:
        print(f"{name} and the same address already exists in the database.")

# Insert sample data into tables

add_publisher(cursor, 1, 'Ablex')
add_publisher(cursor, 2, 'Compute')
add_publisher(cursor, 3, 'GOOD')
add_magazine(cursor, 1, 'Sutton', 3)
add_magazine(cursor, 2, 'The Guarantor', 2)
add_magazine(cursor, 3, 'Preview', 3)
add_subscriber(cursor, 1, 'Alice', '123 Pizza Street')
add_subscriber(cursor, 2, 'Harry', '4 Privet Drive')
add_subscriber(cursor, 3, 'Simi', '987 Bakers Lane')
add_subscription(cursor, 2, 1, 'Harry', '4 Privet Drive', '12-27-2026')
add_subscription(cursor, 3, 2, 'Simi', '987 Bakers Lane', '08-03-2025')
add_subscription(cursor, 3, 1, 'Simi', '987 Bakers Lane', '02-19-2026')

conn.commit()
print()

#Task 4: Write SQL Queries

#Write a query to retrieve all information from the subscribers table.
cursor.execute("SELECT * FROM Subscribers")
result = cursor.fetchall()
for row in result:
    print(row)
print()

cursor.execute("SELECT * FROM Magazines ORDER BY name ASC")
result = cursor.fetchall()
for row in result:
    print(row)
print()

cursor.execute("SELECT * FROM Magazines JOIN Publisher ON magazines.publisher_id = publisher.publisher_id WHERE publisher.name = 'GOOD'")
result = cursor.fetchall()
for row in result:
    print(row)
