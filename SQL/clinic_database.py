import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Leohanx@123',
    database = 'clinic'
)
db.autocommit = True

cursor1 = db.cursor()
cursor1.execute("SELECT id, CONCAT(first_name, ' ', last_name) AS full_name, job_title, salary FROM employees WHERE salary > 1000.00 ORDER BY salary ASC")
result = cursor1.fetchall()
db.commit()
cursor1.close()

cursor2 = db.cursor()
cursor2.execute("UPDATE employees SET salary = salary * 1.1 WHERE job_title = 'Dentist'")
db.commit()
cursor2.close()

for row in result:
    print(row)

db.close