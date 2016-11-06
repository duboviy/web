<h1><img src="https://raw.githubusercontent.com/duboviy/web/master/sinatra-restful-crud/logo.png" height=85 alt="logo" title="logo"> Sinatra/ActiveRecord/Sqlite3 service</h1>
Simple web service with basic RESTful CRUD interface (based on Ruby framework - Sinatra) and very simple JavaScript client (based on Backbone.js)

"<a href="http://www.sinatrarb.com/intro.html">Sinatra</a> is a DSL for quickly creating web applications in Ruby with minimal effort"

"<a href="http://guides.rubyonrails.org/active_record_basics.html">Active Record</a> is the M in MVC - the model - which is the layer of the system responsible for representing business data and logic. Active Record facilitates the creation and use of business objects whose data requires persistent storage to a database."

### Initial Setup ###
Install the gem dependencies specified in our Gemfile:
``bundle install`` 

### Basic usage examples ###
1) Run the Sinatra server:
```bash
ruby app.rb
```

2) Open website in browser at:
```bash
http://127.0.0.1:4567/blogposts
```

3) Open page:
```bash
../client/index.html
```
in any modern browser and look at console log

### Clear/Flush DB ###
The database is just ready to be used from scratch (file hw.db is already in repo).
To create new database, simply run the following two commands:

1) Delete SQLite database: 
```bash
rm -f hw.db
```
2) Launch the migration:
```bash
rake db:migrate
```

### How to play with the CRUD interface ###

You now have a full RESTful CRUD interface to a simple SQLite database backend.
You can play with the interface very easily using simple curl commands:

```bash
$curl localhost:4567/blogposts
[]

$ curl -X POST --data "blogpost[name]=Success" \
localhost:4567/blogposts
true

$ curl -X GET localhost:4567/blogposts
[{"id":1,
"name":"Success",
"created_at":"2014-04-27T04:51:44.040Z",
"updated_at":"2014-04-27T04:51:44.040Z"}]

$ curl -X PUT --data "blogpost[name]=Yay" \
localhost:4567/blogposts/1
true

$ curl -X GET localhost:4567/blogposts/1
{"id":1,
"name":"Yay",
"created_at":"2014-04-27T04:51:44.040Z",
"updated_at":"2014-04-27T04:58:52.225Z"}

$ curl -X DELETE localhost:4567/blogposts
[{"id":1,
"name":"Yay",
"created_at":"2014-04-27T04:51:44.040Z",
"updated_at":"2014-04-27T04:58:52.225Z"}]

$ curl -X GET localhost:4567/blogposts
[]
```

### Supported Ruby and Gems versions ###
Tested on Ruby 2.1.0, 2.2.0 and 2.3.1 with Sinatra 1.4.7, activerecord 5.0 and sqlite3 1.3.12

### Technologies Stack to build RESTful CRUD ###
* Ruby
* Sinatra
* ActiveRecord (ORM)
* JavaScript
* SQLite

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
