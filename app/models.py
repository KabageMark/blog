from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask_login import UserMixin
from  . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    '''
    this is a models class registering users
    '''
              
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
       
    @property
    
    def password(self):
        '''
        password function
        '''
        raise AttributeError('You cannnot read the password attribute')

    
    def set_password(self, password):
        '''
        function for setting password
        '''

        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        '''
      password verification function
        '''
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User { self.username}'

class Blog(db.Model):
   __tablename__='blog'

   '''
   class for for posting a blog
   
   '''

   id = db.Column(db.Integer,primary_key=True)
   title = db.Column(db.String(255))
   blog = db.Column(db.String(255))
   comments = db.relationship('Comment',backref='blog',lazy='dynamic')
   user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   



   def save_blog(self):
       db.session.add(self)
       db.session.commit()



class Comment(db.Model):
   __tablename__='comments'

   '''
   class for for posting a comment
   
   '''

   id = db.Column(db.Integer,primary_key=True)
   comment = db.Column(db.String(255))
   blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
   
    

   def save_comment(self):
       db.session.add(self)
       db.session.commit()

   
   @classmethod
   def get_comments(cls,id):
        comments = Blog.query.filter_by(user_id=id).all()
        return comments   