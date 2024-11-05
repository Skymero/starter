#!/bin/bash

argparse() {
  local args=("$@")
  local powershell=0
  local bash=0

  echo "Arguments: $@"

  while [[ $# -gt 0 ]]; do

    echo "Powershell: $powershell, Bash: $bash"


    if [ -d "venv/bin" ] && [ -f "venv/bin/activate" ]; then
        echo "Activating existing virtual environment in Bash..."
        source ./venv/bin/activate
    else
        echo "Creating and activating new virtual environment in Bash..."
        python3.10 -m venv venv
        source ./venv/bin/activate
        python -m pip install -r requirements.txt
    fi


    exit 1
  fi
}

argparse "$@"


