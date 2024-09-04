#!/usr/bin/python3

import os
import sys

if __name__ == "__main__":
    import hidden_4
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
