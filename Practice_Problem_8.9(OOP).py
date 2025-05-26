'''

Reimplement method dequeue() of class Queue so that a KeyboardInterrupt excep
tion (an inappropriate exception type in this case) with message 'dequeue from empty
 queue'(an appropriate error message, actually) is raised if an attempt to dequeue an empty
 queue is made:

 >> queue = Queue()
 >> queue.dequeue()

 Traceback (most recent call last):
 File "<pyshell#30>", line 1, in <module>
 queue.dequeue()
 File "/Users/me/ch8.py", line 183, in dequeue
 raise KeyboardInterrupt('dequeue from empty queue')
 KeyboardInterrupt: dequeue from empty queue

'''


class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue(self, item):
        'insert item at rear of queue'
        return self.q.append(item)

    def dequeue(self):
        'remove and return item at front of queue'
        if self.isEmpty():
            raise KeyboardInterrupt('dequeue from empty queue')
        return self.q.pop(0)

queue = Queue()
queue.dequeue()  # Lanza: KeyboardInterrupt: dequeue from empty queue


