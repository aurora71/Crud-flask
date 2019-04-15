import pymysql
from flask import Flask, request
import json

app = Flask(__name__)
con = dict(host='192.161.178.223',port = 3306,user='cxrao',passwd = '',db ='crudTest',charset = 'utf8')

class crudHelper():
    @app.route('/flaskGetAll', methods=['get'])
    def getAll():
        orderBy = request.args.get('orderBy')
        conn = pymysql.connect(**con)
        cur = conn.cursor()
        sql = 'select * from student'
        if orderBy is not None:
            sql = sql + ' order by ' + orderBy;
        sql = sql + ' where isDeleted=0'
        print(sql)
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        return json.dumps(data,ensure_ascii=False)

    @app.route('/flaskGetStudentById', methods=['get'])
    def getStudent():
        id = request.args.get('id')
        conn = pymysql.connect(**con)
        cur = conn.cursor()
        sql = 'select * from student where id=' + id;
        print(sql)
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
        return json.dumps(data,ensure_ascii=False)

    @app.route('/flaskUpdateStudent', methods=['get'])
    def updateStudent():
        id = request.args.get('id')
        name = request.args.get('name')
        major = request.args.get('major')
        conn = pymysql.connect(**con)
        cur = conn.cursor()
        sql = "Update student set name = '" + name + "', major='" + major + "' where id=" +id
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        return 'Update Student '+id +' success'

    @app.route('/flaskDeleteStudent', methods=['get'])
    def delStudent():
        id = request.args.get('id')
        conn = pymysql.connect(**con)
        cur = conn.cursor()
        sql = "Update student set isDeleted=1 where id= " +id
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        return 'Delete Student '+id +' success'

    @app.route('/flaskAddStudent', methods=['get'])
    def addStudent():
        name = request.args.get('name')
        major = request.args.get('major')

        conn = pymysql.connect(**con)
        cur = conn.cursor()
        sql = "INSERT INTO student(name, major, isDeleted) VALUES ('" + name + "','" + major + "', 0)"
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        return 'Add new student ' + name

if __name__ == '__main__':
    app.run(debug = True)