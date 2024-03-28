#!/bin/bash
# This script retrieves the response body from a specified URL, specifically targeting responses with a status code of 200.
# It uses the curl command with the options "-sL" to fetch the content of the URL silently and follow redirects if any.
curl -sL "$1"
