from flask import Flask, render_template, request, redirect, url_for
from pm_database import connect_database, check_email, authenticate_email, insert_user, insert_password_entry
from werkzeug.security import check_password_hash, generate_password_hash

password_manager = Flask(__name__)
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

            except Exception as e:
                error = 'database exception'

        else:
            return redirect(url_for("index"))
    context = {}
    context['error'] = error
    return render_template('login.html', context=context)


@password_manager.route('/register', methods=('GET', 'POST'))
def register():
    error = None
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
                print('hi1')
                cursor = assert_db()
                print('hi2')
                if not check_email(cursor, email):
                    print('hi3')
                    if not insert_user(cursor, username, email, password):
                        print('hi4')
                        error = 'database error'

            except Exception as e:
                error = 'database exception'

        else:
            return redirect(url_for("login"))
    context = {}
    context['error'] = error
    return render_template('register.html', context=context)
