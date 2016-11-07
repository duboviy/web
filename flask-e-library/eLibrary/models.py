from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from eLibrary import db


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    login = db.Column(db.String(80), index=True, unique=True)
    password = db.Column(db.String(32), index=True)

    def __repr__(self):
        return '<User %r>' % self.login


books = Table(
    'keywords', db.Model.metadata,
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('book.id'), primary_key=True)
)


class Book(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True)
    authors = relationship("Author", secondary=lambda: books)

    def __repr__(self):
        return '<Book %r>' % self.name


class Author(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    books = relationship("Book", secondary=lambda: books)


    def __repr__(self):
        return '<Author %r>' % self.name
