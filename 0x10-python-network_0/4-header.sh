#!/bin/bash
# This script sends a GET request to the specified URL with a custom header variable.
# It utilizes the curl command with the option "-sH" to include a custom header "-H" with the value 
curl -sH "X-School-User-Id: 98" "${1}"
