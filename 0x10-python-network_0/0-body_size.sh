#!/bin/bash
# Bash script to send a request to a URL and display the size of the response body in bytes

# Check if an argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL using curl, then display the size of the response body in bytes
curl -sI "$1" | awk '/Content-Length/ {print $2}'
