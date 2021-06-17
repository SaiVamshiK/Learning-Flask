from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app=Flask(__name__)

app.config['SECRET_KEY']='e5aeeed185224376330bc6b0a1b0de38'

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

if __name__=='__main__':
    app.run(debug=True)

