from urllib.request import urlopen, urlretrieve  # url
from bs4 import BeautifulSoup as bf  # 解析html
import requests
import re


def get_vmgirls():
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


def get_bi_lives():
    req_data = {'platform': 'web', 'parent_area_id': 1, 'area_id': 0, 'sort_type': 'sort_type_224', 'page': 1}
    for i in range(1, 10):
        req_data['page'] = i
        res = requests.get('https://api.live.bilibili.com/xlive/web-interface/v1/second/getList', params=req_data)
        json_res = res.json()
        blog_list = json_res['data']['list']
        for x in blog_list:
            cover_suffix = x['cover'].split('.').pop()
            face_suffix = x['face'].split('.').pop()
            urlretrieve(x['cover'], 'download/{}-封面图{}'.format(x['title'], cover_suffix))
            urlretrieve(x['face'], 'download/{}-头像{}'.format(x['title'], face_suffix))
            print(x['cover'], i)


# requests.post(url='https://www.vmgirls.com/wp-admin/admin-ajax.php')
get_bi_lives()
