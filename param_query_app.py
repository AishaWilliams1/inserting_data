import mysql.connector as mydbconnection
from mysql.connector import Error

try:
    conn = mydbconnection.connect(
        host="localhost",
        database="classicmodels",
        user="root",
        password="password123",
        port=3306,
    )

    cursor = conn.cursor()

    sql_insert_query = """
    INSERT INTO tasks (title, start_date, due_date, priority, description)
    VALUES (%s, %s, %s, %s, %s)
    """

    record = (
        "Finish BI Assignment",
        "2026-03-04",
        "2026-03-10",
        2,
        "Complete parameterized query lab",
    )

    cursor.execute(sql_insert_query, record)
    conn.commit()

    print("Record inserted successfully")

except Error as e:
    print("Error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed")
