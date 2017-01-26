# Django Lender

[![Build Status](https://travis-ci.org/codefellows/django_lender.svg?branch=master)](https://travis-ci.org/codefellows/django_lender)

[![Coverage Status](https://coveralls.io/repos/github/codefellows/django_lender/badge.svg?branch=master)](https://coveralls.io/github/codefellows/django_lender?branch=master)

**Author:** Nicholas Hunt-Walker and the class of Python 401d5

An app for managing the lending of books from an online book library.

## Getting Started

Clone this repository into whatever directory you want to work from.

```bash
$ git clone https://github.com/codefellows/django_lender.git
```

Assuming that you have access to Python 3 at the system level, start up a new virtual environment.

```bash
$ cd django_lender
$ python3 -m venv .
$ source bin/activate
```

Once your environment has been activated, make sure to install Django and all of this project's required packages.

```bash
(django_lender) $ pip install -r requirements.pip
```

Navigate to the project root, `lending_library`, and apply the migrations for the app.

```bash
(django_lender) $ cd lending_library
(django_lender) $ ./manage.py migrate
```

Finally, run the server in order to server the app on `localhost`

```bash
(django_lender) $ ./manage.py runserver
```

Django will typically serve on port 8000, unless you specify otherwise.
You can access the locally-served site at the address `http://localhost:8000`.

## Running Tests

Running tests for the `django_lender` is fairly straightforward.
Navigate to the same directory as the `manage.py` file and type:

```bash
(django_lender) $ coverage run manage.py test
```

This will show you which tests have failed, which tests have passed.
If you'd like a report of the actual coverage of your tests, type

```bash
(django_lender) $ coverage report
```

This will read from the included `.coverage` file, with configuration set in the `.coveragerc` file.
Currently the configuration will show which lines were missing from the test coverage.

## Current Models (outside of Django built-ins)

*PatronProfile*

- user (related to the built-in User)
- money_owed (float with a precision of 2 decimal places)
- employed (boolean)
- address (unicode)
- library_id (uuid)

*Book*

- title (str < 256)
- author (str < 256)
- publisher (str < 256)
- isbn (integer)
- year (str < 5; choice field)
- cover_image (image field uploading to `book_covers` in `MEDIA`)
- borrower (related to the PatronProfile)
- status (str < 21; choice field)

## Current URL Routes

- `/`
- `/profile`
- `/profile/<username>`
- `/books`
- `/books/<pk>`
- `/books/new`
- `/books/remove/<pk>`
- `/books/loan/<pk>`
- `/registration/register`
- `/login`
- `/logout`
- `/admin`
