#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

  - Displays the body of the response.
"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)
