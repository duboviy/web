<h1><img src="https://raw.githubusercontent.com/duboviy/web/master/logo.png" height=85 alt="logo" title="logo"> django-employer-department</h1>
Very simple webserver with basic REST API interface, admin panel and few tables:

Employees:
id
first name,
last name,
department_id

Departments:
id,
name

Admin panel allows to add/update/delete and search these tables.

An API interface on top of Django, where the results are in JSON format:
a) get_users - returns a list of the users, with their department name
b) get_user - receives as key the user's ID, and returns the user with it's department name.

--
Example:
```bash
curl http://127.0.0.1:8000/api/get_users/
```

```bash
curl http://127.0.0.1:8000/api/get_user/1/
```

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv env``
2. Activate the virtualenv: ``source env/bin/activate``
3. Install Django: ``pip install -r requirements.txt`` or just typing ``pip install Django==1.5.1``
4. Run the server: ``python manage.py runserver``
5. Open website in browser at ``http://localhost:8000/api/get_users/``

### Basic usage examples ###
1. Activate the virtualenv: ``source env/bin/activate``
2. Run the server: ``python manage.py runserver``
3. Open website in browser at ``http://localhost:8000/api/get_users/``

Example:
```bash
curl http://127.0.0.1:8000/api/get_users/
curl http://127.0.0.1:8000/api/get_user/1/
```

### Admin mode ###
1. Create superuser (for admin site usage): ``python manage.py createsuperuser``
2. Open website in browser at ``http://localhost:8000/admin`` (enter your created before credentials) and add users/departments.

### Clear/Flush DB ###
1. Delete SQLite database: ``rm development.sqlite3``
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