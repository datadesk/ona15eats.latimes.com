ONA15 Eats
==========

We wanted to make a simple, approachable guide to eating and exploring while you're at the ONA15 conference. Using some of our open source software like [Django Bakery](https://github.com/datadesk/django-bakery) and [Django Project Template](https://github.com/datadesk/django-project-template) we made a simple site with restaurant and activity suggestions from the [L.A. Times Data Desk](http://www.latimes.com/local/datadesk/). Let us know if you have any suggestions, and patches are always welcome!

Getting started
---------------

Requirements:

* Python
* SQLite
* virtualenv
* Git

Create a virtualenv to store the codebase.

```bash
$ virtualenv eat-ona
```

Activate the virtualenv.

```bash
$ cd eat-ona
$ . bin/activate
```

Clone the git repository from GitHub.

```bash
$ git clone git@github.com:datadesk/eat-ona.git repo
```

Enter the project and install its dependencies.

```bash
$ cd repo
$ pip install -r requirements.txt
```

Make a copy of settings_private.py and configure any local settings you need to publish.

```bash
$ cp project/settings_private.template project/settings_private.py
$ vim project/settings_private.py
```

Let Django create the database tables you need.

```bash
$ python manage.py migrate
```

Load our recommendations.

```bash
$ python manage.py loadalldata
```

Run the test server for the first time.

```bash
$ python manage.py runserver
```

Publishing
----------

We're using [Django Bakery](https://github.com/datadesk/django-bakery) to publish the site as static files hosted on [Amazon S3](https://aws.amazon.com/s3/).

This requires that you configure ``project/settings_private.py`` to connect to a bucket in your Amazon S3 account.

```python
AWS_ACCESS_KEY_ID = '' # The shorter one
AWS_SECRET_ACCESS_KEY = '' # The longer one
AWS_BUCKET_NAME = '' # The name of your bucket to host the files
```

If you need to update the site the first thing you have to do it "build" it, which generates all of the HTML.

```bash
$ python manage.py build
```

Then you publish, which syncs all of the files to your Amazon S3 bucket.

```bash
$ python manage.py publish
```

That's it!
