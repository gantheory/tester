""" parser configuration """

import argparse
from argparse import RawTextHelpFormatter

__all__ = ["config_setup"]

def config_setup():
    """ parser configuration """

    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument('-site', type=int, default=0, help='Codeforces: 0, AtCoder: 1')
    parser.add_argument(
        '-contest_id', type=str, default='',
        help='Codforces: contest_id (ex: 001)\n'
             'AtCoder: [abc|arc|agc]contest_id (ex: abc001)\n'
    )
    config = parser.parse_args()
    return config
