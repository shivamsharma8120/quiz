from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",data='login')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/sign',methods=['post'])
def sign():
    t1=request.form['a']
    t2=request.form['b']
    t3=request.form['c']
    t4=request.form['d']
    t5=request.form['e']

    conn=mysql.connector.connect(host='localhost',user='root',password='',database='zehar1')
    c=conn.cursor()

    c.execute("insert into projectt(name,email,phone,password,address) value('"+t1+"','"+t2+"','"+t3+"','"+t4+"','"+t5+"')")

    conn.commit()

    return render_template("index.html",data='login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/log',methods=['post'])
def log():
    t1=request.form['a']
    t2=request.form['b']

    conn=mysql.connector.connect(host='localhost',user='root',password='',database='zehar1')
    c=conn.cursor()

    c.execute("select * from projectt where email='"+t1+"' and password='"+t2+"'")

    if(c.fetchone()):
        return render_template("index.html",data='logout',x="click here to play quiz")
    else:
        return('wrong id password')


@app.route('/c2')
def c2():
    return render_template("c2.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")






if(__name__)=="__main__":
    app.run(debug=True)