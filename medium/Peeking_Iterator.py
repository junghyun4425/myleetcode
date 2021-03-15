# Problem Link: https://leetcode.com/problems/peeking-iterator/

'''
문제 요약: iterator 객체를 이용해서 peek기능이 있는 iterator를 구현하는 문제. (peek는 다음 값만 보여주고 실제로 다음 포인터로 넘어가지 않는 기능)
ask:
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
answer:
[null, 1, 2, 2, 3, false]

해석:
iterator를 그대로 가져와서 시간복잡도 O(1)에 모든게 해결가능함.
다음값을 val에 미리 저장해 놓는다는 점을 제외한 나머지는 iterator와 유사함.
단, val에 값을 불러올때마다 hasNext()로 검사하고 불러와야함. 값이 없다면 None을 가지게 하면 끝.
굉장히 간단해서 medium보다는 easy같은 느낌.
'''


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.val = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.val

    def next(self):
        """
        :rtype: int
        """
        tmp = self.val
        self.val = self.iterator.next() if self.iterator.hasNext() else None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.val != None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].