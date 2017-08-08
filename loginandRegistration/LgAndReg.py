import time
import sqlite3
import datetime
import database
import getpass

print("Login and Registration system")
print("for login press 1 for Registration press 2")
op = input('>> ')

def login():
    u_name = input('Enter your username: ')
    pwd    = input('Enter your password: ')

def reg():
    u_name = input('Enter your username: ')
    pwd    = input('Enter your password: ')
    if u_name == "" and pwd == "":
        print("Fields Cannot be empty")
        exit()

if op == '1':
    pass
elif op == '2':
    reg()
else:
    print("Inavlid entry")
    exit()


database.create_table_regs()