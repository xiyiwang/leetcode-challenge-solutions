# LeetCode Challenge: Peeking Iterator (02/08/2021)

#   Given an Iterator class interface with methods: next() 
#   and hasNext(), design and implement a PeekingIterator 
#   that support the peek() operation -- it essentially 
#   peek() at the element that will be returned by the next 
#   call to next(). 
# 
#   Follow up: How would you extend your design to be generic 
#   and work with all types, not just integer?

#   Submission Detail:
#   * Runtime: 28 ms (better than 88.51% of python3 submissions)
#   * Memory Usage: 14.3 MB (better than 96.63% of python3 submissions)

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._current = None
        self._peeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._peeked:
            self._current = self._iterator.next()
            self._peeked = True
        return self._current

    def next(self):
        """
        :rtype: int
        """
        if self._peeked:
            self._peeked = False
        else:
            self._current = self._iterator.next()
        return self._current
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peeked or self._iterator.hasNext()
