import pymysql
from database import MyDB

# MyDB 클래스 생성
mydb = MyDB(
    _host = 'ojds01.mysql.pythonanywhere-services.com',
    _port = 3306,
    _user = 'ojds01',
    _pw = 'toqha131',
    _db_name = 'ojds01$default'
)

# table 생성 쿼리문
create_user = '''
    create table
    if not exists
    user (
    id varchar(32) primary key,
    password varchar(64) not null,
    name varchar(32)
    )
'''
# sql 쿼리문 실행
mydb.sql_query(create_user)
# db 서버에 동기화하고 연결 종료
mydb.commit_db()