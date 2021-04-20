# Problem Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

'''
문제 요약: Double Linked List가 들어오면, 다차원 리스트들을 일차원으로 평평하게 펴서 반환하는 문제.
ask: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
answer: [1,2,3,7,8,11,12,9,10,4,5,6]

해석:
child라는 변수에 None이면 따로 연결된게 없고, 링크드리스트 객체를 가리키고있다면 2차원인 상태.
따라서 이들을 1차원으로 펴줘야 하는 링크드리스트 문제.
재귀함수 혹은 stack을 활용해서 풀수있는 문제로, child가 있으면 진행을 멈추고 자식 리스트를 먼저 탐색해야 함.
prev, next 두개를 2차원의 시작점과 끝점을 가운데로 오게끔만 붙여주면 되는 생각보다 간단한 문제.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head:
                return None
            while head.next or head.child:
                if head.child:
                    end = dfs(head.child)
                    if head.next:
                        head.next.prev, end.next = end, head.next
                    head.next, head.child.prev = head.child, head
                    head.child, head = None, end
                else:
                    head = head.next
            return head
        dfs(head)
        return head