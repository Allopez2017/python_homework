import sqlite3
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Publishers (
                   publisher_id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL UNIQUE,
                   );
                   """)
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Magazines (
                   magazine_id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL UNIQUE,
                   issue INTEGER
                   publisher_id INTEGER NOT NULL
                   FOREIGN KEY (publisher_id) REFERENCES publishers (publishers_id)
                   );
                   """)
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Subscribers (
                   subscriber_id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE
                   );
                   """)
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Subscriptions (
                   subscription_id INTEGER PRIMARY KEY,
                   subscriber_id INTEGER NOT NULL,
                   magazine_id INTEGER,
                   subscription_start TEXT NOT NULL,
                   FOREIGN KEY (subscriber_id) REFERENCES Subsribers (subscriber_id),
                   FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
                   UNIQUE (subscriber_id, magazine_id)
                   );
                   """)
    print("Tables successfully created")

    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT INTO Publishers (name) VALUES (?);",(name))
        except sqlite3.KeyError as e:
            print(f"Error adding publisher: {e}")

    def add_magazine(cursor, title, issue, publisher):
        cursor.execute("SELECT * FROM Publishers WHERE title = ?", (publisher))
        results = cursor.fetchall()
        if len(results) > 0:
            publisher_id = results[0][0]
        else:
            print(f"Error adding publisher {e}")
        try:
            cursor.execute("INSERT INTO Magazines (title, issue, publisher_id) VALUES (?, ?, ?);", (title, issue, publisher_id))
        except sqlite3.KeyError as e:
            print(f"Error adding publisher: {e}")

    def add_subscriber(cursor, name, email):
        try:
            cursor.execute("SELECT * from Subscribers WHERE name = ? AND email = ?;", (name, email))
            results = cursor.fetchall()
            if len(results) > 0:
                print(f"Error adding subscriber to database: {e}")
            else:
                cursor.execute("INSERT INTO Subscribers (name, email) VALUES (?, ?);", (name,email))
        except sqlite3.KeyError as e:
            print(f"Error adding subscriber: {e}")

    def add_subscription(cursor, name, email, magazine, subscription_start):
        cursor.execute("SELECT * from Subscribers WHERE name = ? AND email = ?;", (name, email))
        results = cursor.fetchall()
        if len(results) > 0:
            subscriber_id = results[0][0]
        else:
            print(f"Subscriber does not exist")

        cursor.execute("SELECT * from Magazines WHERE title = ?;", (magazine))
        results = cursor.fetchall()
        if len(results) > 0:
            magazine_id = results[0][0]
        else:
            print(f"Magazine does not exist")

        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?;", (subscriber_id, magazine_id))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"This subscription already exists")
        else:
            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, subscription_start) VALUES (?, ?, ?);", (subscriber_id, magazine_id, subscription_start))

        add_publisher(cursor, "Square")
        add_publisher(cursor, "Triangle")
        add_publisher(cursor, "Circle")

        add_magazine(cursor, "National Geographic")
        add_magazine(cursor, "Essence")
        add_magazine(cursor, "Vogue")

        add_subscriber(cursor, "Mary", "123@gmail.com")
        add_subscriber(cursor, "Alice", "456@yahoo.com")
        add_subscriber(cursor, "John", "789@hotmail.com")

        add_subscription(cursor, "Mary", "123@gmail.com", "August 4, 2017")
        add_subscription(cursor, "Alice", "456@yahoo.com", "November 6, 2018")
        add_subscription(cursor, "John", "789@hotmail.com", "June 3, 2022")

        print(f"Data successfully uploaded")
        conn.commit

        cursor.execute("""SELECT * FROM Magazines m JOIN Publishers p ON p.publisher_id = m.publisher_id WHERE p.title = 'Triangle'""")
        result = cursor.fetchall()
        for row in result:
            print(row)

except sqlite3.KeyError as e:
    print(f"An error occured: {e}")
