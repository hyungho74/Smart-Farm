import pymysql,time #pip install pymysql
conn = pymysql.Connect(host='10.82.17.194', user = 'rasp', password = 'password', db = 'database', charset = 'utf8') 
#host = 'db서버의 ip주소' user = '설정한 username' password = '설정한 password' db = 'db이름'
curr = conn.cursor()
sql = "insert into value1 value ('1', 'test', '성공')"
conn.commit()
curr.clost()
conn.close()
conn = None
curr = None