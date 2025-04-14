#Lexus Aguilera
# books_full.py

import sqlite3
from sqlalchemy import create_engine, MetaData, Table, select

# ---------- 16.4: Create books.db and insert data ----------

# Create SQLite database and connect
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Drop table if it exists (to reset for testing)
cursor.execute('DROP TABLE IF EXISTS book')

# Create table
cursor.execute('''
    CREATE TABLE book (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Insert book records
books = [
    ('A Thousand Splendid Suns', 'Khaled Hosseini', 2007),
    ('The Alchemist', 'Paulo Coelho', 1988),
    ('Signs: The Secret Language of the Universe', 'Laura Lynee Jackson', 2019),
    ('The Four Agreements: A Practical Guide to Personal Freedom', 'Don Miguel Ruiz', 1997),
    ('Milk and Honey', 'Rupi Kaur', 2014)
]

cursor.executemany('INSERT INTO book VALUES (?, ?, ?)', books)
conn.commit()
conn.close()

# ---------- 16.8: Use SQLAlchemy to select and print titles ----------

# Connect using SQLAlchemy
engine = create_engine('sqlite:///books.db')
connection = engine.connect()

# Reflect database schema
metadata = MetaData()
metadata.reflect(bind=engine)

# Access the book table
book = metadata.tables['book']

# Select and print titles alphabetically
stmt = select(book.c.title).order_by(book.c.title)
results = connection.execute(stmt)

print("\nBook titles in alphabetical order:")
for row in results:
    print(row.title)
