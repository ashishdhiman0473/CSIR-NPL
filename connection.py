import psycopg2

hostname = 'localhost'
database = 'mapping_db'
username = 'postgres'
pwd = '1234567' 
port_id = 5432
cur = none
conn = none

try:
conn = psycopg2.connect(
    host = hostname,
    dbname = databse,
    user = username,
    password = pwd,
    port = port_id)

cur = conn.cursor()



except Exception as error:
    print(error)
    
finally:
    if cur is not none:
        cur.close()
    if conn is not none:
        conn.close()
    
