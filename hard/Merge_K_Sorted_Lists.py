# Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

'''
문제 요약: 숫자를 가진 링크드 리스트들을 받아서 정렬하여 하나의 링크드 리스트로 반환하는 문제.
ask: [1 -> 2 -> 4, 1 -> 3 -> 4, 7 -> 8]
answer: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 7 -> 8

해석:
O(n)만큼의 space를 사용해서 링크드 리스트 값들을 리스트로 바꾼뒤, 정렬(nlogn) 한 뒤 다시 링크드 리스트를 새로 생성하여 반환.
간단하게론 문제를 해결했지만 더 효율적인 방법으로 Priority Queue를 써서 해결하는 방법이 있었기 때문에, 다시 풀어봄.
'''

'''
Solved as a First Try

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        lists_len = len(lists)
        if lists_len == 0:
            return None
        for i in range(lists_len):
            while lists[i]:
                l.append(lists[i].val)
                lists[i] = lists[i].next
        l.sort()
        l_len = len(l)
        ans = pointer = ListNode(0)
        for i in range(l_len):
            pointer.next = ListNode(l[i])
            pointer = pointer.next
        return ans.next
'''

'''
Solved using Priority Queue
'''

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()
        ans = pointer = ListNode(0)

        for i, l in enumerate(lists):
            if l:
                pq.put((l.val, i))

        while not pq.empty():
            v, i = pq.get()
            pointer.next = ListNode(v)
            pointer = pointer.next
            lists[i] = lists[i].next
            if lists[i]:
                pq.put((lists[i].val, i))
        return ans.next
