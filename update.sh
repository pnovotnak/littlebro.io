#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

# Activate Python env
source env/bin/activate

# Fetch update
git checkout origin/master
git pull origin master

# Run migrations
python ./littlebro/manage.py migrate --noinput
python ./littlebro/manage.py collectstatic --noinput
