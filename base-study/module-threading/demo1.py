"""
多线程的学习，
threading和time模块都是python自带的模块，无需安装
"""
import time
import threading


def coding():
    for x in range(3):
        print('正在写代码%s' % x)
        time.sleep(1)


def drawing():
    for x in range(3):
        print('正在画画 %s' % x)
        time.sleep(1)


def main():
    thread1 = threading.Thread(target=coding)
    thread2 = threading.Thread(target=drawing)
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
