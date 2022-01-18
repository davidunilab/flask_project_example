
import sqlite3
from faker import Faker
import random

fake = Faker('ka_GE')
con = sqlite3.connect('exmaple.db',  check_same_thread=False)
cur = con.cursor()


def create_students():
    cur.execute("""create table students (
    id integer primary key autoincrement, 
    name text not null, 
    age integer, 
    university default "Ilia State University"

    ) """)
    con.commit()

def seed_students(n=40):
    for i in range(1,n):
        cur.execute("""insert into students ( name, age) values (?,? )""", ( fake.name(), random.randint(20, 100)))
        con.commit()

if __name__ == "__main__":
    create_students()
    seed_students(200)
