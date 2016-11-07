<h1><img src="https://raw.githubusercontent.com/duboviy/web/master/logo.png" height=85 alt="logo" title="logo"> flask-e-library</h1>
Web application to provide e-library management.

### How to install ###
First, you need to install requirements:
```bash
pip install -r requirements.txt
```

To deploy db and fill it with test data:
```bash
python createAndFillDB.py
```

Now, your server is ready to start, run:
```bash
python runserver.py
```

### Technologies Stack to build RESTful CRUD ###
* Python
* Flask
* SQLAlchemy
* SQLite
* Jinja2 Templates
* WTForms
* jQuery
* Bootstrap

### Features ###

1. Editing (available for an authorized user):
* Book list management: add / remove / edit the book.
* Managing the list of authors: add / remove / edit the author.
* Connection between books and authors - many to many.

2. Book Search by title or author (available for all users (not only authorized)).

3. Authentication and Authorization.

4. The user data validated before being stored in the database.

5. The project contain SQL-scripts for database deployment and filling it with test data.


### Supported Python versions ###
Tested on Python 2.7


### License ###
**MIT** licensed library. See [LICENSE.txt](LICENSE.txt) for details.

### Contributing ###
If you have suggestions for improving the django-todo, please [open an issue or
pull request on GitHub](https://github.com/duboviy/web/).

### Badges ###
[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/web/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/web/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/web/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/web/)
