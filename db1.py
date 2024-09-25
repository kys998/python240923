# db1.py

import sqlite3

# con=sqlite3.connect(":memory:")
con=sqlite3.connect("c:\\work\\sample.db")
cur=con.cursor()
cur.execute("CREATE TABLE if not exists PhoneBook (Name text, PhoneNum text);")
cur.execute("insert into PhoneBook values('김길동', '010-111-1234');")

cur.execute("select * from PhoneBook")
for row in cur:
    print(row[0],row[1])

name="전우치"
PhoneNum="010-222-1234"
cur.execute("insert into PhoneBook values (?,?);", (name, PhoneNum))

datalist=(("박문수", "010-333-1234"),("홍길동", "010-555-1234"))
cur.executemany ("insert into PhoneBook values (?,?);", datalist)

cur.execute("select * from PhoneBook")
# for row in cur:
    # print(row[0],row[1])

print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall())---")
print(cur.fetchall())

cur.execute("select * from PhoneBook")
print(cur.fetchall())

for row in cur:
    print(row[0],row[1])

con.commit()
