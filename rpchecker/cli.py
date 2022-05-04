import argparse


def read_user_args():
    """Handle user supplied CLI args passed at cli invocation."""
    parser = argparse.ArgumentParser(
        prog="rpchecker",
        description="check connectivity of a website or list of sites"
        )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n\tError: "{error}"')
