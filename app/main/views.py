from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request,abort
from flask_login import login_user,current_user
from ..models import User,Blog
from .forms import BlogForm
from .. import db
from .import main








@main.route("/post/",methods=['GET','POST'])
def postedblog():
    blog_form=BlogForm()
    title = Blog.query.filter_by(title='title').all()
    blog = Blog.query.filter_by(blog='blog').all()
    return render_template('post.html',title=title,blog=blog,blog_form=blog_form)