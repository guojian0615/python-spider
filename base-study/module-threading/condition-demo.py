"""
使用condition锁来实现生产者和消费者模式
condtion相比lock锁机制可以实现线程间的通信
"""
import threading
import time

# 商品的数量
GOODS = 0
# 全局锁
condition = threading.Condition()


class Producer(threading.Thread):
    """
    生产者，当仓库容量等于50时，处于等待状态
    """

    def run(self):
        global GOODS
        while True:
            time.sleep(3)

            condition.acquire()
            # 需要特别注意的地方，为什么要使用while而不是if，原因在于
            # wait操作后的线程获得锁后为继续执行后面的代码，而不是从头执行
            while GOODS >= 10:
                condition.notify_all()
                # wait()操作会释放锁，进行等待状态；
                # 直到被其他线程唤醒，获得锁后，继续执行下面的代码
                condition.wait()

            GOODS += 1
            print('生产者[%s]生产了1个商品，商品总数：%s' % (threading.current_thread(), GOODS))
            condition.release()


class Consumer(threading.Thread):
    """
    当仓库容量为0时，处于等待状态
    """

    def run(self):
        global GOODS
        while True:
            condition.acquire()
            while GOODS <= 0:
                condition.notify_all()
                condition.wait()

            time.sleep(1)
            GOODS -= 1
            print('消费者[%s]消费了一个商品,剩余商品：%s' % (threading.current_thread(), GOODS))
            condition.release()


def main():
    # 2个生产者
    for x in range(2):
        producer = Producer(name=f'producer{x}')
        producer.start()
    # 3个消费者
    print("hello world")
    for y in range(2):
        consumer = Consumer(name=f'consumer{y}')
        consumer.start()


if __name__ == '__main__':
    main()
