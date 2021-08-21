#!/usr/bin/python3
""" Github API """
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/"
    endpoint = "user"
    auth = (argv[1], argv[2])

    res = requests.get(url + endpoint, auth=auth)
    res = res.json()

    if "id" in res:
        print(res["id"])
    else:
        print("None")
