from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import configparser



Base = declarative_base()

class UnfinishedTask(Base):
    __tablename__ = 'task_board'

    task = Column(String, primary_key=True)
    assignee = Column(String)
    day = Column(String)
    status = Column(String, default='O')

    def __init__ (self, task, assignee, day, status):
        self.task = task
        self.assignee = assignee
        self.day = day
        self.status = status

    def __repr__(self):
        return f"{self.task}: {self.assignee} {self.day} ({self.status})"

# Create a database engine
engine = create_engine('sqlite:///tasks.db', echo=True)

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def clear_table(session):
    session.query(UnfinishedTask).delete()
    session.commit()
    session.close()

def insert_data(data):
    # Add data and commit to table
    session.add_all(data)
    session.commit()
    session.close()

def display_table():
    # Retrieve data from the table
    data = session.query(UnfinishedTask).all()

    # Display the data
    for row in data:
        print(row.task, row.status)

    session.close()

def mark_as_complete(task):
    data = session.query(UnfinishedTask).all()

    for row in data:
        if row.task == task:
            row.status = 'X'

    session.commit()
    session.close()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config["General"] = {
        "title": "Task Calendar",
        "version": "1.0",
        "debug": "True"
    }

    data = [
        UnfinishedTask(task='dishes', assignee='Janet', day='mon', status='complete'),
        UnfinishedTask(task='trash', assignee='Marty', day='tue', status='complete'),
        UnfinishedTask(task='laundry', assignee='Silvia', day='fri', status='incomplete')
    ]
    insert_data(data)
    
    """mark_as_complete('dishes')
    display_table()

    clear_table(session)
    display_table()"""