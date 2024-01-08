#!/usr/bin/env python
import sys
import requests
import argparse
import urllib.parse


def get_url_end_location(url=''):
    return requests.head(url=url, allow_redirects=True).url


def sanitise_url(url) -> str:
    trim_after = [';', '`', '*', '!']
    trimmed_url = url
    for i, char in enumerate(url):
        if char in trim_after:
            trimmed_url = trimmed_url[:i]
            break
    return urllib.parse.quote(trimmed_url, safe='/:?&')


def is_valid_url(url) -> bool:
    try:
        parsed = urllib.parse.urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False


def __get_args():
    parser = argparse.ArgumentParser(
        prog="Where Does This Go?",
        description="Find out where a given url redirects to",
    )

    parser.add_argument(
        'url',
        help='The URL to follow',
    )
    return parser.parse_args()


def main() -> int:
    return 0


if __name__ == '__main__':
    args = __get_args()
    result = get_url_end_location(args.url)
    print(result)
    sys.exit(main())
