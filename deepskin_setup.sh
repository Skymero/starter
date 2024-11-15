#!/bin/bash
# Install dependencies from requirements.txt
pip install -r 'C:/tmp/cloned_repo/WoundSize/WoundSize/Deepskin/requirements.txt'
pip install -r 'C:/tmp/cloned_repo/WoundSize/WoundSize/Deepskin/docs/requirements.txt'
# python3.10 -m pip install .
cd C:/tmp/cloned_repo/WoundSize/WoundSize/Deepskin
# Install Deepskin package
# python3.10 ./Deepskin/setup.py
python -m pip install --editable .
cd ~