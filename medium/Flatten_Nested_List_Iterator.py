# Problem Link: https://leetcode.com/problems/flatten-nested-list-iterator/

'''
문제 요약: 입력으로 들어오는 다차원 배열을 flatten 배열로 만드는 문제.
ask: [[1,1],2,[1,1]]
answer: [1,1,2,1,1]

해석:
NestedInteger라는 클래스가 제공되고 이를 통해 1차월 배열로 만드는 작업을 수행하도록 해야함.
즉, next()나 hasNext()함수 구현이 중점이 아닌 init()함수에서 배열을 flat하게 만든느 작업이 중점.
다차원 배열을 만나면 그 배열을 현재 NestedList의 앞단에 extend로 붙여줘서 해결함.
앞단에 붙였기 때문에 순서에 지장이 없고 다차원 배열이라도 계속 flat작업이 가능함.
꽤나 단순하게 구현한거라 성능 자체는 중위권 정도. 나중에 복습하게되면 최적화를 시도해 볼것.
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
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

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatList = []
        while nestedList:
            if nestedList[0].isInteger():
                self.flatList.append(nestedList[0].getInteger())
                nestedList.pop(0)
            elif nestedList[0].getList() != []:
                tmp = nestedList[0].getList()
                nestedList.pop(0)
                nestedList = tmp + nestedList
            else:
                nestedList.pop(0)

    def next(self) -> int:
        return self.flatList.pop(0)

    def hasNext(self) -> bool:
        return self.flatList != []

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())