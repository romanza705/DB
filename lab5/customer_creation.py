import psycopg2
from faker import Faker
import random

print("program started")
con = psycopg2.connect(database="DB_lab5", user="postgres", password="TALer@501070", host="127.0.0.1")
print("DB connected")
cur = con.cursor()
cur.execute('''CREATE TABLE customers
       (id INT PRIMARY KEY NOT NULL,
       name TEXT NOT NULL,
       address TEXT NOT NULL,
       age INT NOT NULL,
       review TEXT);''')

fake = Faker()
for i in range(100000):
    if not (i % 1000):
        print(str(i // 1000) + "%")
    cur.execute("INSERT INTO customers (id,name,address,age,review) VALUES('" + str(
        i) + "','" + fake.name() + "','" + fake.address() + "','" + str(
        random.randint(18, 63)) + "','" + fake.text() + "')")
    con.commit()
print("program finished")
