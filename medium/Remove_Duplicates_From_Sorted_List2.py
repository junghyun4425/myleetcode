# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

'''
문제 요약: 중복이 있는 정렬된 링크드 리스트가 들어오면, 중복된 노드를 모두 제거하고 헤드를 반환하는 문제.
ask: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4
answer: 1 -> 3

해석:
리스트의 중복을 완전히 지우기 위해서 dup_start와 head 두개의 포인터를 활용.
ans에 임시노드 하나에 head를 연결. 그 이유는 첫번쨰 노드부터 중복이 될 경우 지워줘야 하기 때문.
그리고는 head.val와 head.next.val가 같은지 체크하고, 값이 달라질때까지 while 루프를 수행.
값이 달라진다면 dup_start.next를 head.next로 가리키면 끝.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = dup_start = ListNode(0, head)
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                dup_start.next = head.next
            else:
                dup_start = dup_start.next
            head = head.next
        return ans.next