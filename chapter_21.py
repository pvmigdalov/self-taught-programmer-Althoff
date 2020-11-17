import time
from random import randint


class Stack:
    def __init__(self, *args):
        self.items = list(args)

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.items:
            return False
        return True



class Queue:
    def __init__(self, *args):
        self.items = list(args)

    def size(self):
        return len(self.items)

    def enqueue(self, x):
        self.items.insert(0, x)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        if self.items:
            return False
        return True

    @classmethod
    def simulation(cls, till_show, max_time, *args):
        queue = Queue(*reversed(args))
        now = time.time()
        end = now + till_show
        tix_sold = []

        while now < end and not queue.is_empty():
            time_of_service = randint(0, max_time)
            # time.sleep(time_of_service)
            person = queue.dequeue()
            tix_sold.append(person)
            now += time_of_service
        return tix_sold




if __name__ == '__main__':
    print('DEMONSTRATION OF WORK OF STACK')
    stack = Stack()
    for c in 'Hello':
        stack.push(c)

    reverse = ''
    while not stack.is_empty():
        reverse += stack.pop()
    print(reverse)
    print()
    
    print('SIMULATION OF QUEUE')
    people = ['person ' + str(i) for i in range(1, 27)]
    sold = Queue.simulation(115, 11, *people)
    print('The people served: ' + ', '.join(sold))