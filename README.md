# MySQL Data Insertion Using Python

## Overview
This project demonstrates how to connect Python to a MySQL database and perform basic database operations such as creating a table and inserting records.

## Technologies Used
- Python
- MySQL
- mysql-connector-python
- python-dotenv

## Database
Database used in this assignment:

usersdb

## Files

create_table_app.py  
Creates the Laptop table.

insertsinglerecord.py  
Inserts a single record into the Laptop table.

insert_record_variable.py  
Inserts a record using variables.

insert_multipleRecords.py  
Inserts multiple records into the Laptop table.

laptop_table_results.csv  
Exported results from the Laptop table.

## Environment Variables

The database password is stored in a `.env` file.

Example:

MYSQL_PASSWORD=your_password

The password is loaded in Python using:

```python
load_dotenv()
password = os.getenv("MYSQL_PASSWORD")