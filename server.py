#import pyodbc as pyodbc
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')


@app.route('/<num>')
def hello(num):
    # conn = pyodbc.connect(
    #     r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db1\serv.accdb;')
    # cursor = conn.cursor()
    # cursor.execute('select * from table ВыборПоверитель')
    #
    # for row in cursor.fetchall():
    #     print(row)
     return render_template('user.html', name=num)

@app.route('/')
def froot():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #app.run()