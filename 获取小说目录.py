import requests
from bs4 import BeautifulSoup
from queue import Queue
from 获取文章内容 import get_nr
from tqdm import tqdm

def get_chapters(target = 'https://www.xsbiquge.com/15_15338/'):
    # server ='https://www.xsbiquge.com' #网络主页
    # book_name = "诡秘之主" #小说名
    # target = 'https://www.xsbiquge.com/15_15338/' #小说目录页
    #获取目录页的内容
    req = requests.get(url=target)
    #解码
    req.encoding = 'utf-8'
    #讲解码出的文本传入变量
    html = req.text

    bs = BeautifulSoup(html,'lxml')
    chapters = bs.find('div',id='list')
    chapters = chapters.find_all('a')
    return chapters



def get_chapter_name(chapters): #获取章节名
    chapter_names = Queue()
    for chapter in tqdm(chapters):
        chapter_names.put(chapter.string)
    return chapter_names

def get_chapter_url(chapters): #获取章节url
    chapter_urls = Queue()
    for chapter in tqdm(chapters):
        chapter_urls.put('https://www.xsbiquge.com'+chapter.get('href'))
    return chapter_urls


    # for chapter in tqdm(chapters):
    #     chapter_name=chapter.string
    #     url = server+chapter.get('href')
    #     nr = get_nr(url)
    #     with open(book_name+'.txt','a',encoding='utf-8') as f:
    #         f.write(chapter_name)
    #         f.write('\n')
    #         f.write('\n'.join(nr))
    #         f.write('\n')


if __name__ == '__main__':
    get_chapters()
