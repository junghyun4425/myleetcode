# Problem Link: https://leetcode.com/problems/implement-stack-using-queues/

'''
문제 요약: 큐 2개를 활용해 스택의 push, pop, top 기능을 구현하는 문제.
ask:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
answer:
[null, null, null, 2, 2, false]

해석:
너무 유명한 큐 2개로 스택 만드는 문제.
큐에 담았다가 그걸 다시 다른큐에 담으면 스택처럼 바뀌기 때문에 이를 활용하면 스택처럼 쓸수 있음.
먼저 queue1에 모든 값을 다 담아놓고 pop()함수가 호출되면 하나씩 제거하면서 queue2에 담음.
마지막값만 return하고 queue2의 내용을 다시 queue1에 넣어주면 마지막값만 빠져나온 상태.
'''

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            tmp = self.queue1.pop(0)
            self.queue2.append(tmp)
        tmp = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue1 == [] and self.queue2 == []

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
