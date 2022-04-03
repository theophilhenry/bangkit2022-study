#!/usr/bin/env python3
import sys
import subprocess

with open(sys.argv[1]) as file:
    for line in file.readlines():
        new_line = line.strip().replace('jane', 'jdoe')
        subprocess.run(["mv", line.strip(), new_line])
