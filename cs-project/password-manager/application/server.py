from flask import Flask, render_template, request, redirect, url_for, session
from pm_database import connect_database, check_email, authenticate_email, insert_user, insert_password_entry
from werkzeug.security import check_password_hash, generate_password_hash
# from flask_session import Session

password_manager = Flask(__name__)
password_manager.secret_key = 'hellohello'
# password_manager.config['SESSION_PERMANENT'] = False
# Session(password_manager)
database = None


def assert_db():
    if database:
        return database
    return connect_database()


@password_manager.route('/')
def index():
    return render_template('index.html')


@password_manager.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    # if session and session.get('name'):
    #     print(session['name'])
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                cursor = assert_db()
                if not authenticate_email(cursor, email, password):
                    error = 'login error'
                else:
                    session['email'] = email
                    return redirect(url_for("index"))
            except Exception as e:
                error = 'database exception'

    context = {'error': error}
    return render_template('login.html', context=context)


@password_manager.route('/register', methods=('GET', 'POST'))
def register():
    error = None
    # session['name'] = 'hihello'
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

        if error is None:
            try:
                cursor = assert_db()
                if not check_email(cursor, email):
                    if not insert_user(cursor, username, email, password):
                        error = 'database error'
                    else:
                        session['error'] = 'Please login.'
                        return redirect(url_for("login"))
            except Exception as e:
                error = 'database exception'

    context = {'error': error}
    return render_template('login.html', context=context)
