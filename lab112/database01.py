#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect("test.db")

print("opened DB successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
        (ID       INT      PRIMARY KEY     NOT NULL,
         NAME     TEXT                     NOT NULL,
         AGE      INT                      NOT NULL,
         ADDRESS  CHAR(50),
         SALARY   REAL                      );''')

print("Table created successfully")


#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1, 'Paul', 32, 'California', 20000.00)")
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")


#conn.commit()
#print("Records created successfully")

conn.execute("DELETE FROM COMPANY WHERE ID = 4")

cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")

for x in cursor:
    print(x)

conn.close()
