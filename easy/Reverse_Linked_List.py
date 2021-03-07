# Problem Link: https://leetcode.com/problems/reverse-linked-list/

'''
문제 요약: 링크드리스트를 뒤집는 문제.
ask: 1->2->3->4->5
answer: 5->4->3->2->1

해석:
start 노드를 하나 생성하고, 재귀함수를 통해 뒤에서부터 앞으로 연결을 바꿔가는 방법으로 해결.
재귀함수가 편해서 이런 방법으로 풀긴 했으나, 다음에 복습을 하게된다면 iterative하게 풀어는걸로.
iterative면 처음부터 바꿔가면 되기 때문에 시간복잡도나 공간복잡도는 현재 풀이한 방식과 같을거라 예상.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1)
        def recursion(head):
            if not head:
                return new_head
            prev = recursion(head.next)
            prev.next = head
            head.next = None
            return head
        recursion(head)
        return new_head.next