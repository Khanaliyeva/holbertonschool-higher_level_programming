#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

import urllib.request

url = 'https://intranet.hbtn.io/status'
request = urllib.request.Request(url, headers={'User-Agent': 'HolbertonStudent'})

with urllib.request.urlopen(request) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
