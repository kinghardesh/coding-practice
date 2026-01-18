from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///expense.db'
db=SQLAlchemy(app)
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    expense = db.Column(db.Integer,default=True)
    def __repr__(self):
        return f"<Task{self.id}>"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method== 'POST':
        Expense_discription=request.form['content']
        expense_amount=request.form['expense']
        new_task=Expense(
            content=Expense_discription,
            expense=expense_amount
        )
        try:
            db.Session.add(new_task)
            db.Session.commit()
            return redirect('/')
        except:
            return 'there is a issue adding the description of the table'
    else:
        tasks=Expense.query.order_by(Expense.date_created).all()
        return render_template('index.html',tasks=tasks)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)




