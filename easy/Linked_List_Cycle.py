# Problem Link: https://leetcode.com/problems/linked-list-cycle/

'''
문제 요약: 리스트가 사이클인지 아닌지 판단하는 문제.
ask: head = [3,2,0,-4], pos = 1 (pos는 사이클 지점)
answer: True

해석:
해쉬맵에 노드를 저장하면서 가면 사이클인지 아닌지 쉽게 판단이 가능해서 문제를 해결.
하지만 문제 끝부분에 memory O(1) 제한이 추가적인 도전과제로 남아있어서 도전.
사실 여러방법을 생각해봤지만 마땅히 안떠오르고 그나마 가능성있는 포인터 두개로 하나는 한칸씩, 다른 하나는 두칸씩 가는걸로 해봄.
일단 잘 동작하고, 정확한 원리는 모르겠지만 몇가지 예를 들어서 증명함.

사이클이 돈다면 일단 같은곳을 기준으로 다시 돌아오는데 필요한 비용은 무조건 짝수이기 때문에, 2배씩 출발하고 한칸씩 가면 만나게 되어있음.
이때 만나는 길이가 생각보다 길지않음. 2칸씩 건너뛰기 때문에, 사이클 두바퀴를 돌기전에 만나는게 대부분이고 O(n)의 시간복잡도를 가짐.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Optimized Solution time O(n) / space O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

# Simple Solution with dictionary
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        d = {}
        while head not in d:
            d[head] = True
            if not head.next:
                return False
            head = head.next
        return True
'''