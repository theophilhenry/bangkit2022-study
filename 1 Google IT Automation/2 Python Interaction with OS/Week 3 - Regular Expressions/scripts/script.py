import csv
import re
from tkinter import E


def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@' + domain + '$'
  if re.match(domain_pattern, address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '../data/user_emails.csv'
  report_file = '../data' + '/updated_user_emails.csv'

  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location) as csv_file:
    user_data_list = list(csv.reader(csv_file))
    user_email_list = [d[1].strip() for d in user_data_list[1:]]

    # Looping the email, if needs to be replaced, replace
    # If replaced, add the old and new to the corespondend list
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(
          email_address, old_domain, new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    # If old is equal the current user, then it needs to be replaced.
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
    csv_file.close()

    print(user_data_list)

    with open(report_file, 'w+') as report:
      writer = csv.writer(report)
      writer.writerows(user_data_list)
      report.close()

main()