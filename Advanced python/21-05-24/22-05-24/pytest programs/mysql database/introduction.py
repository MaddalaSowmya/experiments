import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='orcl'
)
print(dataBase)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE \
               IF NOT EXISTS first")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
cursor.close()
dataBase.close()

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='orcl',
    database='new'
)
print(dataBase)
cursor.close()
dataBase.close()

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='orcl',
    database='first'
)
print(dataBase)

cursor=dataBase.cursor()


cursor.execute("""
SHOW TABLES;
""")

# print("prinitig tables")
# for t in cursor:
#     print(t)

# cursor.fetchall()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT(
        NAME VARCHAR(20) NOT NULL PRIMARY KEY,
        BRANCH VARCHAR(20),
        ROLL INT NOT NULL,
        SECTION VARCHAR(20),
        AGE INT);
""")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT_DETAILS(
        NAME VARCHAR(20) NOT NULL PRIMARY KEY,
        BRANCH VARCHAR(20),
        ROLL INT NOT NULL,
        SECTION VARCHAR(20),
        AGE INT);
""")

'''
cursor.execute("""
        INSERT INTO STUDENT_DETAILS (NAME, BRANCH ,ROLL, SECTION, AGE)
        VALUES
        ('A', 'ECE', 1, 'A', 22),
        ('B', 'ECE', 2, 'A', 22);        
""")
# dataBase.commit()
'''

# cursor.execute("""
# UPDATE STUDENT_DETAILS SET BRANCH='CSE' WHERE NAME='B';
# """)
# dataBase.commit()

print("&&&&&&&&&&&&&&&&")