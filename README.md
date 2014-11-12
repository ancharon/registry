registry - Backupify code challenge
=====
Ethan Caldwell


Setup
=====
It is suggested but not required that virtualenv be used to isolate the dependencies this project requires.
If you choose not to use it, skip the first two steps.

Steps to run:
```
  virtualenv env
  source env/bin/activate

  pip install django
  pip install djangorestframework
  pip install django-filter

  cd <path to registry>

  python manage.py syncdb
  python manage.py runserver
```
At this point the registry server should be up and ready for requests as a development server.

Sample Data
===========
To load the sample data supplied with the code challenge, run the loadsampledata.py tool included in this package.
```
  cd tools
  python loadsampledata.py testdata.csv
```
This may take a minute or two depending on data size, as it calls the API for each person instead of writing directly to DB.

API Use
=======
Once the server is up, the API is fully browsable at http://127.0.0.1:8000/
However, as an overview here are some basic operations allowed (not a comprehensive list):

http://127.0.0.1:8000/people/
  * GET
    - returns a list of all people, defaulting to 20/page
    - page size can be configured by adding ?page_size=<num>
    - can filter people by name, age, or other fields by adding ?<field_name>=<foo>
    - can search people fields by adding ?search=<baz>
    - can order people by name, age, or other fields by adding ?ordering=<field_name>
    - (use '-<field_name>' to reverse order)
    - valid filter and ordering fields are: id, first_name, last_name, age, github_acct, third_grade_grad_date
  * POST
    - creates a new person in the registry

http://127.0.0.1:8000/people/#/
  * GET
    - returns a single person, by ID #
  * PUT
    - updates existing person in the registry
  * DELETE
    - removes existing person from the registry

All of these support the OPTIONS verb for additional usage documentation.
