from flask import Blueprint, render_template, redirect, url_for, request, flash
from model import db, Users
from flask_login import login_user, login_required, logout_user
from security import Hashing

authentication = Blueprint('authentication', __name__)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        password_hash = Hashing(password).hash_string()

        check_user = Users.query.filter_by(username=username).first()

        if check_user.password == password_hash:
            login_user(check_user, remember=remember)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Please check your login details and try again!')
            return redirect(url_for('authentication.login'))

    elif request.method == 'GET':
        return render_template('login.html')


@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('authentication.login'))