# Problem Link: https://leetcode.com/problems/implement-queue-using-stacks/

'''
문제 요약: 스택 2개로 큐를 구현하는 문제.
ask:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
answer: [null, null, null, 1, 1, false]

해석:
여러 방법이 있겠지만 push할때 스택을 큐로 만들어놓는 방법을 선택. push할때만 O(n)의 시간복잡도를 가지고 나머지 연산에서는 O(1).
push할때 stack이 비어있다면 top값을 기록하고 stack에 단순 저장.
stack에 값이 있다면 값을 다른스택에 다 빼준다음 새로온값을 추가해주고 다시 원래 stack에 저장하게되면 큐와 같이 저장됨.
큐와 스택의 원리만 알면 간단히 해결됨. 물론 정공법이 아니게 풀면 메모리를 아낄수있지만 정석대로 풀어봄.
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.top = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.top = x
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = self.stack1.pop()
        if self.stack1:
            self.top = self.stack1[-1]
        return tmp

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.top

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1 == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()