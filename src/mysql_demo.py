from pymysql import cursors, connect


conn = connect(host = '127.0.0.1', user='root',password='123456',
               db='guest', charset='utf8mb4',
               cursorclass=cursors.DictCursor)


try:
    with conn.cursor() as cursor:
        sql = r"select * from sign_guest"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()