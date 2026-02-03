from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///aadhar.db'
db=SQLAlchemy(app)
class Aadhar(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    specialized_no=db.Column(db.Integer,default=0)
    def __repr__(self):
        return f"<Aadhar {self.id}>"
@app.route('/',methods=['GET','POST']) 
def index():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        specialized_no=request.form['specialized_no']
        new_aadhar=Aadhar(
            name=name,
            email=email,
            specialized_no=specialized_no
        )
        try:
            db.session.add(new_aadhar)
            db.session.commit()
            return redirect('/aadhar')
        except:
            return "There was an issue adding your aadhar"
    else:
        return render_template("form.html")
