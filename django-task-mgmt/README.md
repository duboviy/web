<h1><img src="https://raw.githubusercontent.com/duboviy/web/master/logo.png" height=85 alt="logo" title="logo"> django-task-mgmt</h1>
Web service to provide task / issues / TODOs tracking management.
 
Service includes following interfaces:
* RESTful CRUD API;
* Web Pages

<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/dashboard_page.png">

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv env``
2. Activate the virtualenv: ``source env/bin/activate``
3. Install Django and requirements: ``pip install -r requirements.txt``
4. Launch syncdb: ``python manage.py syncdb``
5. Run the server: ``python manage.py runserver``

### Basic usage examples ###
1. Activate the virtualenv: ``source env/bin/activate``
2. Run the server: ``python manage.py runserver``
3. Open website in browser at ``http://localhost:8000/``

### Simple Rest Api ###
RESTful CRUD API allows to:

Create:
```bash
curl -i --user test:test -H "Content-Type: application/json" -H "Accept: application/json" -X POST \
--data '{"done": false, "priority": 2, "title": "asdasd task", "user": "/api/v1/auth/user/2/"}' http://127.0.0.1:8000/api/v1/task/
```

Update:
```bash
curl -i --user test:test -H "Content-Type: application/json" -H "Accept: application/json" -X PATCH \
--data '{"second": "second task"}' http://127.0.0.1:8000/api/v1/task/5/
```

Delete:
```bash
curl -i --user test:test --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/task/5/
```

### Web Pages ###
Open website in browser at ``http://localhost:8000/`` and you'll see following pages flow:

<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/login_screen.png">
<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/right_side_tile_bar_menu.png">
<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/register_page.png">
<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/new_task_page.png">
<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/dashboard_page.png">
<img src="https://raw.githubusercontent.com/duboviy/web/master/django-task-mgmt/screenshots/edit_task_page.png">

### Clear/Flush DB ###
1. Delete SQLite database: ``rm development.sqlite3``
2. Launch syncdb: ``python manage.py syncdb``

### Supported python versions ###
Tested on Python 2.7.8 with Django 1.6.2

### Badges ###
[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/web/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/web/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/web/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/web/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/web/)
