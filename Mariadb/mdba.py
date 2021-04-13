# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="99022807",
        host="127.0.0.1",
        port=3306,
        database="pythondb"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# selectall = "SELECT * from employee" 
select_all_query = "SELECT NAME, No from test" 
cur.execute( select_all_query )

# query 결과를 list 형으로 가져옴.
resultset = cur.fetchall()

for firstname, lastname in resultset: 
    print(f"Name: {NAME}, Number: {No}")