from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import usermixin
from flask_wtf import wtforms
from wtforms import StringField,PasswordField,SubmitField
from wrforms.validators import inputRequired,Length,validatorsError

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

class user(db.Model,):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    password_hash=db.Column(db.String(30), nullable=False)

class registerForm(wtforms.Form):
    name=StringField('name',validators=[inputRequired(),Length(min=4,max=30)])
    password=PasswordField('password',validators=[inputRequired(),Length(min=4,max=30)])
    submit=SubmitField('Register')
    def validate_name(self,name):
        existing_user=user.query.filter_by(name=name.data).first()
        if existing_user:
            raise validatorsError('Username already exists. Please choose a different one.')
class loginForm(wtforms.Form):
    name=StringField('name',validators=[inputRequired(),Length(min=4,max=30)])
    password=PasswordField('password',validators=[inputRequired(),Length(min=4,max=30)])
    submit=SubmitField('Login')
    

@app.route('/')
def home():
    return render_template('basic_page.html')
    
@app.route('/form', methods=('get','post'))
def index():
    if request.method=='post':
        content=request.form['content']
        amount=int(request.form['amount'])
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

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)