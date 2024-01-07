#!/usr/bin/env python
import sys
import requests

def get_url_end_location(url = ''):
    r = requests.head(url=url, allow_redirects=True)
    return url

def main() -> int:
    return 0

if __name__ == '__main__':
    sys.exit(main())
