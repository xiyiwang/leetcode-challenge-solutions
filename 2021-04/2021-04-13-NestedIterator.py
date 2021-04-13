"""
LeetCode Challenge: Flatten Nested List Iterator (2021-04-13)

You are given a nested list of integers nestedList. Each element 
is either an integer or a list whose elements may also be integers 
or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:
- NestedIterator(List<NestedInteger> nestedList) Initializes the 
  iterator with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers 
  in the nested list and false otherwise.

Constraints:
- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range 
  [-10^6, 10^6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# dfs solution - O(n)
class NestedIterator:
    def __init__(self, nestedList):
        def dfs(nest):
            for x in nest:
                if x.isInteger():
                    self.queue.append(x.getInteger())
                else:
                    dfs(x.getList())
                    
        self.queue = []
        dfs(nestedList)
    
    def next(self) -> int:
        return self.queue.pop(0)
        
    def hasNext(self) -> bool:
        return True if self.queue else False
