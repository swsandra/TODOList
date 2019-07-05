#!/bin/bash

## Postgres configuration

# Verify if Postgres is installed
if ! type "psql" > /dev/null; then
    echo "Postgres not installed."
    printf "To install: sudo apt-get install postgresql\n"
    echo "Then run this script again"
fi

# Drop old database and user
sudo -u postgres dropdb todolist_db >> /dev/null
sudo -u postgres dropuser todouser >> /dev/null

# Create database and user
sudo -u postgres psql << EOF
create database todolist_db;
create user todouser with password 'todouser';
alter role todouser set client_encoding to 'utf-8';
alter role todouser set default_transaction_isolation TO 'read committed';
alter role todouser set timezone to 'UTC';
alter role todouser createdb;
grant all privileges on database todolist_db to todouser;
\q
EOF

# Remove old migrations
rm -r ToDoListMiniApp/migrations >> /dev/null