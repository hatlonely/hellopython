#!/usr/bin/env python3


import argparse


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""Example:
    python3 argparse_test.py 123 choice1 -o 127.0.0.1 -p 4000
""")
    parser.add_argument("arg1", nargs="?", type=int, help="arg1")
    parser.add_argument("arg2", nargs="?", choices=[
                        "choice1", "choice2"], help="arg2")
    parser.add_argument("-o", "--host", default="127.0.0.1", help="host")
    parser.add_argument("-p", "--port", default=8000, help="port")
    args = parser.parse_args()
    print(args.arg1, args.arg2, args.host, args.port)


if __name__ == "__main__":
    main()
