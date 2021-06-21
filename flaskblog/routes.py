from flask import render_template,url_for,flash,redirect,request
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm,LoginForm,ProfileUpdateForm,NewPost
from flaskblog import app,db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required

@app.route("/")
@app.route("/home")
def home():
    posts=Post.query.all()
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Login Failed!','danger')
    return render_template('login.html',title='Login',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        u1=User(username=form.username.data,password=hashed_password,email=form.email.data)
        db.session.add(u1)
        db.session.commit()
        flash(f'Account created for {form.username.data}!!!','success')
        return redirect(url_for('login'))        
    return render_template('register.html',title='Register',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form=ProfileUpdateForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash(f'Account Updated Successfully','success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file=url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template('account.html',title='Account Page',image_file=image_file,form=form)

@app.route("/post-new",methods=['GET','POST'])
@login_required
def newPost():
    form=NewPost()
    if form.validate_on_submit():
        p1=Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(p1)
        db.session.commit()
        flash(f'Post creation successful!','success')
        return redirect(url_for('home'))
    return render_template('new_post.html',title='Create-Post',form=form)


@app.route("/post/<int:post_id>")
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html',title=post.title,post=post)