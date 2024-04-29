from flask import Flask
from flask_login import LoginManager
from model import db, Users, SesameKey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_SmomtcoolaSEcret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sesame.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'authentication.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

with app.app_context():

    db.create_all()

from authentication import authentication as auth_blueprint
app.register_blueprint(auth_blueprint)

from main import main as main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)