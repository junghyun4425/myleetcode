# Problem Link: https://leetcode.com/problems/min-stack/

'''
문제 요약: 최소값 출력이 가능한 스택을 구현하는 문제.
ask:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
answer:
[null,null,null,null,-3,null,0,-2]

해석:
스택 자체를 구현하는건 어려운 일이 아니지만 최소값을 관리해야 하는데 어떻게하면 효율적으로 할지 고민을 했던 문제.
min 값들을 관리하는 배열을 추가시켜서 해결. 들어오는 모든값을 min에 저장하지 않도록 약간의 최적화를 함.
input으로 들어오는 값 x 보다 현재 스택의 min_val값이 클때만 x값을 min에 저장함.
min_val보다 큰값들이 계속 추가된다 해도 min값은 이전에 있기 때문에 pop()을 한다해도 getMin() 함수에 영향을 끼치지 못함.
고로 큰값들은 min에 고려대상이 되지 않음.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        self.min_val = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min_val:
            self.mins.append(self.min_val)
            self.min_val = x

    def pop(self) -> None:
        if self.stack.pop() == self.min_val:
            self.min_val = self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()