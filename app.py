
from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Create the tables
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    entries = db.relationship('Entry', backref='author', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username_lower = form.username.data.lower()
        existing_user = User.query.filter_by(username=username_lower).first()
        if existing_user:
            flash('That username is already taken. Please choose a different one.')
            return redirect(url_for('register'))
        user = User(username=username_lower)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Successfully logged in!')
            return redirect(url_for('view_all_entries'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/entry/new', methods=['GET', 'POST'])
@login_required
def new_entry():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        entry = Entry(title=title, content=content, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Entry successfully created!')
        return redirect(url_for('view_all_entries'))
    return render_template('entry.html')

@app.route('/user')
@login_required
def user():
    if not current_user.is_authenticated:
        # Redirect to login if user is not authenticated
        return redirect(url_for('login'))
    entries = Entry.query.filter_by(author=current_user).order_by(Entry.timestamp.desc()).all()
    return render_template('user.html', entries=entries)

@app.route('/entries')
@login_required
def view_all_entries():
    entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.timestamp.desc()).all()
    return render_template('view_entries.html', entries=entries)

@app.route('/entry/<int:entry_id>')
def view_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    return render_template('view_entry.html', entry=entry)

@app.route('/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if request.method == 'POST':
        entry.title = request.form['title']
        entry.content = request.form['content']
        db.session.commit()
        flash('Entry successfully updated!')
        return redirect(url_for('view_all_entries'))
    return render_template('entry.html', entry=entry)

@app.route('/entry/<int:entry_id>/delete', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash('Entry successfully deleted!')
    return redirect(url_for('view_all_entries'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
