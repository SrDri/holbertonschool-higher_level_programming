#!/usr/bin/python3
""" Display the value of a header """
import urllib.request as requ
import sys


if __name__ == "__main__":
    argv = sys.argv

    with requ.urlopen("{}".format(argv[1])) as html:
        print("{}".format(html.getheader("X-Request-Id")))
