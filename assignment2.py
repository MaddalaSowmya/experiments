import sqlite3

conn = sqlite3.connect('Hospital.db')
cursor = conn.cursor()

'''
cursor.execute("""
        CREATE TABLE IF NOT EXISTS physician(
        employee_id INT NOT NULL PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        position VARCHAR(20) NOT NULL,
        ssn INT NOT NULL
        );
""")

cursor.execute("""
        INSERT INTO physician 
        (employee_id, name, position, ssn)
        values
        (1, 'John Dorian', 'Staff Internist', 111),
        (2, 'Elliot Reid', 'Attending physician', 222),
        (3, 'Christopher Turk', 'Surgical attending physician', 333),
        (4, 'Percival Cox', 'Senior attending physician', 444),
        (5, 'Bob Kelso', 'Head Chief of Medicine', 555),
        (6, 'Todd Quinlan', 'Surgical attending physician', 666),
        (7, 'John Wen', 'Surgical attending physician', 777),
        (8, 'Keith Dudemeister', 'MD Resident', 888),
        (9, 'Molly Clock', 'Attending Psychiatrist', 999);        
""")

cursor.execute("""
        CREATE TABLE IF NOT EXISTS department(
        department_id INT NOT NULL PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        head INT NOT NULL);
""")

cursor.execute("""
        INSERT INTO department 
        (department_id, name, head)
        VALUES
        (1, 'General Medicine', 4),
        (2, 'Surgery', 7),
        (3, 'Psychiatry', 9);
""")

conn.commit()
'''

print("=================INNER JOIN=================")
cursor.execute("""
        SELECT * 
        FROM physician
        JOIN department
        ON physician.name=department.name;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


print("=================LEFT JOIN=================")
cursor.execute("""
        SELECT * 
        FROM physician
        LEFT JOIN department
        ON physician.name=department.name;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("=================RIGHT JOIN=================")
cursor.execute("""
        SELECT * 
        FROM physician
        RIGHT JOIN department
        ON physician.name=department.name;
""")
rows = cursor.fetchall()
for row in rows:
    print(row)


print("=================FULL JOIN=================")
cursor.execute("""
        SELECT * 
        FROM physician
        LEFT JOIN department
        ON physician.name=department.name
        
        UNION
        
        SELECT * 
        FROM physician
        RIGHT JOIN department
        ON physician.name=department.name        
        
""")
rows = cursor.fetchall()
for row in rows:
    print(row)