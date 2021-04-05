"""
LeetCode Challenge: Design Circular Queue (2021-04-04)

Design your implementation of the circular queue. The 
circular queue is a linear data structure in which the 
operations are performed based on FIFO (First In First 
Out) principle and the last position is connected back 
to the first position to make a circle. It is also called 
"Ring Buffer".

One of the benefits of the circular queue is that we can 
make use of the spaces in front of the queue. In a normal 
queue, once the queue becomes full, we cannot insert the 
next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store 
new values.

Implementation the MyCircularQueue class:
- MyCircularQueue(k) Initializes the object with the size 
  of the queue to be k.
- int Front() Gets the front item from the queue. If the 
  queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue 
  is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular 
  queue. Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. 
  Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty 
  or not.
- boolean isFull() Checks whether the circular queue is full or 
  not.

Constraints:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, 
  isEmpty, and isFull.
"""

# runtime: 68 ms (beats 72.79%)
# memory usage: 14.5 MB (beats 97.53%)

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.k = k
        self.n = 0
        self.front = self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1)%self.k
        self.queue[self.rear] = value
        self.n += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty(): 
            return False

        self.queue[self.front] = None
        self.front = (self.front+1)%self.k
        self.n -= 1
        if self.isEmpty(): 
            self.front = self.rear = None
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k
