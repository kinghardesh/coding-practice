from flask import  Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense1.db'
db=SQLAlchemy(app)
class expense1(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    amount=db.Column(db.Integer,default=True)
    def __repr__(self):
        return f"<Task{self.id}>"
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        expense_description=request.form['content']
        expense_amount=request.form['amount']
        new_task=expense1(
            content=expense_description,
            amount=expense_amount
        )
        try:
            db.session.add(new_task)
            db.session.commit
            return redirect ('/')
        except:
            return 'there is a 404 error'
    else:
        return render_template('index.html',tasks=tasks)
 
@app.route('/table')
def table():
    if request.method=='post':
        
        
        
    return render_template('table.html')


if __name__=="__main__":
   app.run(debug=True) 