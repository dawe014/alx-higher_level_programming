#!/bin/bash
# This script displays all the HTTP methods that the server of a specified URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
