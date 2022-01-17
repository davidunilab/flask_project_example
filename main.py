# pip install -r requirements.txt # install
# pip freeze > requirements.txt # create file
# https://docs.python.org/3/library/sqlite3.html

from flask import Flask
from flask_restful import Resource, Api
import sqlite3
con = sqlite3.connect('identifier.sqlite',  check_same_thread=False)
cur = con.cursor()

# cur.execute("SELECT * FROM students where `name` = 'Arsen'")
# print(cur.fetchall())

# cur.execute("Update students set name = ? where id = ?",('Gvanca', 5))
# con.commit()

# cur.execute("Delete from students where  id in (?, ?)", (4, 6))
# con.commit()
# CRUD

# cur.executemany("insert InTo students (id, name, course, age) values (?,?,?,?)", [(9, 'Mariami', '', 21), (10, 'Arsen', '?', 21)])
# con.commit()





app = Flask(__name__)
api = Api(app)
# mysite.ge/


class Students(Resource):
    def get(self, student_id):
        print(type(student_id))
        print(student_id)

        cur.execute("SELECT * FROM students where id = ?", (student_id,))
        student = cur.fetchone()
        print(student)
        return student

api.add_resource(Students, '/read/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
