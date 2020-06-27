import re
import os
import urllib
from bs4 import BeautifulSoup

base_url = 'https://movie.douban.com/top250?start='
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
find_image_link = re.compile(r'https://.*jpg')
find_name = re.compile(r'alt=".*?"')

# req = urllib.request.Request(url=base_url, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode())

# b = 'http://www.llss.at/wp/category/all/anime/'
# req = urllib.request.Request(url=b, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode())



def get_html(url: str) -> str:
    request = urllib.request.Request(url, headers=headers)
    
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    
    html = response.read().decode()
    return html 


def save_image(base_url, save_dir='doubantop250'):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for i in range(0, 10):
        url = base_url + str(i + 25)
        html = get_html(url)
        
        parser = BeautifulSoup(html, 'html.parser')
        for item in parser.find_all('div', class_='item'):          
            item = str(item)
            return item
            name = re.findall(find_name, item)[0][5:-1]
            image_link = re.findall(find_image_link, item)[0]
            if name is not None and image_link is not None:
                name += '.jpg'
                save_path = os.path.join(save_dir, name)
                _, _ = urllib.request.urlretrieve(image_link, save_path)
            print(f'{name}已保存！')


if __name__ == '__main__':
    save_image(base_url)
