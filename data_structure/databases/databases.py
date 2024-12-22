import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="py_users",
    auth_plugin="mysql_native_password",
    port=3006
)
cursor = conn.cursor()

cursor.execute("select * from user;")
print(cursor.fetchall())  # [(1526, 'John', 'john@example.com', 'premium'), (6745, 'Peter', 'smith@example.com', 'regular')]

cursor.execute("insert into user values(4478, 'Bob', 'bob@example.com', 'regular')")
conn.commit()

cursor.execute("select userId, username from user where userType = 'premium'")
print(cursor.fetchall())  # [(1526, 'John')]

conn.close()