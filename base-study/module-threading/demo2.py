"""
创建线程的第二种方法，继承threading.Thread类的形式
"""
import threading
import time


class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s' % threading.current_thread())
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画画 %s' % threading.current_thread())
            time.sleep(1)


def main():
    code = CodingThread()
    draw = DrawingThread()
    code.start()
    draw.start()


if __name__ == '__main__':
    main()
