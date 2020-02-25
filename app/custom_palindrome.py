import argparse
import re

IGNORE_NON_ALPHA_CHARACTER = re.compile(r"\W+|_")


def isPalindrome(word):
    """
       Check the give word is palindrome.

       Args:
          :param word(str): string input
       Returns:
          bool: True|False
    """

    input_str = IGNORE_NON_ALPHA_CHARACTER.sub("", str(word)).casefold()
    return input_str == input_str[::-1]


def make_cli_parser():
    cli_parser = argparse.ArgumentParser(add_help=True)
    cli_parser.add_argument(
        '--words',
        nargs="+",
        help="string to verify..")
    return cli_parser


def main(argv=None):
    cli_parser = make_cli_parser()
    args = cli_parser.parse_args(argv)
    try:
       for word in args.words:
           print("{} is a Palindrome? {}".format(word, isPalindrome(word)))
    except:
       cli_parser.print_help()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        raise error
