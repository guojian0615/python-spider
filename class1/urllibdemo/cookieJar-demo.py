"""
使用cookieJar自动登录获取cookie
然后请求需要登录的接口
"""
from urllib import request
from http.cookiejar import CookieJar
import json


def get_opener():
    # 创建CookieJar对象
    cookie_jar = CookieJar()
    cookie_processor = request.HTTPCookieProcessor(cookie_jar)
    opener = request.build_opener(cookie_processor)
    return opener


my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/61.0.3141.7 Safari/537.36'
}


def login(opener):
    login_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3141.7 Safari/537.36',
        'Content-Type': 'application/json'
    }
    login_rul = 'http://172.31.205.27:9090/api/v1/authc/login'
    login_data = {
        'account': 'jianguo2',
        'password': 'Gj20180214'
    }
    print(json.dumps(login_data).encode('utf-8'))
    req = request.Request(login_rul, headers=login_header, data=json.dumps(login_data).encode(
        'utf-8'))
    opener.open(req)


def get_project_list(opener):
    project_url = 'http://172.31.205.27:9090/api/v1/project/listProject'
    req = request.Request(project_url, headers=my_headers)
    resp = opener.open(req)
    project_list = resp.read().decode('utf-8')
    print('项目列表:', project_list)


opener = get_opener()
login(opener)
get_project_list(opener)
