#!/bin/bash
# This script sends a DELETE request to the specified URL and displays the response body.
# It uses the curl command with the option "-sX DELETE" to send a DELETE request silently ("-s") to the provided URL.
curl -sX DELETE "$1"
