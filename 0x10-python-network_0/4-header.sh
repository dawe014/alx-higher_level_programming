#!/bin/bash
# This script sends a GET request to the specified URL with a custom header variable.
curl -X GET -H "X-School-User-Id: 98" "${1}"
