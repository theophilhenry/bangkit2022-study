#!/usr/bin/env python3

import shutil
import psutil
import smtplib
import email.message
import socket

def send_email(subject):
    # Prepare and Send the email
    message = email.message.EmailMessage()
    message["From"] = "automation@example.com"
    message["To"] =  "student-01-6f5429b355a5@example.com"
    message["Subject"] = subject
    message.set_content("Please check your system and resolve the issue as soon as possible.")
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

def check_disk_usage():
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    return free < 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_memory_usage():
    usage = psutil.virtual_memory().used >> 20
    return usage > 500

def check_localhost():
    return socket.gethostbyname('localhost')

if check_disk_usage():
    send_email("Error - Available disk space is less than 20%")
if check_cpu_usage():
    send_email("Error - CPU usage is over 80%")
if check_memory_usage():
    send_email("Error - Available memory is less than 500MB")
if check_localhost() != '127.0.0.1':
    send_email("Error - localhost cannot be resolved to 127.0.0.1")


