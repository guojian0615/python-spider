"""
queue安全队列模块的学习
"""
from queue import Queue

name_queue = Queue(4)
print(name_queue.full())
name_queue.put('tom')
print(name_queue.qsize())
