from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin,login_user,logout_user,login_required,LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError
from werkzeug.security import check_password_hash
from flask_bcrypt import Bcrypt

app=Flask(__name__)

# Secret key (needed for forms + sessions)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Single database (recommended)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spending.db'

# Disable modification tracking (performance)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class spending(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(30), nullable=False)
    amount=db.Column(db.Integer, nullable=False)
    category=db.Column(db.String(30),nullable=True)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return f"<spending {self.id}>"

class user(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    password_hash=db.Column(db.String(30), nullable=False)

class registerForm(FlaskForm):
        name=StringField('name',validators=[InputRequired(),Length(min=4,max=30)],render_kw={"placeholder": "Username"})
        password=PasswordField('password',validators=[InputRequired(),Length(min=4,max=30)],render_kw={"placeholder": "Password"})
        submit=SubmitField('Register')
        def validate_name(self,name):
            existing_user=user.query.filter_by(name=name.data).first()
            if existing_user:
                raise ValidationError('Username already exists. Please choose a different one.')

class loginForm(FlaskForm):
    name=StringField('name',validators=[InputRequired(),Length(min=4,max=30)],render_kw={"placeholder": "Username"})
    password=PasswordField('password',validators=[InputRequired(),Length(min=4,max=30)],render_kw={"placeholder": "Password"})
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

@app.route('/table')
def table():
    expenses=spending.query.all()
    return render_template('table.html', expenses=expenses)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=spending.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'there is a error deleting the task'



@app.route('/signup')
def signup():
    form=registerForm()
    if form.validate_on_submit():
        hashed_password=generate_password_hash(form.password.data)
        new_user=user(name=form.name.data,password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('signup.html', form=form)

@app.route('/login')
def login():
    form=loginForm()
    if form.validate_on_submit():
        user=user.query.filter_by(name=form.name.data).first()
        if user and check_password_hash(user.password_hash,form.password.data):
            login_user(user)
            return redirect('/form')
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)