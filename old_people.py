"""
Authors (Group Assignment):
Sivaneshwar Tamilmaran Latha
Mohamed Aadhil Syed Kaberdeen

Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
import sqlite3
import pandas as pd

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Query the database for all information for all people.
    cur.execute('SELECT name, age FROM people WHERE age >= 50')

    # Fetch all query results.
    # The fetchall() method returns a list, where each list item
    # is a tuple containing data from one row in the people table.
    old_people = cur.fetchall()

    con.commit()
    con.close()
    return old_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for name, age in name_and_age_list:
        print(f'{name} is {age} years old.')

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """

    save_as_csv = pd.DataFrame(name_and_age_list, columns=['Name', 'Age'])
    save_as_csv.to_csv(csv_path, index=False)


if __name__ == '__main__':
   main()