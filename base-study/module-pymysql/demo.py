"""
使用pymysql驱动来操作mysql
pip install pymysql
"""
import pymysql

conn = pymysql.Connect(
    host='192.168.59.135',
    user='root',
    password='123456',
    database='pymysql_demo',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
cursor.execute('select * from user')


def get_one_data():
    """
    获取单条数
    :return:
    """
    result = cursor.fetchone()
    print(result)
    conn.close()


def get_all_data():
    """
    获取满足条件的所有的数据
    :return:
    """
    results = cursor.fetchall()
    for result in results:
        print(type(result))
        print(result)
        print("=" * 40)
    conn.close()


def get_limit_data():
    """
    获取指定条数的数据
    :return:
    """
    results = cursor.fetchmany(2)
    for result in results:
        print(result)
    conn.close()


def insert_one_data():
    sql = """
        insert into user(name,age) VALUE (%s,%s)
    """
    cursor.execute(sql, ('王明', 14))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    insert_one_data()
