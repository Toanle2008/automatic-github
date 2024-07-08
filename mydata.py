import mysql.connector

passwd = open("passwd.pass", "r").readline()
data = mysql.connector.connect(
    user ="root",
    host ="localhost",
    passwd = passwd,
    database = "testdb"
)
cursor = data.cursor()
# cursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# update = "UPDATE students SET age = 16 WHERE name LIKE %s"
# cursor.execute(update, ('%ei',))
sqlFormImfor = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [
    ('henry', 21),
    ('Borney', 15),
    ('Kei', 11),
    ('Neptun', 31)
]
x = lambda x: 2
y = lambda y: 2

cursor.execute("SELECT * FROM students WHERE name LIKE 'k%'")
# cursor.execute("SELECT * FROM students LIMIT %s OFFSET %s", ( x(0),y(0), ))
result = cursor.fetchall()
# cursor.execute("DELETE FROM students")
# cursor.execute("DROP DATABASE test2db")
# cursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# cursor.execute("DROP TABLE students")
# cursor.executemany(sqlFormImfor, students)

for row in result: 
    print(row)
# for tb in cursor:
#     print(tb)
data.commit()
data.close()