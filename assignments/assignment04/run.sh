#!/usr/bin/bash

python3 -m venv env

source ./env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python3 ner/main.py -b16

deactivate