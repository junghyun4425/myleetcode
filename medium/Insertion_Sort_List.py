# Problem Link: https://leetcode.com/problems/insertion-sort-list/

'''
문제 요약: 링크드 리스트를 insertion sort 방식으로 정렬하는 문제.
ask: 4 -> 2 -> 1 -> 3
answer: 1 -> 2 -> 3 -> 4

해석:
시간제한이 없길래 그냥 O(n^2)으로 풀면 된다고 생각해서 while문과 재귀함수를 하나씩 사용해서 문제를 해결.
그런데 time limit 이 걸려있어서 실패. 아무래도 바꾸려는 노드의 값보다 작은값을 만나면 break 해주길 원해는 모양.
다른 공부도 해야하기 때문에 일단 구현한 코드는 올려놓고 내일 prev, next 두개의 포인터로 break point를 찾으면서 처음부터 다시 풀 생각.

두번째 시도.
start 라는 더미 노드로 시작. (prev, next 포인터 두개를 사용)
start부터 하나씩 붙여가고, prev와 next는 start에서 항상 시작해 값을 비교해 나감.
next가 현재 노드보다 큰 경우엔 그자리를 바꿔주면 됨. (start 노드에 붙여주기)
이런식으로 start 노드를 완성시켜서 정렬을 완료.
중요한건 time limit을 만족하냐 못하냐 이기 때문에 쓸데없는 계산을 피하기 위해 도중에 바로 break문으로 나갈 수 있게끔 설계.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Passed Solution
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        start = ListNode(-1)
        while head:
            next_head = head.next
            prev, nxt = start, start.next
            while nxt:
                if nxt.val > head.val:
                    break
                prev = nxt
                nxt = nxt.next
            head.next = nxt
            prev.next = head
            head = next_head
        return start.next

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