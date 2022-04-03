import csv
import sys


def populate_dictionary(filename):
    dict = {}
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dict[row['Full Name']] = row[' Email Address']
        file.close()
    return dict

def find_email(argv):
    dict = populate_dictionary('../data/user_emails.csv')
    return dict[argv[1]].strip()