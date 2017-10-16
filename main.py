""" tester main function """

import os
from colorama import Fore
from lib.config import config_setup
from lib.parser import parse_codeforces, parse_atcoder

if __name__ == "__main__":
    CONFIG = config_setup()
    print(Fore.RED + "\n    Parser by gantheory" + Fore.WHITE)

    try:
        os.makedirs('testcases')
    except os.error:
        pass

    if CONFIG.site == 0:
        parse_codeforces(CONFIG)
    elif CONFIG.site == 1:
        parse_atcoder(CONFIG)
    else:
        raise ValueError("Invalid Contest Site")
