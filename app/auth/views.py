from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request,abort
from flask_login import login_user,current_user
from ..models import User
from .forms import RegistrationForm
from .. import db
from . import auth




@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password_hash  = form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
        title = "New Account"
        flash('Account succesfully created')
    return render_template('auth/signup.html',form = form)