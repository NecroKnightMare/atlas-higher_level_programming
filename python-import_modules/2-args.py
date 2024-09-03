#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv
    num_args = len(argv) - 1

    if num_args == 0:
        print("Number of argument(s): 0.")
    else:
        print("{}: argument{}".format(num_args, "" if num_args == 1 else "s"))
        for i in range (1, len(argv)):
            print("{}: {}".format(i, argv[i]))
