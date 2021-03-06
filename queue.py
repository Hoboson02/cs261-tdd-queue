# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Ryan Earl

# Hint: pip3 install llist
from llist import sllist
class Queue:

    def __init__(self): 
        self.data =sllist()
    
    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self): 
        return self.data.popleft()

    def is_empty(self): 
        return self.data.size == 0