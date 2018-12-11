"""
使用cookie模拟登录
"""
from urllib import request

project_url = 'http://172.31.205.27:9090/api/v1/project/listProject'
my_heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
    'Cookie': 'JSESSIONID=EF4B1DFABCEC442B03B22A5655EEE51A; pass_login_token=9'
}
req = request.Request(project_url, headers=my_heads)
resp = request.urlopen(req)

print(resp.read().decode('utf-8'))

# with open('data/aipaasLogin.html', 'w') as file_obj:
#     file_obj.write(resp.read().decode('utf-8'))
