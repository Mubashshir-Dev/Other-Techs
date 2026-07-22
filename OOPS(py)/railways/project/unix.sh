#!/bin/bash

if ! command -v python3 >/dev/null 2>&1; then
    if command -v pacman >/dev/null 2>&1; then
        sudo pacman -Sy --needed python python-pip
    elif command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install -y python3 python3-pip python3-venv
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y python3 python3-pip
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y python3 python3-pip
    elif command -v zypper >/dev/null 2>&1; then
        sudo zypper install -y python3 python3-pip
    elif command -v brew >/dev/null 2>&1; then
        brew install python
    else
        exit 1
    fi
fi

if [ ! -d "myvenv" ]; then
    python3 -m venv myvenv
fi

source myvenv/bin/activate

python -m pip install --upgrade pip

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

python main.py

deactivate