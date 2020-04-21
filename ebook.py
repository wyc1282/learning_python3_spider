import requests
from bs4 import BeautifulSoup
from queue import Queue
from tqdm import tqdm

class EBook():

    def __init__(self,server_url='https://www.xsbiquge.com',book_name="诡秘之主",directory_url='https://www.xsbiquge.com/15_15338/'):
        """
        :param server_url: 服务器地址
        :param directory_url: 目录地址
        :param book_name: 书名
        """
        self.server_url = server_url
        self.directory_url = directory_url
        self.book_name = book_name


    def get_chapters(self):
        """
        :return: chapter_names 章节名
                 chapter_urls 章节url
        """
        # 获取目录页的内容
        req = requests.get(url=self.directory_url)
        # 解码
        req.encoding = 'utf-8'
        # 讲解码出的文本传入变量
        html = req.text
        bs = BeautifulSoup(html, 'lxml')
        chapters = bs.find('div', id='list')
        chapters =chapters.find_all('a')
        c_n = Queue()
        c_u = Queue()
        for chapter in chapters:
            c_n.put(chapter.string)
            c_u.put(self.server_url + chapter.get('href'))
        chapter_names,chapter_urls = c_n,c_u
        return chapter_names,chapter_urls
    #     return chapters
    #
    # def get_chapter_name(self):  # 获取章节名
    #     c_n = Queue()
    #     for chapter in tqdm(self.get_chapters()):
    #         c_n.put(chapter.string)
    #     chapter_names = c_n
    #     return chapter_names
    #
    # def get_chapter_url(self): # 获取章节url
    #         c_u = Queue()
    #         for chapter in self.get_chapters():
    #             c_u.put(self.server_url + chapter.get('href'))
    #         chapter_urls = c_u
    #         return chapter_urls


    def get_nr(self,chapter_urls):  # 接收URL列表
        """
        :return: 按章节排列的队列
        """
        n = Queue()  # 先进先出的队列
        chapter_names,chapter_urls =self.get_chapters()
        while not chapter_urls.empty():
            req = requests.get(url=chapter_urls.get())
            req.encoding = 'utf-8'
            html = req.text
            bs = BeautifulSoup(html, "lxml")
            texts = bs.find('div', id='content')
            nr = texts.text.strip().split('\xa0' * 4)
            n.put(nr)
        nrs = n
        return nrs  #返回队列



    def output(self):
        # nrs = self.get_nr()
        chapter_names, chapter_urls = self.get_chapters()
        with open(self.book_name+'.txt', 'a', encoding='utf-8') as f:
            while not chapter_urls.empty() and not chapter_names.empty():
                f.write(chapter_names.get())
                f.write('\n')
                f.write(chapter_urls.get())
                f.write('\n')

