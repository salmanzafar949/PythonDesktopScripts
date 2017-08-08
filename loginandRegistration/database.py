import sqlite3
import time


conn = sqlite3.connect('RegsSystem.db')
c = conn.cursor()

def create_table_regs():
    c.execute("CREATE TABLE IF NOT EXISTS regs(id INTEGER PRIMARY KEY, u_name TEXT , pwd TEXT ")

def insert_data(u_name, pwd):
    c.execute("insert into regs (u_name, pwd) values(?,?)",(u_name,pwd))
    conn.commit()

def validate_login(u_name, pwd):
    c.execute("select u_name, pwd from regs")
    data = c.fetchall()
    print(data)