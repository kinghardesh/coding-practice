from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contacts.db'
db=SQLAlchemy(app)
class Contacts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    phone=db.Column(db.Integer,default=0)
    def __repr__(self):
        return f"<Contact {self.id}>"
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        new_contact=Contacts(
            name=name,
            email=email,
            phone=phone
        )
        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/contact')
        except:
            return "There was an issue adding your contact"
    else:
        return render_template("form.html")
@app.route('/contact')
def contact():
    contacts=Contacts.query.order_by(Contacts.name).all()
    return render_template("contact.html",contacts=contacts)
@app.route('/delete/<int:id>')
def delete(id):
    contact_to_delete=Contacts.query.get_or_404(id)
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect('/contact')
    except:
        return "There was a problem deleting that contact"

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    contact=Contacts.query.get_or_404(id)
    if request.method=="POST":
        contact.name=request.form['name']
        contact.email=request.form['email']
        contact.phone=request.form['phone']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your contact"
    else:
        return render_template("update.html",contact=contact)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)