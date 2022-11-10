from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:550215@localhost:5432/usersofpy"
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
class NFTS(db.Model):
    nft_name = db.Column(db.String(), primary_key=True) 
    url = db.Column(db.String())
    address = db.Column(db.String())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('form.html', name=current_user.username)
@app.route('/dashboard',methods = ['POST'])
@login_required
def dashboard2():
    address = request.form['Name']
    x = NFTS.query.filter_by(address=address).first()
    if x is None:
        url = f"https://solana-gateway.moralis.io/nft/mainnet/{address}/metadata"
        headers = {
            "accept": "application/json",
            "X-API-Key": "S77RJTmiMoBbTQTEed5MExSDfHQ2HolnDEXy7GZRoo3Eah6t1YAR20dfdGIJASaT"
        }    
        response = requests.get(url, headers=headers)
        info = response.text
        i = info.find("name")+7
        i2 = 0
        for x in range(i, len(info)):
            if info[x] == '"':
                i2 = x
                break
        i3 = info.find("metadataUri")+14
        i4 = 0
        for x in range(i3, len(info)):
            if info[x] == '"':
                i4 = x
                break
        name = info[i:i2]
        url = info[i3:i4]
        nft = NFTS(nft_name = name, url = url, address= address)
        db.session.add(nft)
        db.session.commit()
    nft = NFTS.query.filter_by(address=address).first()
    return render_template('data.html', address = address, name = nft.nft_name , url = nft.url)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
