#!/bin/bash

# Wait for the PostgreSQL database to be available
chmod +x app/scripts/wait-for-it.sh
app/scripts/wait-for-it.sh db:5432 --timeout=60 --strict -- echo "PostgreSQL is up and running"

# Run db migration
alembic upgrade head

# Run prepopulate data for db
python prepopulate_db.py

export ENV=dev
# Run the app
python run.py