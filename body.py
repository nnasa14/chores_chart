import sqlite3

# Connect to database
conn = sqlite3.connect('chores.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chores_chart (
               chore TEXT NOT NULL PRIMARY KEY,
               name TEXT,
               day TEXT
    )
''')

# Commit and close
conn.commit()
conn.close()