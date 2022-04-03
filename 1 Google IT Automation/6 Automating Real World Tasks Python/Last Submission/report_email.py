#!/usr/bin/env python3

from datetime import datetime
import os
import reports
import emails

title = "Processed Updated on {}".format(datetime.today().strftime('%B %d, %Y'))
paragraph = ""
for file in os.listdir(os.path.join('supplier-data', 'descriptions')):
    with open(os.path.join('supplier-data', 'descriptions', file)) as fruit_file:
        paragraph += "<br/>"
        paragraph += "name: {}<br/>".format(fruit_file.readline().strip())
        paragraph += "weight: {}<br/>".format(fruit_file.readline().strip())

if __name__ == "__main__":
    reports.generate_report('/tmp/processed.pdf', title, paragraph)
    message = emails.generate("automation@example.com", "student-01-6f5429b355a5@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
    emails.send(message)
