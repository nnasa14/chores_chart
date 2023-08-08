from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'my_table'
    task = Column(String, primary_key=True, nullable=False)
    assignee = Column(String)
    day = Column(String)

# Create a database engine
engine = create_engine('sqlite:///tasks.db')

# Create all defined tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the table
data = [
    MyTable(task='dishes', assignee='Alice', day='mon'),
    MyTable(task='trash', assignee='Bob', day='tue'),
    MyTable(task='laundry', assignee='Charlie', day='fri')
]

session.add_all(data)
session.commit()

# Close the session
session.close()

Session = sessionmaker(bind=engine)
session = Session()

# Retrieve data from the table
data = session.query(MyTable).all()

# Display the data
for row in data:
    print(row.task, row.assignee, row.day)

# Close the session
session.close()