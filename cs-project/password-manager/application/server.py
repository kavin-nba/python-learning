from flask import Flask, render_template, request, redirect, url_for, session
from pm_database import connect_database, assert_email, authenticate_email, insert_user, insert_password_entry, fetch_user_entry, fetch_password_entry
from werkzeug.security import check_password_hash, generate_password_hash

# from flask_session import Session

password_manager = Flask(__name__)
password_manager.secret_key = 'USE_SECRET_KEY'
database = None


def assert_db():
    if database:
        return database
    return connect_database()


@password_manager.route('/', methods=('GET', 'POST'))
@password_manager.route('/<error>', methods=('GET', 'POST'))
def index(error=None):
    context = {}
    if not session.get('email'):
        return redirect('/login/Please%20login%20first')

    cursor = assert_db()

    if not assert_email(cursor, session.get('email')):
        return redirect('/login/Incorrect email, please login first')

    password_table = fetch_password_entry(cursor, session['email'])
    context['password_table'] = password_table
    if request.method == 'POST':
        username = request.form['username']
        url = request.form['url']
        password = request.form['password']

        print(username, url, password)
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not url:
            error = 'URL is required.'

        if error is None:
            try:
                print("here")
                if insert_password_entry(cursor, session['email'], username, url, password):
                    print("here")
                    return redirect('/#password-page')
            except Exception as e:
                print(e)
                error = 'Database exception'

    context['error'] = error

    return render_template('index.html', context=context)


@password_manager.route('/login', methods=('GET', 'POST'))
@password_manager.route('/login/<error>', methods=('GET', 'POST'))
def login(error=None):
    context = {}
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        context['email'] = email
        context['password'] = password

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                cursor = assert_db()
                if not authenticate_email(cursor, email, password):
                    error = 'Incorrect username or password'
                else:
                    session['email'] = email
                    session['username'] = fetch_user_entry(cursor, email)[0]
                    return redirect(url_for("index"))
            except Exception as e:
                error = 'Database exception'

    context['error'] = error
    context['page'] = 'login'
    return render_template('login.html', context=context)


@password_manager.route('/register', methods=('GET', 'POST'))
@password_manager.route('/register/<error>', methods=('GET', 'POST'))
def register(error=None):
    context = {}
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        context['username'] = username
        context['email'] = email
        context['password'] = password

        if error is None:
            try:
                cursor = assert_db()
                if not assert_email(cursor, email):
                    if not insert_user(cursor, username, email, password):
                        error = 'Database error'
                    else:
                        error = 'Please login'
                        return redirect('/login/' + error)
                else:
                    error = 'Email already exists'
            except Exception as e:
                error = 'Database exception'

    context['error'] = error
    context['page'] = 'register'
    return render_template('login.html', context=context)


@password_manager.route('/logout')
def logout():
    session['email'] = None
    session['username'] = None
    return redirect(url_for('login'))
