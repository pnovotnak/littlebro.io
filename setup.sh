#!/bin/bash

PROJECT="littlebro"
_PATH="$PROJECT/$PROJECT"

# setup virtual env
echo "Setting up virtual environment (env)"
virtualenv --no-site-packages env
echo "Activating virtual environment"
source env/bin/activate

# install dependencies
pip install --download-cache ~/.pip-cache --allow-external PIL --upgrade --use-mirrors -r requirements.txt

