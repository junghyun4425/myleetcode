# Problem Link: https://leetcode.com/problems/mini-parser/

'''
문제 요약: NestedInteger 클래스를 de-serialization 하는 함수를 구현하는 문제.
ask: s = "[123,[456,[789]]]"
answer: [123,[456,[789]]]

해석:
정규표현식과 stack을 활용해 문제를 해결. 사실 풀고보니 정규표현식을 안써도 상관없다는 생각이 들긴함.
우선, 정규표현식으로 숫자와 리스트들을 하나의 리스트에 파싱하고 하나씩 꺼내서 수행.
처음엔 NestedInteger 구현체가 어떤식으로 동작하는지 몰라서 여러번 테스트를 수행해봄.
'[' 를 마주칠때마다 stack에 새로운 인스턴스를 추가하고 숫자들을 넣어주는 방식.
']' 를 마주치면 pop()만 해주면 되기 때문에 심플하게 구현이 가능. 그저 숫자가 있었는지만 파악하고 추가해주면 리스트가 완성.
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        s_list = re.findall(r'(\[|\]|,|[-]*\d+)', s)
        num = ans = None
        stack = []
        for c in s_list:
            if c == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                num = None
            elif c == '[':
                new_list = NestedInteger()
                if stack: stack[-1].add(new_list)
                stack.append(new_list)
            elif c == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                ans = stack.pop()
                num = None
            else:
                num = c
        return ans if ans else NestedInteger(int(num))
