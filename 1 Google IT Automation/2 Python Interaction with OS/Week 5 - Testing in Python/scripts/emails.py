#!/usr/bin/env python3
import sys
import csv

def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  try:
    # Create the username based on the command line input.
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    # email_dict = populate_dictionary('/home/student-01-877a31283206/data/user_emails.csv')
    email_dict = populate_dictionary('../data/user_emails.csv')
    # Find and print the email
    return email_dict.get(fullname.lower(), "No email address found")
  except IndexError:
      return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()
