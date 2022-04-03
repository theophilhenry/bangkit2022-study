#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
    condition = "y"
    while(condition == "y"):
        error = input("What is the error?")
        if(isinstance(error, (int, str, list))):
            condition = "n"

    returned_error = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = []
            error_list = error.split(' ')
            for i in range(len(error_list)):
                error_patterns.append(r"{}".format(error_list[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_error.append(log)
        file.close()
    return returned_error


def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    # with open('../data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
    file.close()


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_error = error_search(log_file)
    file_output(returned_error)
    sys.exit(0)