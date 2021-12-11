import sqlite3

def do_thing():
    connection = sqlite3.connect(':memory:')
    connection.execute("""
        CREATE TABLE users (
            uid INT,
            ulname VARCHAR,
            userType INT
        )
    """)
    connection.execute('INSERT INTO users VALUES (1, "ZZZ", 3)')
    connection.execute('INSERT INTO users VALUES (2, "YYY", 2)')
    query = connection.execute('SELECT * FROM users WHERE userType=3')
    results = query.fetchall()
    print(results)

if __name__ == "__main__":
    do_thing()
