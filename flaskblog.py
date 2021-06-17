from flask import Flask,render_template,url_for
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

if __name__=='__main__':
    app.run(debug=True)

