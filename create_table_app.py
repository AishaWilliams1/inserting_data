import mysql.connector as mydbconnection
from mysql.connector import Error

try:
    # Connect to classicmodels database
    conn = mydbconnection.connect(
        host="localhost",
        database="classicmodels",
        user="root",
        password="password123",
        port=3306,
    )

    if conn.is_connected():
        print("Connected to MySQL")

        cursor = conn.cursor()

        myquery = """
        CREATE TABLE tasks (
            task_id INT AUTO_INCREMENT,
            title VARCHAR(255) NOT NULL,
            start_date DATE,
            due_date DATE,
            priority TINYINT NOT NULL DEFAULT 3,
            description TEXT,
            PRIMARY KEY (task_id)
        )
        """

        print(myquery)

        cursor.execute(myquery)
        print("Table created successfully!")

except Error as e:
    print("Error:", e)

finally:
    if "conn" in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed.")
