#!/usr/bin/python3
""" Take a url and email and send a post request """
import urllib.request as req
import urllib.parse as parse
import sys


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    email = parse.urlencode(email)
    email = email.encode()

    body = req.Request(sys.argv[1], email)
    with req.urlopen(body) as res:
        print(res.read().decode("utf-8"))
