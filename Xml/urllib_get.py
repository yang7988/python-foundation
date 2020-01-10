# Get
# urllib 的 request 模块可以非常方便地抓取 URL 内容，也就是发送一个
# GET 请求到指定的页面，然后返回 HTTP 的响应：
# 例如，对豆瓣的一个 URLhttps://api.douban.com/v2/book/2129650 进行
# 抓取，并返回响应：
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
