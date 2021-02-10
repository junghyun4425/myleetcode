# Problem Link: https://leetcode.com/problems/insertion-sort-list/

'''
문제 요약: 링크드 리스트를 insertion sort 방식으로 정렬하는 문제.
ask: 4 -> 2 -> 1 -> 3
answer: 1 -> 2 -> 3 -> 4

해석:
시간제한이 없길래 그냥 O(n^2)으로 풀면 된다고 생각해서 while문과 재귀함수를 하나씩 사용해서 문제를 해결.
그런데 time limit 이 걸려있어서 실패. 아무래도 바꾸려는 노드의 값보다 작은값을 만나면 break 해주길 원해는 모양.
다른 공부도 해야하기 때문에 일단 구현한 코드는 올려놓고 내일 prev, next 두개의 포인터로 break point를 찾으면서 처음부터 다시 풀 생각.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Failed Solution (Time limit)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def change_pos(head, cur):
            if head == cur:
                return cur
            nxt_head = change_pos(head.next, cur)
            if nxt_head.val < head.val:
                head.next = nxt_head.next
                nxt_head.next = head
                return nxt_head
            else:
                head.next = nxt_head
                return head

        cur = head
        while cur:
            tmp = cur
            cur = cur.next
            tmp = change_pos(head, tmp)
            if tmp.val < head.val:
                head = tmp
        return head