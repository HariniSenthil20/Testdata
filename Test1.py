import os
import psycopg

# 1. Critical Hardcoded AWS Key
AWS_SECRET = "AKIA1234567890ABCDEF"

# 2. High Severity SQL Injection
def find_user_by_email(email):
    sql = f"SELECT * FROM accounts WHERE email = '{email}'"
    cursor.execute(sql)
    return cursor.fetchall()

# 3. High Severity Command Injection
def run_backup(folder_name):
    os.system("tar -czf backup.tar.gz " + folder_name)

# 4. Medium Severity Resource Leak
def read_config():
    f = open("/etc/config.json", "r")
    return f.read()
