# Reproducer for Django Issue #34796

https://code.djangoproject.com/ticket/34796

## Usage

Install dependencies and create the database

```
virtualenv .venv
pip install Django
cd mysite
```

Run migrations and then inspect the database records. Observe that there are
records in the `places_place` table that correspond to records from the
`PostOffice` model that was deleted in migration `0003`.

```
python manage.py migrate
echo "SELECT * FROM places_place;" | sqlite3 db.sqlite3
```

Expected:

```
$ echo "SELECT * FROM places_place;" | sqlite3 mysite/db.sqlite3
1|Bob's Cafe|1 High Street
```

Actual:

```
$ echo "SELECT * FROM places_place;" | sqlite3 mysite/db.sqlite3
1|Bob's Cafe|1 High Street
2|GPO|O'Connell Street
```
