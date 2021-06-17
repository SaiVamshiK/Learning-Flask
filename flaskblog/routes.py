from flask import render_template,url_for,flash,redirect
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog import app

posts=[
    {
        'author':'Sai Vamshi',
        'title':'Blog Post 1',
        'content':'First blog post',
        'date_posted':'April 18 2021'
    },
    {
        'author':'KL Rahul',
        'title':'Blog Post 2',
        'content':'Second blog post',
        'date_posted':'April 20 2021'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash(f'Login Successful!','success')            
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed!','danger')
    return render_template('login.html',title='Login',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!!!','success')
        return redirect(url_for('home'))        
    return render_template('register.html',title='Register',form=form)