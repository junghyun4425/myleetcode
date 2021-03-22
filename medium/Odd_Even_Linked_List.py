# Problem Link: https://leetcode.com/problems/odd-even-linked-list/

'''
문제 요약: 링크드 리스트의 짝수번째 노드를 순서대로 리스트 마지막 위치로 옮기는 문제.
ask: 1->2->3->4->5
answer: 1->3->5->2->4

해석:
우선 사이즈를 구해서 몇번만큼의 작업을 수행할지 결정함과 동시에 tail의 포인터를 리스트 끝에 가리키게 함.
그리고 노드를 옮겨주는데, odd는 그다음번째 odd 노드를 가리키게 함.
even노드는 tail포인터를 이용해 뒤쪽으로 옮겨줌.
리스트간 링크만 잘 바꿔주면 상수 공간복잡도 내에 해결되는 문제.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        size = 1
        tail = odd = head
        while tail.next:
            tail = tail.next
            size += 1
        for _ in range(size//2):
            even = odd.next
            if even == tail: break
            tail.next, even.next, odd.next = even, None, odd.next.next
            tail = tail.next
            odd = odd.next
        return head