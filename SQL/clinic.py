import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Leohanx@123',
    database = 'clinic'
)
cursor = db.cursor()
db.autocommit = True

cursor.execute("Delete FROM employees WHERE department_id IN (3,4) ORDER BY id")
db.commit()
cursor.close()
db.close()