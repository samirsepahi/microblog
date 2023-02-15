from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/songs')
def songs():
    user = {'username': 'Samuel'}
    songs_list = [
        {
            'title': 'Let It Be', 
            'artist': 'Beetles'
        },
        {
            'title': 'Billy Jean',
            'artist': 'Michael Jackson'
        }
    ]
    return render_template('songs.html', songs_list=songs_list)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/snowman', methods=['GET', 'POST'])
def snowman():
    form = snowmanForm()
    return render_template('snowman.html', title='Submit Guesses', form=form)
