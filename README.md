# adhoc-admin-api
API for adhoc admin ui

## Project structure and setup
1. Create virtual environment `python3 -m venv .venv`
2. Source .venv/bin/activate
3. Install packages `pip3 install -r requirements.txt`
4. Run `./start.sh`

If you have docker desktop installed locally, then run command `docker-compose up`. This command sets up database, application and pgadmin for the database.

Useful commands if you want to run locally:

```
To run makemigrations and apply migrations

docker-compose exec app alembic revision --autogenerate -m
docker-compose exec app alembic upgrade head

To prepopulate database with csv files

docker-compose exec app python prepopulate_db.py

```

