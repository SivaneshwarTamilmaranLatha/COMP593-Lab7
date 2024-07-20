"""
Authors (Group Assignment):
Sivaneshwar Tamilmaran Latha
Mohamed Aadhil Syed Kaberdeen

Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime
import random

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # Open a connection to the database.
    con = sqlite3.connect('social_network.db')
    # Get a Cursor object that can be used to run SQL queries on the database.
    cur = con.cursor()
    
    # Define an SQL query that creates a table named 'people'.
    # Each row in this table will hold information about a specific person.
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """

    # Execute the SQL query to create the 'people' table.
    # Database operations like this are called transactions.
    cur.execute(create_ppl_tbl_query)

    # Commit (save) pending transactions to the database.
    # Transactions must be committed to be persistent.
    con.commit()

    # Close the database connection.
    # Pending transactions are not implicitly committed, so any
    # pending transactions that have not been committed will be lost.
    con.close()
    print("Successfully created the people table in the database...")
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""

    # Open a connection to the database.
    con = sqlite3.connect('social_network.db')

    # Get a Cursor object that can be used to run SQL queries on the database.
    cur = con.cursor()

    # Create a faker object for English Canadian locale
    fake = Faker("en_CA")

    # Define an SQL query that inserts a row of data in the people table.
    # The ?'s are placeholders to be fill in when the query is executed.
    # Specific values can be passed as a tuple into the execute() method.
    add_person_query = """
    INSERT INTO people
    (
    name,
    email,
    address,
    city,
    province,
    bio,
    age,
    created_at,
    updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    
    # Generate fake data for 200 people
    for _ in range(200):
        province = fake.administrative_unit()
        new_person = (
            fake.name(),
            fake.email(),
            fake.address(),
            fake.city(),
            province,
            fake.text(),
            random.randint(1, 100),
            datetime.now(),
            datetime.now()
        )
        
        # Execute query to add new person to people table
        cur.execute(add_person_query, new_person)
    
    con.commit()
    con.close()
    print("Successfully populated the people table with 200 fake people! ")
    return

def adapt_datetime(date_time):
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
    return date_time.strftime("%Y-%m-%d %H:%M:%S")

sqlite3.register_adapter(datetime, adapt_datetime)

if __name__ == '__main__':
   main()