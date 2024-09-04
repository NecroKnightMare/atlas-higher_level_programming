#!/usr/bin/python3

import os
import sys

os.system('curl -Lso /tmp/hidden_4.pyc "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"')

py_compile.compile('/tmp/hidden_4.pyc')

if __name__ == "__main__":
    import hidden_4
    names = sorted(name for name in dir(hidden_4) if not name.startswith("__")]
    for name in names:
        print(name)
