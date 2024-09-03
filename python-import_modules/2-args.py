#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s): 0.")
    else:
        print("{} argument:{}".format(num_args, "" if num_args == 1 else "s"))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, argv[i]))
