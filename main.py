"""
Use this in the same way as Python's SimpleHTTPServer:

  python -m RangeHTTPServer [port]

The only difference from SimpleHTTPServer is that RangeHTTPServer supports
'Range:' headers to load portions of files. This is helpful for doing local web
development with genomic data files, which tend to be to large to load into the
browser all at once.
"""

from server import *
import argparse
from http.server import test

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "port",
        action="store",
        default=8000,
        type=int,
        nargs="?",
        help="Specify alternate port [default: 8000]",
    )
    parser.add_argument(
        "-b",
        "--bind",
        metavar="ADDRESS",
        help="bind to this address (default: all interfaces)",
    )
    parser.add_argument(
        "--cors",
        action="store_true",
        help="Enable CORS (Access-Control-Allow-Origin: *)",
    )

    args = parser.parse_args()

    test(HandlerClass=RangeRequestHandler, port=args.port, bind=args.bind)
