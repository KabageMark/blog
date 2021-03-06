from flask_login import login_required
from flask import render_template,redirect,url_for, flash,request,abort
from flask_login import login_user,current_user
from ..models import User,Blog,Comment
from .forms import BlogForm,CommentForm
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

        postblog = Blog(blog=form.blog.data,title=form.title.data)

        postblog.save_blog()
        return redirect(url_for('.postedblog'))
    return render_template('post.html',postblog=postblog,form=form)


@main.route("/",methods=['GET','POST'])
def postedblog():
    '''
    this is view funtion for posting a blog 
    '''
    blog_form=BlogForm()
    comment_form=CommentForm()
    if comment_form.validate_on_submit():

        postcomment = Comment(comment=comment_form.comment.data)

        postcomment.save_comment()

    title = blog_form.title.data  
    blog = blog_form.blog.data
    Comments = comment_form.comment.data
    

    postblog= Blog.query.all()
    postcomment=Comment.query.all()

    return render_template('index.html',title=title,comment=postcomment,blog=postblog,blog_form=blog_form,comment_form=comment_form)