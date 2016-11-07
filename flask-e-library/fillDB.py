from eLibrary import models, db

u = models.User(login="root", password="root")
db.session.add(u)
db.session.commit()


book = models.Book(name="Accelerated C++")
book.authors.append(models.Author(name="Andrew Koenig"))
book.authors.append(models.Author(name="Barbara Moo"))
db.session.add(book)
db.session.commit()

author = models.Author(name="Bruce Eckel")
author.books.append(models.Book(name="Using C++"))
author.books.append(models.Book(name="Thinking in C++"))
author.books.append(models.Book(name="Thinking in Java"))
db.session.add(author)
db.session.commit()
