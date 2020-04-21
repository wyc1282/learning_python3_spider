import requests
from bs4 import BeautifulSoup
from queue import Queue
def get_nr(chapter_name,chapter_urls):#接收URL列表
    nts = Queue() #先进先出的队列
    for chapter_url in chapter_urls:
        req = requests.get(url=chapter_url)
        req.encoding = 'utf-8'
        html = req.text
        bs = BeautifulSoup(html,"lxml")
        texts = bs.find('div',id='content')
        nr = texts.text.strip().split('\xa0'*4)

        with open(book_name + '.txt', 'a', encoding='utf-8') as f:
                f.write(chapter_name)
                f.write('\n')
                f.write('\n'.join(nr))
                f.write('\n')
        nts.put(nr)
    return nts #返回队列