#!/bin/bash
# This script displays all the HTTP methods that the server of a specified URL will accept.
# It uses the curl command with the option "-sI" to fetch the HTTP headers of the URL silently, then pipes the output to grep to find the line containing "Allow",
# and finally, it utilizes cut command to extract and display the HTTP methods from the line by specifying the delimiter "-d " " and the fields "-f 2-".
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
