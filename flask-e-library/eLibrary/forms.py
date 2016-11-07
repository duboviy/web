from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Length


class LoginForm(Form):
    login = TextField('login', validators=[Length(min=4, max=25)])
    password = PasswordField('password', validators=[Required()])


class AddBook(Form):
    name = TextField('name', validators=[Required()])
    authors = TextField('authors')


class AddAuthor(Form):
    name = TextField('name', validators=[Required()])
    books = TextField('books')


class EditBook(Form):
    name = TextField('name')
    authors = TextField('authors')


class EditAuthor(Form):
    name = TextField('name')
    books = TextField('books')
