from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UnfinishedTask(Base):
    __tablename__ = 'task_board'
    task = Column(String, primary_key=True)
    assignee = Column(String)
    day = Column(String)
    status = Column(String, default='unfinished')

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

def display_table(MyTable):
    # Retrieve data from the table
    data = session.query(MyTable).all()

    # Display the data
    if MyTable == 'UnfinishedTask'
        for row in data:
            print(row.task, row.assignee, row.day, row.status)
    else:
        for row in data:
            print(row.task, row.status)

    session.close()

if __name__ == '__main__':
    data = [
        UnfinishedTask(task='dishes', assignee='Janet', day='mon'),
        UnfinishedTask(task='trash', assignee='Marty', day='tue'),
        UnfinishedTask(task='laundry', assignee='Silvia', day='fri')
    ]
    insert_data(data)