"""
使用生产者消费者模式来异步下载【斗图啦网站】最新表情
"""
import requests
from lxml import etree
import os
import re
from urllib import request
from queue import Queue
import threading


class Producer(threading.Thread):
    """
    生产者
    """

    def __init__(self, page_url_queue, image_url_queue, *args, **kwargs):
        """
        构造器
        :param page_url_queue:
        :param image_url_queue:
        :param args:
        :param kwargs:
        """
        super(Producer, self).__init__(*args, **kwargs)
        self.page_url_queue = page_url_queue
        self.image_url_queue = image_url_queue

    def run(self):
        """
        重写父类的方法
        :return:
        """
        while True:
            if self.page_url_queue.empty():
                break
            page_url = self.page_url_queue.get()
            self.parse_page(page_url)

    def parse_page(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        text = response.text
        html = etree.HTML(text)
        images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for image in images:
            image_url = image.get('data-original')
            suffix = os.path.splitext(image_url)[-1]
            file_name = re.sub('[\?？,，\.!！\*]', '', image.get('alt')) + suffix
            self.image_url_queue.put((image_url, file_name))


class Consumer(threading.Thread):
    def __init__(self, page_url_queue, image_url_queue, *args, **kwargs):
        """
        构造器
        :param page_url_queue:
        :param image_url_queue:
        :param args:
        :param kwargs:
        """
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_url_queue = page_url_queue
        self.image_url_queue = image_url_queue

    def run(self):
        while True:
            if self.page_url_queue.empty() and self.image_url_queue.empty():
                break
            image_url, file_name = self.image_url_queue.get()
            request.urlretrieve(image_url, 'f:\\images\\' + file_name)
            print(file_name, '下载完成')


def main():
    # queue是线程安全的队列，可以在多线程环境中安全使用
    page_url_queue = Queue(50)
    image_url_queue = Queue(2000)
    base_url = 'http://www.doutula.com/photo/list/?page={}'
    for index in range(1, 51):
        url = base_url.format(index)
        page_url_queue.put(url)

    # 创建5个生产者
    for x in range(5):
        producer = Producer(page_url_queue=page_url_queue, image_url_queue=image_url_queue)
        producer.start()

    # 创建5个消费者
    for y in range(5):
        consumer = Consumer(page_url_queue=page_url_queue, image_url_queue=image_url_queue)
        consumer.start()


if __name__ == '__main__':
    main()
