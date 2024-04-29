from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from model import SesameKey
import subprocess
import os

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == "GET":
        return render_template('dash.html')
    if request.method == "POST":
        key = request.form.get("key")
        file_read = request.form.get("fileread")
        check_key = SesameKey.query.filter_by(key=key).first()
        if check_key is not None:
            num = 107
            stk = chr(num)
            secret = ''.join([chr(ord(x) ^ ord(stk)) for x in key])
            with open("temp_secret", "w") as temp:
                temp.write(secret)
            command = f"sudo sesame -i temp_secret -r {file_read}"
            run = subprocess.check_output(command, shell=True)
            run = run.decode('utf-8')

            os.system(f"rm -rf temp_secret")

            return render_template('dash.html', message="It Works")
        else:
            return render_template('dash.html', message="Wrong Key")
