#!/usr/bin/python3
"""Sends a request to the URL and
displays the body of the response"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            decoded_content = response.read().decode('utf-8')
            print(decoded_content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
