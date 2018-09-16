from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request,abort
from flask_login import login_user,current_user
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from . import auth


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or Password')

    title = "Blog login"
    return render_template('auth/login.html',form = login_form,title=title)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password_hash  = form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
        flash('Account succesfully created')
    return render_template('auth/signup.html',form = form) 