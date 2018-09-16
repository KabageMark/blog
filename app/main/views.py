from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request,abort
from flask_login import login_user,current_user
from ..models import User,Blog
from .forms import BlogForm
from .. import db
from .import main

@main.route("/post/",methods=['GET','POST'])
@login_required
def postblog():
    '''
    this is view funtion for posting a blog 
    '''
    postblog=[]
    form=BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data

        postblog = Blog(blog=blog,title=title)

        postblog.save_blog()
        return redirect(url_for('.postedblog'))
    return render_template('post.html',postblog=postblog,form=form)


@main.route("/",methods=['GET','POST'])
def postedblog():
    '''
    this is view funtion for posting a blog 
    '''
    blog_form=BlogForm()
    title = Blog.query.filter_by(title='title').all()
    blog = Blog.query.filter_by(blog='blog').all()
    return render_template('index.html',title=title,blog=blog,blog_form=blog_form)