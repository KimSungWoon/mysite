from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models


def insert(name, email, password, gender):
    conn = getconnection()
    cursor = conn.cursor()

    sql = '''
        insert
          into user
        values (null, %s, %s, password(%s), %s, now())
    '''
    cursor.execute(sql, (name, email, password, gender))
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def fetchone(email, password):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select no, name
          from user
         where email=%s
           and password=password(%s)    
    '''
    cursor.execute(sql, (email, password))
    result = cursor.fetchone()

    # 자원 정리
    cursor.close()
    conn.close()

    return result


def fetchonebyno(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select no, name, email, gender
          from user
         where no=%s    
    '''
    cursor.execute(sql, (no,))
    result = cursor.fetchone()

    # 자원 정리
    cursor.close()
    conn.close()

    return result


def update(no, name, password, gender):
    conn = getconnection()
    cursor = conn.cursor()

    if password == '':
        sql = '''
            update user
               set name=%s, gender=%s
             where no=%s 
        '''
        t = (name, gender, no)
    else:
        sql = '''
            update user
               set name=%s, password=password(%s), gender=%s
             where no=%s 
        '''
        t = (name, password, gender, no)

    cursor.execute(sql, t)
    conn.commit()

    # 자원 정리
    cursor.close()
    conn.close()


def getconnection():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.112',
        port=3307,
        db='mysite',
        charset='utf8')

# Create your models here.

