#!/bin/bash
# This script retrieves the byte size of the HTTP response header for a specified URL.
# It uses the curl command to fetch the content of the URL silently ("-s") and
# then pipes it to the wc (word count) command with the "-c" option to count the bytes.

# Check if an argument (URL) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Fetch the content of the URL using curl, then count the bytes
curl -s "$1" | wc -c
