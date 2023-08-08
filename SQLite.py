import sqlite3

class Chores:

    def __init__(self):
        """ Create table
 
        chore(str): title of chore
        name(str): person(s) delegated to chore
        day(str): day(s) which chore is expected to be done

         Connect to database"""
        conn = sqlite3.connect('chores.db')
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor
        
        self.table = cursor.execute('''
            CREATE TABLE IF NOT EXISTS chores_chart (
                    chore TEXT NOT NULL PRIMARY KEY,     
                    name TEXT,
                    day TEXT
            )
        ''') 

    def close_commit(self):
        # Commit and close
        self.conn.commit()
        self.conn.close()

    def add_data(self, chore, name, day):
        self.cursor.execute('INSERT INTO chores_chart (chore, name, day) VALUES (?, ?, ?)', chore, name, day)

        self.conn.commit()
        self.conn.close()
        Chores.close_commit()

    def display_data(self):
            # Retrieve data
        self.cursor.execute('SELECT * FROM chores_chart')
        data = self.cursor.fetchall()

        # Display data
        for row in data:
            print(row)

        Chores.close_commit()
    
if __name__ == "__main__":
    chores_instance = Chores()

    # Add data to table
    Chores.add_data = [
        ('Trash', 'Marty', 'Tuesday'),
        ('Dishes', 'Flexible', 'Daily'),
        ('Meal Prep', 'Janice', 'Sunday')
    ]