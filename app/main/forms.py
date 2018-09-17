from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField,BooleanField,RadioField,TextAreaField
from wtforms.validators import DataRequired,Required, Length , Email , EqualTo
from ..models import User,Blog


class BlogForm(FlaskForm):
    blog = TextAreaField('Blog',validators=[DataRequired()])

    title = StringField('title',validators=[DataRequired()])

    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    comment = StringField('comment')

    submit = SubmitField('submit')