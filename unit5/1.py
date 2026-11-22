import mysql.connector as db

try:
    with open('data.docx') as file:    
        print(file.read())
except FileNotFoundError as e:
    print('Error: ', e)
except Exception as e:
    print('Error: ', e)

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
finally:
    conn.close()