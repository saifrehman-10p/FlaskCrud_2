from flask import Flask, session,current_app,Request
from markupsafe import escape
from flask import url_for
from flask import request
app = Flask(__name__)


from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import flash
import sys

import os
import random
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost/Test'
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'AJDJRJS24$($(#$$33--'
from app import db

    
class People(db.Model):
    __tablename__='People'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
class Employee(db.Model):
    __tablename__='Employee'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(150),  nullable=False)
    salary = db.Column(db.String(150), nullable=False)
    dept=db.Column(db.String(150), nullable=False)
    
    def __init__(self, username,password, email,salary,dept):
        self.username = username
        self.password = password
        self.email = email
        self.salary = salary
        self.dept = dept

        
SECRET_KEY = 'the random string'
con = psycopg2.connect(database="Test", user="postgres", password="12345", host="127.0.0.1", port="5432")
# # con = psycopg2.connect(database="Test", user="postgres", password="12345", host="127.0.0.1")
cursor = con.cursor()
@app.route('/submit', methods=['GET','POST'])
def submit():
    try:
        print(session.get("name"))
        if session.get("name"):




            if request.method=='POST':


                print("heloo")
                username =request.form['username']
                email=request.form['password']
                
  

                student=People(username,email)
                db.session.add(student)
                db.session.commit()
                return redirect(url_for('landing'))
            else:
         

                # i=0
                # i=i+1
                # print(i)
                # studentResult=db.session.query(People).filter(People.id==1)
                # for result in studentResult:


                #     print(result.username)
                return render_template('login3.html')
        else:
            return redirect(url_for('login'))

    except:
        return redirect(url_for('login'))

        
    # return render_template('login3.html')

@app.route('/esubmit', methods=['GET','POST'])
def esubmit():
    try:
        print(session.get("name"))
        if session.get("name"):




            if request.method=='POST':


                print("heloo")
                username =request.form['username']
                password =request.form['password']
                email=request.form['email']
                salary=request.form['salary']
                dept=request.form['dept']

                
  

                employee=Employee(username,password,email,salary,dept)
                db.session.add(employee)
                db.session.commit()
                return redirect(url_for('landing'))
            else:
         

                # i=0
                # i=i+1
                # print(i)
                # studentResult=db.session.query(People).filter(People.id==1)
                # for result in studentResult:


                #     print(result.username)
                return render_template('eadd.html')
        else:
            return redirect(url_for('login'))

    except:
        return redirect(url_for('login'))

  

@app.route("/")
def index():
    # db.create_all()
    # app.run()


   
    return redirect(url_for('login'))


if __name__ == '__main__':
    session['secrrt']='sec'
    db.create_all()
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", port=5000, debug=True)

@app.route("/landing")
def landing():
    print(session.get("name"))
    if not session.get("name"):
        return redirect(url_for('login'))
    else:

        return render_template('landing.html')
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {(name)}!"
# @app.route("/A.html")
# def home2():
#    return"<p>Hello, World</p>"
# @app.route("/boy/<path:name>")
# def fhunc1(name):
#     return f"hello world {escape(name)}"
   

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login3')
# def login3():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     x=url_for('profile', username='John Doe')
#     print(x)

# @app.route("/login1",methods=['GET','POST'])
# def fun1():
#     if request.method=='POST':
#         return login()
#     else:

#         return index()
# # @app.route("/login", methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         return do_the_login()
# #     else:
# #         return show_the_login_form()
   
# from flask import render_template

# #@app.route('/hello/')
# x=['saif','usama']
# y='amna'
# @app.route('/hello/')
# def hello():
#     print(x)
#     return render_template('hello.html', name1=x,name2=y)

@app.route("/home")
def home():
    return("logged in successfully")

@app.route('/login', methods=['GET', 'POST'])
def login():



    



    
    try:
        
        if request.method=='POST':
            

             
       
       
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #studentResult=db.session.query(People).filter(People.username==request.form['username'])
            studentResult=People.query.filter(People.username==request.form['username'])

            for i in studentResult:

                print(i)
                if request.form['username'] == i.username and request.form['password'] == i.email:
                
                    print('You were successfully logged in')
                    session["name"] = request.form.get("username")
                    flash('You were successfully logged in')
                    return redirect(url_for('landing'))
                else:
                   return render_template("login2.html")
        else:




           
            return render_template('login2.html')
    except:
        return render_template('login2.html')
@app.route('/Delete', methods=['GET', 'POST'])
def Delete():



    



    
    try:

        print(session.get("name"))
        if session.get("name"):
            
        
            if request.method=='POST':
             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
                People.query.filter(People.username==request.form['username']).delete()
                db.session.commit()
                return redirect(url_for('landing'))

            
            else:





           
                return render_template('del.html')
        else:
            return redirect(url_for('login'))

    except:
        return render_template('login2.html')
@app.route('/update', methods=['GET', 'POST'])
def update():



    



    
    try:
        print(session.get("name"))
        if session.get("name"):
        
            if request.method=='POST':
             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
                users=People.query.filter(People.username==request.form['username'])
            # users.email="lk"
            # db.session.commit()
            # return(redirect(login))

                for i in users:
                    print(i.username)
                    i.email=request.form['password']
                
                    db.session.commit()
                    return redirect(url_for('landing'))
            
            else:




           
                return render_template('update.html')
        else:
            return redirect(url_for('login'))
    except:
        return redirect(url_for('login'))
@app.route('/update1', methods=['GET', 'POST'])
def update1():




    



    
    try:
        
        if request.method=='POST':
            
            




             
       
        
        #l='saif'
            # cursor.execute('select * from public."People"')
            # result = cursor.fetchall()
            # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
            print('post')
           # cursor.execute('UPDATE public."People" set email=%s WHERE username=%s', ('1234','filza',))
          
            cursor.execute('UPDATE public."People" SET email = %s WHERE username = %s',('saif123','saif'))
            #cursor.execute('UPDATE public."Employee" SET password =%s,email =%s,salary =%s,dept =%s WHERE username=%s' , (request.form['password'],request.form['email'],request.form['salary'],request.form['dept'],request.form['username'],))
            con.commit()
            
            # x=cursor.fetchone()
            # for i in x:
            #     print(i)
            # People.query.filter(People.username==request.form['username']).delete()
            # db.session.commit()
            return(redirect(url_for('login')))

            
        else:





           
            return render_template('update.html')
    except:
        return render_template('login1.html')
@app.route('/Delete1', methods=['GET', 'POST'])
def Delete1():



    



    
    try:

        print(session.get("name"))
        if session.get("name"):
            
        
            if request.method=='POST':
             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
                Employee.query.filter(Employee.username==request.form['username']).delete()
                db.session.commit()
                return redirect(url_for('landing'))

            
            else:





           
                return render_template('dele.html')
        else:
            return redirect(url_for('login'))

    except:
        return render_template('login2.html')
@app.route('/updateemp', methods=['GET', 'POST'])
def updateemp():




    



    
    try:
        
        if request.method=='POST':

             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
            print('post')
            #working com
            cursor.execute('UPDATE public."Employee" SET password =%s,email =%s,salary =%s,dept =%s WHERE username=%s' , (request.form['password'],request.form['email'],request.form['salary'],request.form['dept'],request.form['username'],))
            con.commit()
            #cursor.execute('UPDATE public."Employee" SET password =%s WHERE username=%s' , (request.form['password'],request.form['username'],))
            # users=Employee.query.filter(Employee.username==request.form['username'])
          
            # for i in users:


            #     i.password=request.form['password']
            #     i.email=request.form['email']
            #     i.salary=request.form['salary']
            #     i.dept=request.form['dept']
                
            #con.session.commit()
            return redirect(url_for('landing'))

            #     print(i)
            # People.query.filter(People.username==request.form['username']).delete()
            # db.session.commit()
            #return(redirect(url_for('landing')))

            
        else:




           
            return render_template('updatemp.html')
    except:
        return render_template('login2.html')

   
    
    

  