import sqlite3

# Connect to database
conn = sqlite3.connect('chores.db')
cursor = conn.cursor()

# Create table
"""
    chore(str): title of chore
    name(str): person(s) delegated to chore
    day(str): day(s) which chore is expected to be done
"""
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chores_chart (
               chore TEXT NOT NULL PRIMARY KEY,     
               name TEXT,
               day TEXT
    )
''') 

# Add data to table
cursor.executemany('INSERT INTO chores_chart (chore, name, day) VALUES (?,?)'[
    ('Trash', 'Marty', 'Tuesday'),
    ('Dishes', 'Flexible', 'Daily'),
    ('Meal Prep', 'Janice', 'Sunday')
])

# Retrieve data
cursor.execute('SELECT * FROM chores_chart')
data = cursor.fetchall()

# Display data
for row in data:
    print(row)

# Commit and close
conn.commit()
conn.close()

