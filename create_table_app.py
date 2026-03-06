import os
from dotenv import load_dotenv
import mysql.connector as mydbconnection
from mysql.connector import Error

load_dotenv(dotenv_path=".env")

password = os.getenv("MYSQL_PASSWORD")
print("Password loaded?", password)

try:
    conn = mydbconnection.connect(
        host="localhost",
        database="usersdb",
        user="root",
        password=password,
        port="3306",
    )
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Laptop (
        Id INT NOT NULL PRIMARY KEY,
        Name VARCHAR(250) NOT NULL,
        Price FLOAT NOT NULL,
        Purchase_date DATE NOT NULL
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table is created (or already exists).")

except Error as e:
    print(f"Failed to create table: {e}")

finally:
    try:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")
    except NameError:
        pass
