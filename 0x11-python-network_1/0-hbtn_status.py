#!/usr/bin/python3
"""This script fetches a URL using"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: " + str(data.__class__))
        print("\t- content: " + str(data))
        print("\t- utf8 content: " + str(data.decode('utf-8')))
