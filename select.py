import pymysql
conn = pymysql.Connect(host='10.82.17.194', user = 'rasp', password = 'password', db = 'database', charset = 'utf8') 
#host = 'db서버의 ip주소' user = '설정한 username' password = '설정한 password' db = 'db이름'
with conn.cursor() as curr:
    sql = "SELECT * frmo item"
    curr.execute(sql)
    rs = curr.fetchall()
    for data in rs:
        print(data)