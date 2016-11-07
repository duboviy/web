from functools import wraps
from flask import session, url_for, request
from eLibrary import models, db
import eLibrary.views


def is_login_true(login, password):
    users = models.User.query.all()
    for user in users:
        if login == user.login and password == user.password:
            return True
    return False


def process_post_login(form):
    username = None
    if 'logged_in' in session:
        username = session['logged_in']
    elif is_login_true(form.login.data, form.password.data):
        session['logged_in'] = form.login.data
        username = session['logged_in']
    else:
        eLibrary.views.flash(u'Invalid password or login provided', 'error')
    return username


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            eLibrary.views.flash(u'Permission denied', 'error')
            return eLibrary.views.redirect(url_for('books'))

    return wrap


def string_to_list_process(books):
    result = []
    books = filter(lambda a: a.strip() != '', books)

    for i in books:
        if i[0] == ' ':
            i = i[:0] + i[1:]
        if i[len(i) - 1] == " ":
            i[len(i) - 1] = i[len(i) - 1:]
        result.append(i)
    return result


def get_checked_books(books):
    mas = []
    for book in books:
        q = db.session.query(models.Book).filter(models.Book.name == book)
        if db.session.query(q.exists()).scalar():
            curr_book = db.session.query(models.Book).filter(models.Book.name == book).first()
            mas.append(curr_book)
        else:
            mas.append(models.Book(name=book))
    return mas


def get_checked_authors(authors):
    mas = []
    for author in authors:
        q = db.session.query(models.Author).filter(models.Author.name == author)
        if db.session.query(q.exists()).scalar():
            curr_author = db.session.query(models.Author).filter(models.Author.name == author).first()
            mas.append(curr_author)
        else:
            mas.append(models.Author(name=author))
    return mas


def add_author_to_db(author_name):
    books = set(string_to_list_process(request.form['books'].split(',')))
    author = models.Author(name=author_name, books=get_checked_books(books))
    db.session.add(author)
    db.session.commit()


def add_book_to_db(book_name):
    authors = set(string_to_list_process(request.form['authors'].split(',')))
    book = models.Book(name=book_name, authors=get_checked_authors(authors))
    db.session.add(book)
    db.session.commit()
