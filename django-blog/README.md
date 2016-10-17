##Blog
####A basic blog web application based on Django framework.
####The sample website can be seen at [Blog](http://duboviy.pythonanywhere.com/)

![djangoblog](https://raw.githubusercontent.com/duboviy/web/master/django-blog/blog/static/image/homepage.jpg)

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv env``
2. Activate the virtualenv: ``source env/bin/activate``
3. Install Django: ``pip install -r requirements.txt`` or just typing ``pip install Django==1.8``
4. Run the server: ``python manage.py runserver``
5. Open website in browser at ``http://localhost:8000``

### Basic usage examples ###
1. Activate the virtualenv: ``source env/bin/activate``
2. Run the server: ``python manage.py runserver``
3. Open website in browser at ``http://localhost:8000``

### Supported python versions ###
Tested on Python 3.5.2 with Django 1.8

### Admin mode ###
1. Create superuser (for admin site usage): ``python manage.py createsuperuser``
2. Open website in browser at ``http://localhost:8000/admin`` (enter your created before credentials) and add posts.

### Clear/Flush DB ###
1. Delete SQLite database: ``rm db.sqlite3``
2. Launch the migration: ``python manage.py migrate``

### License ###
**MIT** licensed library. See [LICENSE](LICENSE) for details.

### Contributing ###
If you have suggestions for improving the django-blog, please [open an issue or
pull request on GitHub](https://github.com/duboviy/web/).

### Badges ###
[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/web/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/web/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/web/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/web/)