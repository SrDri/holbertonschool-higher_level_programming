#!/usr/bin/python3
""" fetch the https://intranet.hbtn.io/status """
import urllib.request as requ

if __name__ == "__main__":
    with requ.urlopen("https://intranet.hbtn.io/status") as res:
        body = res.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode(encoding="utf-8")))
