import mysql.connector as db

try:
    conn = db.connect(
        host='localhost',
        user='root',
        password='',
        database='lms',
    )
    if conn.is_connected():
        print('Connected')
except ConnectionError as conn_err:
    print('Error: ', conn_err)
except Exception as e:
    print('Error: ', e)
else:
    print('No Error Occured.. Perform DB operations here.')
finally:
    conn.close()
