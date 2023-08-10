from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CompletedTask(Base):
    __tablename__ = 'completed'
    task = Column(String, primary_key=True)
    status = Column(String, default='completed')
    
# Create a database engine
engine = create_engine('sqlite:///tasks.db')

# Create all defined tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def insert_data(data):
    # Add data and commit to table
    session.add_all(data)
    session.commit()
    session.close()

def display_table():
    # Retrieve data from the table
    data = session.query(CompletedTask).all()

    # Display the data
    for row in data:
        print(row.task, row.status)

    session.close()

def mark_as_complete(task):
    data = session.query(CompletedTask).all()

    for row in data:
        if row.task == task:
            # Mark as complete
            pass

if __name__ == '__main__':
    data = [
        CompletedTask(task='dishes', assignee='Janet', day='mon'),
        CompletedTask(task='trash', assignee='Marty', day='tue'),
        CompletedTask(task='laundry', assignee='Silvia', day='fri')
    ]
    insert_data(data)
    display_table()