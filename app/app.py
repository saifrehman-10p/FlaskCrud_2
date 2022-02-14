from flask import Flask,request,session
from flask import flash
from flask import url_for
from flask import redirect
from flask_session import Session
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import random
#from flask.ext.sqlalchemy import exc


app=Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost/Test'
db=SQLAlchemy(app)
from database.models.Employee import Employ
con = psycopg2.connect(database="Test", user="postgres", password="12345", host="127.0.0.1", port="5432")
SECRET_KEY = 'the random string'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cursor = con.cursor()


if __name__ == '__main__':
    session['secrrt']='sec'

    app.run(host="0.0.0.0", port=5000, debug=True)

#Basic Function For Redirecting Login As Landing Page

@app.route('/')
def index():
    db.create_all()
    return redirect(url_for('login'))



#Function For Redirecting To Employe Add Page(Get Method)

@app.route('/show')
def show():

    
    
    return redirect(url_for('eadd'))

#Function For Employee Add Page

@app.route('/eadd',methods=['GET','POST'])
def eadd():
    print(session.get("name"))
    if session.get("name"):
        try:
            


        
    




    
            if request.method=='POST':




                print("heloo")
                username =request.form['username']
                password =request.form['password']
                email=request.form['email']
                salary=request.form['salary']
                dept=request.form['dept']

                
  

                employee=Employ(username,password,email,salary,dept)
               
                db.session.add(employee)
                db.session.commit()
                
               

                return redirect(url_for('show'))
            else:
                edata=Employ.query.filter()
                return render_template('employee.html',Result=edata)
        except Exception as e:
            edata=Employ.query.filter()
            print('yo',str(e))
            return render_template('employee.html',Result=edata)

    else:
        
        return redirect(url_for('login'))

#Function For Employee Delete                   

@app.route('/edel/<username>',methods=['GET','POST'])
def edel(username):
    if session.get("name"):
        try:



            if request.method=='POST':

                Employ.query.filter(Employ.username==username).delete()
                db.session.commit()
                return redirect(url_for('eadd'))  
            else:

                Employ.query.filter(Employ.username==username).delete()
                db.session.commit()

                return redirect(url_for('eadd')) 
        except:
            return redirect(url_for('eadd'))
    else:
        return redirect(url_for('login'))


#Function For Employee Update 

@app.route('/eupdate',methods=['GET','POST'])
def eupdate():
    if session.get("name"):
    
        try:

            if request.method=='POST':
                cursor.execute('UPDATE public."Employ" SET password =%s,email =%s,salary =%s,dept =%s WHERE username=%s' , (request.form['password'],request.form['email'],request.form['salary'],request.form['dept'],request.form['username'],))
                con.commit()
                return redirect(url_for('eadd'))
            else:

                return redirect(url_for('eadd'))

        except:
            return redirect(url_for('eadd'))
    else:
        return redirect(url_for('login'))


        

        

#Function For Employee Login  

@app.route('/login',methods=['POST','GET'])
def login():
    error=None



    try:



        
        if request.method=='POST':
            print('hello')





            edata=Employ.query.filter(Employ.username==request.form['username'])
            print('hello1')





            for i in edata:


                



                print(i.username)
                

                if request.form['username'] == i.username and request.form['password'] == i.password:
                    print('saifyyy')
                    
                    session["name"] = request.form.get("username")


                    

                    return redirect(url_for('eadd'))
                    
                else:
                   
                    return render_template('login.html')
                    
        else:


            return render_template('login.html')
    except Exception as e:

        #print(e,'EKKK')
        # return "error hello", 400
        return render_template('login.html')
        







