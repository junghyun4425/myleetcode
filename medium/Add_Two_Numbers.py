# Problem Link: https://leetcode.com/problems/add-two-numbers/

'''
문제 요약: 두개의 ListNode 에 적혀진 값을 역순으로 값을 만들어 더하고, 역순의 리스트노드로 반환하기.
ask: l1 = 2 -> 4 -> 3, l2 = 5 -> 6 -> 4
answer: 7 -> 0 -> 8
(342 + 564 = 807)

해석:
내가 풀은 방법은 단순하게 자리수 값들을 실제 숫자로 변환하고, 더한 뒤 다시 리스트 노드를 만드는 과정을 포함했다.
하지만 그럴 필요없이 l1, l2 를 탐색할때 같이 result를 만들어주면 된다. 그럼 더 깔끔하고 빠른 코드가 된다.
(나의 runtime은 80ms이나, 60ms대로 줄일 수 있다)
주의할점은 덧셈한 결과가 한자리 수 늘어나면 carry란 변수를 사용해 처리해 줘야 한다는 점.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = getNum(l1)
        num2 = getNum(l2)
        result = list(map(int, str(num1 + num2)))
        ln = ListNode(result[-1], None)

        for i in range(len(result) - 2, -1, -1):
            addNode(ln, result[i])
        return ln

def addNode(ln, num):
    while ln.next:
        ln = ln.next
    ln.next = ListNode(num)

def getNum(ln: ListNode) -> ListNode:
    num = 0
    deci = 1
    while ln:
        num += ln.val * deci
        deci *= 10
        ln = ln.next
    return num