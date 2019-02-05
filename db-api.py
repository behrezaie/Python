#!/usr/bin/env python3

import sqlite3

def main():
    print('connecting to the database...')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    print('creating database...')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, age INTEGER, sex TEXT
        )
        """)
    
    print('inserting the first row...')
    cur.execute("""
        INSERT INTO test (fname, lname, age, sex) VALUES ('Yixun', 'Lu', 24, 'female')
        """)
    
    print('inserting the second row...')
    cur.execute("""
        INSERT INTO test (fname, lname, age, sex) VALUES ('Scott', 'John', 29, 'male')
        """)
    
    print('inserting the third row...')
    cur.execute("""
        INSERT INTO test (fname, lname, age, sex) VALUES ('Ali', 'Farahi', 40, 'male')
        """)
    
    print('committing...')
    db.commit()
    
    print('countting number of rows...')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    
    print(f'there are {count} rows in the \'test\' table.')
    print('------------------------------------------------')
    
    print('reading the \'test\' table...')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('dropping the \'test\' table')
    cur.execute("DROP TABLE test")
    
    print('closing the database...')
    db.close()

if __name__ == '__main__': main()
