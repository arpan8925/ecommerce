#!/bin/bash
# Install the necessary requirements
pip install -r requirements.txt

# Collect static files without asking for input
python3.9 manage.py collectstatic --no-input --clear
