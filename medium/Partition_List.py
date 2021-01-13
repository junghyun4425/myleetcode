# Problem Link: https://leetcode.com/problems/partition-list/

'''
문제 요약: 링크드리스트가 주어졌을때, x보다 작은값은 왼쪽 큰값은 오른쪽에 나열하되, 순서는 있는 그대로 정렬없이 반환하는 문제.
ask: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
answer: 1 -> 2 -> 2 -> 4 -> 3 -> 5

해석:
정렬이 아니라 있는 그대로의 순서에 대한 x보다 큰값 작은값을 찾아내야하기 때문에 다소 생소한 문제.
어렵게 생각해서 이것저것 시도해 보는데 자꾸 꼬였으며, 문제를 정확히 이해하지 못한 잘못이 큼.
문제에서 정렬이 아니라 있는 '그대로'의 순서 이기 때문에, while 문으로 리스트를 탐색하는 동안 작은값, 큰값을 나눠주기만 하면 끝.
small 에 작은값을, large에 크거나 같은값을 연결시켜주고 마지막엔 small을 large_head에 연결시켜주면 완성.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small, large = ListNode(), ListNode()
        small_head, large_head = small, large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
            small.next = large.next = None

        small.next = large_head.next
        return small_head.next