import mysql.connector as mydbconnection
from mysql.connector import Error

try:
    conn = mydbconnection.connect(
        host="localhost",
        database="usersdb",
        user="root",
        password="",
        port="3306",
    )

    cursor = conn.cursor()

    mySql_insert_query = """
    INSERT INTO Laptop (Id, Name, Price, Purchase_date)
    VALUES (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14')
    """

    cursor.execute(mySql_insert_query)
    conn.commit()

    print(cursor.rowcount, "Record inserted successfully")

except Error as e:
    print("Failed to insert record {}".format(e))

finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
