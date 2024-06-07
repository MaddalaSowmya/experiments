import sqlite3

# create a connection to the database
connection = sqlite3.connect('employee.db')

# cursor object
cursor_obj = connection.cursor()


# create table employee_details
cursor_obj.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEE_DETAILS(
    NAME VARCHAR(20) NOT NULL PRIMARY KEY,
    ID INT NOT NULL,
    BU VARCHAR(10),
    SALARY INT);
''')

'''
# insert data to the employee_details table
cursor_obj.execute("""
        INSERT INTO EMPLOYEE_DETAILS VALUES 
        ('A',1,'HR',20000),
        ('B',2,'IT',30000),
        ('C',3,'HR',20000),
        ('D',4,'SP',10000),
        ('E',5,'SP',10000),
        ('F',6,'HR',20000);        
        """)

cursor_obj.execute("""
        INSERT into EMPLOYEE_DETAILS VALUES ('G',7,'IT',30000);       
""")

connection.commit()
'''

obj = cursor_obj.execute("""
select * from employee_details;
""")

for row in obj:
    print(row)

connection.close()