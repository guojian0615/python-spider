"""
多线程下共享数据问题
"""
import threading

VALUE = 0
# 定义一个全局锁
gLock = threading.Lock()


class Compute(threading.Thread):
    def run(self):
        global VALUE
        for x in range(1000000):
            # 上锁
            gLock.acquire()
            VALUE += 1
            # 释放锁
            gLock.release()
        print(f'value={VALUE}')


def main():
    for x in range(2):
        compute = Compute()
        compute.start()


if __name__ == '__main__':
    main()
