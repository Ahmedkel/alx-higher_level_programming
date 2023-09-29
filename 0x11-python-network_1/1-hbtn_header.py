#!/usr/bin/python3
import urllib.request
import sys


def fetch_header(url):
    """
    Fetches a URL and displays the value of the
    X-Request-Id variable in the response header.
    """
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header(url)
