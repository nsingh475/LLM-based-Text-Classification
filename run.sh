#!/bin/bash

# Print a message indicating the script has started
echo "Entered run.sh script"

# Install required dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
else
    echo "There was an error installing the dependencies."
    exit 1
fi

# Start the FastAPI server using Uvicorn
echo "Starting FastAPI server with Uvicorn..."
uvicorn app.main:app --reload