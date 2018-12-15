"""
queue安全队列模块的学习
"""
from queue import Queue


# name_queue = Queue(4)
# print(name_queue.full())
# print(name_queue.empty())
# name_queue.put('tom')
# print(name_queue.qsize())

def test(*args, **kwargs):
    print('*args:', args)
    print('**kwargs:', **kwargs)


test(name='rose', age=10)
