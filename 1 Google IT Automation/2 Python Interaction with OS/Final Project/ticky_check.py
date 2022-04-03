#!/usr/bin/env python3

import sys
import re
import operator
import csv


def generate_report(filename):
    error_dict = {}
    per_user_dict = {}

    with open(filename) as file:
        for line in file:
            result = re.search(
                r'(ERROR|INFO) ([\w \']*) ?(\[.*\])? ?\(([\w.-_]+)\)', line)
            result = result.groups()
            # ('INFO', 'Created ticket ', '[#4217]', 'mdouglas')
            # ('INFO', 'Created ticket ', 'mdouglas')

            # Add to ERROR dict
            if result[0] == "ERROR":
                error_dict[result[1]] = error_dict.get(result[1], 0) + 1
                # {'error something' : 4, 'error else' : 2}

            # ADD INFO/ERROR to User Usage
            if len(result) <= 3:
                username = result[2]
            else:
                username = result[3]
            if username not in per_user_dict:  # If the username is there
                per_user_dict[username] = {'Username': username}
                per_user_dict[username]["INFO"] = 0
                per_user_dict[username]["ERROR"] = 0
            per_user_dict[username][result[0]] += 1

    sorted_error = dict(sorted(error_dict.items(), key=operator.itemgetter(
        1), reverse=True))  # Sort based on value
    # {'theo': {'Username': 'theo', 'INFO': 2, 'ERROR}: 3}}
    sorted_user = dict(sorted(per_user_dict.items()))

    sorted_error["column_names"] = ("Error", "Count")
    sorted_user["column_names"] = ("Username", "INFO", "ERROR")

    return (sorted_error, sorted_user)


error_dict, user_dict = generate_report(sys.argv[1])

with open("error_message.csv", "w") as error_message:
    writer = csv.DictWriter(
        error_message, fieldnames=error_dict["column_names"])
    writer.writeheader()
    for error_key, error_value in error_dict.items():
        if(error_key == "column_names"):
            continue
        writer.writerow({'Error': error_key, 'Count': error_value})

with open("user_statistics.csv", "w") as user_statistics:
    writer = csv.DictWriter(
        user_statistics, fieldnames=user_dict["column_names"])
    writer.writeheader()
    for user_key, user_value in user_dict.items():
        if(user_key == "column_names"):
            continue
        writer.writerow(user_value)
