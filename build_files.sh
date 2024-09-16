#!/bin/bash

# Ensure Python3 is installed and virtual environment is created
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
python3 -m pip install --upgrade pip

# Install the necessary requirements
pip install -r requirements.txt

# Collect static files without input
python3 manage.py collectstatic --no-input --clear
