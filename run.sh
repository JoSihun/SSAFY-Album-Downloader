#!/bin/bash

# Check if the virtual environment directory exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install the requirements
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
fi

# Run the run.py script
if [ -f "run.py" ]; then
    echo "Running run.py..."
    python run.py
else
    echo "run.py not found."
fi

# Deactivate the virtual environment
deactivate
