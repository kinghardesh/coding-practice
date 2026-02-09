from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from model import spending,user
app=Flask(__name__)
app.config['SQLAlchemy_Database_uri']='sqlite:///spending.db'
db=SQLAlchemy(app)
class spending(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(30), nullable=False)
    amount=db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(30),nullable=True)
    date_created=db.Column(db.datetime,default=datetime.utcnow)
    def __repr__(self):
        return f"<spending {self.id}>"

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    password_hash=db.Column(db.String(30), nullable=False)
    
@app.route('/', methods=('get','post'))
def index():
    if request.method=='post':
        content=request.form['content']
        amount=request.form['amount']
        category=request.form['category']
        new_task=spending(
            content=content,
            amount=amount,
            category=category
        )
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'there is a error adding the task'
    else:
        return render_template('form.html')

@app.route('/login')
def login():
    return 'login page'

@app.route('/signup')
def signup():
    return 'signup page'

@app.route('/logout')
def logout():
    return 'logout page'
