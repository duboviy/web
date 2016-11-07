from flask import *
from eLibrary import app, db
from eLibrary.forms import *
from eLibrary.process_functions import *
import models



@app.route('/get-book-list', methods=['POST'])
def get_book_list():
    query = models.Book.query.all()

    return json.dumps([
        {'id': book.id, 'name': book.name, 'authors': [author.name for author in book.authors]}
        for book in query
    ])


@app.route('/get-author-list', methods=['POST'])
def get_author_list():
    query = models.Author.query.all()

    return json.dumps([
        {'id': author.id, 'name': author.name, 'books': [book.name for book in author.books]}
        for author in query
    ])

@app.route('/', methods=['GET', 'POST'])
def books():
    form = LoginForm()
    username = None

    if request.method == 'POST' and form.validate_on_submit():
        username = process_post_login(form)

    if 'logged_in' in session:
        username = session['logged_in']

    return render_template('books.html', username=username, form=form,
                           add_form=AddBook(), edit_form=EditBook())


@app.route('/authors', methods=['GET', 'POST'])
def authors():
    login_form = LoginForm()
    username = None

    if request.method == 'POST' and login_form.validate_on_submit():
        username = process_post_login(login_form)

    if 'logged_in' in session:
        username = session['logged_in']

    return render_template('authors.html', username=username,
                           form=login_form, add_form=AddAuthor(), edit_form=EditAuthor())


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('books'))


@app.route('/remove-author/<auth_id>')
@login_required
def remove_author(auth_id):
    author = db.session.query(models.Author).filter(models.Author.id == auth_id).first()
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('authors'))


@app.route('/remove-book/<book_id>')
@login_required
def remove_book(book_id):
    book = db.session.query(models.Book).filter(models.Book.id == book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books'))


@app.route('/add-author', methods=['POST'])
@login_required
def add_author():
    if request.form['name'].strip() != "":
        author_name = request.form['name']
        q = db.session.query(models.Author).filter(models.Author.name == author_name)
        if db.session.query(q.exists()).scalar():
            flash(u'This name is already exists', 'error')

        add_author_to_db(author_name)
    else:
        flash(u'Field name can`t be empty', 'error')
    return redirect(url_for('authors'))


@app.route('/add-book', methods=['POST'])
@login_required
def add_book():
    if request.form['name'].strip() != "":
        book_name = request.form['name']
        q = db.session.query(models.Book).filter(models.Book.name == book_name)
        if db.session.query(q.exists()).scalar():
            flash(u'This name is already exists', 'error')

        add_book_to_db(book_name)
    else:
        flash(u'Field name can`t be empty', 'error')
    return redirect(url_for('books'))


@app.route('/edit-book/<id_book>', methods=['POST'])
@login_required
def edit_book(id_book):
    book = db.session.query(models.Book).filter(models.Book.id == id_book).first()
    authors = set(string_to_list_process(request.form['authors'].split(',')))

    name_book = request.form['name']

    if not name_book and not authors:
        flash(u'Changes have not been applied', 'error')
        return redirect(url_for('books'))

    if not name_book.strip():
        name_book = book.name
    else:
        q = db.session.query(models.Book).filter(models.Book.name == name_book)
        if db.session.query(q.exists()).scalar() and name_book != book.name:
            flash(u'This name is already exists', 'error')
            return redirect(url_for('books'))

    db.session.delete(book)
    db.session.commit()
    book = models.Book(name=name_book, authors=get_checked_authors(authors))
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('books'))


@app.route('/edit-author/<id_author>', methods=['POST'])
@login_required
def edit_author(id_author):
    author = db.session.query(models.Author).filter(models.Author.id == id_author).first()
    books = set(string_to_list_process(request.form['books'].split(',')))

    name_auth = request.form['name']

    if not name_auth.strip() and not books:
        flash(u'Changes have not been applied', 'error')
        return redirect(url_for('authors'))

    if not name_auth.strip():
        name_auth = author.name
    else:
        q = db.session.query(models.Author).filter(models.Author.name == name_auth)
        if db.session.query(q.exists()).scalar() and name_auth != author.name:
            flash(u'This name is already exists', 'error')
            return redirect(url_for('authors'))

    db.session.delete(author)
    db.session.commit()
    author = models.Author(name=name_auth, books=get_checked_books(books))
    db.session.add(author)
    db.session.commit()

    return redirect(url_for('authors'))
