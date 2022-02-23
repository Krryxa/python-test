from urllib.request import urlopen, urlretrieve  # url
from bs4 import BeautifulSoup as bf  # 解析html
import requests
import re

html = urlopen('https://www.vmgirls.com')
obj = bf(html.read(), 'html.parser')
print(obj.head.title)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}
pic_info = obj.find_all('a', style=re.compile(r'background-image'))
print(pic_info)
for img in pic_info:
    # file_name = img['src'].split('/')[-1]
    temp = img['style'].split('//').pop()
    url = 'https://' + temp[0:-2]
    file_name = url.split('/').pop()
    image = requests.get(url, headers=headers).content  # 因为策略原因，要加上header才能抓取
    # urlretrieve(url, 'download/{}'.format(file_name))
    with open('download/' + file_name, 'wb') as f:
        f.write(image)
        print('downloading-->' + file_name)
    print(url)

# res = requests.get('https://ainyi.com/krryblog/blog/getAllBlog?type=NO')
# json_res = res.json()
# blog_list = json_res['result']['data']
# for i in blog_list:
#     print(i['title'])


# requests.post(url='https://www.vmgirls.com/wp-admin/admin-ajax.php')
