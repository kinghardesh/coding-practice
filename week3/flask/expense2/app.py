from flask import  Flask,render_template,redirect,request,url_for
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
        expense_description=request.form['tasks']
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
        return render_template('exp.html')
 
@app.route('/table')
def table():
    tasks = expense1.query.order_by(expense1.date_created).all()
    return render_template('table.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete():
    task_to_delete=task.get_or_404(id)
    try:
        db.session.commit()
        return redirect('/table')
    except:
        return "there is a issue deleting the task"

@app.route('/update/<int:id>',methods=('GET','POST'))
def update():
    if request.method=='POST':
        expense_description=request.form['content']
        expense_amount=request.form['amount']
        new_task=expense1(
            content=expense_description,
            amount=expense_amount
        )
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/table')
        except:
            return "there is a issue updating"
    else:
        return render_template('update.html')

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) 