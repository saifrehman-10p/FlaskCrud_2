
from app import db

class Employ(db.Model):
    __tablename__='Employ'
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
    def __repr__(self):
        return '<Employ {}>'.format(self.id)