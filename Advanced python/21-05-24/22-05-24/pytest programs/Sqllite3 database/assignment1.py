import sqlite3

conn = sqlite3.connect('StudentRepo.db')

cursor = conn.cursor()


cursor.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT_DETAILS(
        ID INT NOT NULL PRIMARY KEY,
        NAME VARCHAR(20) NOT NULL,
        CLASS VARCHAR(20) NOT NULL,
        MARKS INT NOT NULL,
        GENDER CHAR(3) NOT NULL);
""")

'''
cursor.execute("""
        INSERT INTO STUDENT_DETAILS 
        (ID, NAME, CLASS, MARKS, GENDER)
        VALUES
        (1, 'John Deo', 'Four', 75, 'female'),
        (2, 'Max Ruin', 'Three', 85, 'male'),
        (3, 'Arnold', 'Three', 55, 'male'),
        (4, 'Krish Star', 'Four', 60, 'female'),
        (5, 'John Mike', 'Four', 60, 'female'),
        (6, 'Alex John', 'Four', 55, 'male'),
        (7, 'My John Rob', 'Five', 78, 'male'),
        (8, 'Asruid', 'Five', 85, 'male'),
        (9, 'Tes Qry', 'Six', 78, 'male'),
        (10, 'Big John', 'Four', 55, 'female');    
""")
conn.commit()


cursor.execute("""
        UPDATE STUDENT_DETAILS SET MARKS=70 WHERE NAME='Arnold';
""")
conn.commit()


cursor.execute("""
DELETE FROM STUDENT_DETAILS WHERE NAME='Tes Qry';
""")
conn.commit()


'''
rows = cursor.execute("""
SELECT * FROM STUDENT_DETAILS ORDER BY MARKS;
""")
for row in rows:
    print(row)


rows = cursor.execute("""
SELECT * FROM STUDENT_DETAILS WHERE GENDER='female';
""")
for row in rows:
    print(row)


rows = cursor.execute("""
SELECT NAME FROM STUDENT_DETAILS ORDER BY MARKS DESC LIMIT 1;
""")
for row in rows:
    print(row)

'''
# cursor.execute("""
# SELECT NAME FROM STUDENT_DETAILS ORDER BY MARKS DESC;
# """)
# # r = fetchall()
# r = cursor.fetchone()
# print(r[0])

'''

rows = cursor.execute("""
SELECT NAME FROM STUDENT_DETAILS ORDER BY MARKS LIMIT 1;
""")
for row in rows:
    print(row)
'''
# conn.commit()


conn.close()
'''