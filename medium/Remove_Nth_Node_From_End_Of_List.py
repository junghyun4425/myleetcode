# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''
문제 요약: 주어진 Linked List 를 끝에서 n번째 노드를 제거하는 문제.
ask: 1 -> 2 -> 3 -> 4 -> 5, 2
answer: 1 -> 2 -> 3 -> 5 (4가 제거됨)

해석:
링크드 리스트, 특히 이전의 노드정보가 없기 때문에 한cycle에 제거를 수행하려면 포인터 두개가 필요.
r포인터가 끝을 가리킨다면, l포인터는 n만큼 값을 뺀 노드를 가리키게 함.
그렇게하여 l포인터의 next값을 다다음 노드로 바꿔주면 해결.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = r = head
        cur = 1
        while r.next:
            r = r.next
            if cur > n:
                l = l.next
            cur += 1

        if cur == n:
            head = head.next
        elif r == l:
            head = None
        else:
            l.next = l.next.next
        return head
