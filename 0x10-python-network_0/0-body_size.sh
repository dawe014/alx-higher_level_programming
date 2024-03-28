#!/bin/bash
# This script retrieves the byte size of the HTTP response header for a specified URL.
# It utilizes the curl command to fetch the content of the URL silently ("-s") and
# then pipes it to wc (word count) command with the "-c" option to count the bytes.
curl -s "$1" | wc -c
