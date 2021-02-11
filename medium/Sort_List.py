# Problem Link: https://leetcode.com/problems/sort-list/

'''
문제 요약: Linked List를 정렬하는 문제. (조건: Time Complexity O(nlogn), Space Complexity O(1))
ask: 4 -> 3 -> 2 -> 1
answer: 1 -> 2 -> 3 -> 4

해석:
시간 복잡도와 공간 복잡도를 보면, 링크드 리스트를 머지소트 요구하는 문제.
배열의 머지소트와 굉장히 유사하며 공간복잡도가 상수만큼 차지하기에 괜찮은 효율을 가짐. 다만 좀더 복잡함.
Top-Down 방식으로 반씩 갈라서 재귀함수를 호출함.
mid값을 바로 찾을 수 없기 때문에 mid를 탐색해야하고, mid와 그 앞의 연결을 끊어야 사이클을 막을 수 있음.
그외엔 배열에서의 머지소트와 유사하기 때문에 배열에서 할줄 알면 큰 무리없이 문제 해결가능.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def getMid(head):
            tmp = ListNode(0, head)
            while head and head.next:
                tmp = tmp.next
                head = head.next.next
            mid = tmp.next
            tmp.next = None
            return mid

        def merge(left, right):
            merged = ListNode()
            merged_start = merged
            while left and right:
                if left.val < right.val:
                    merged.next = left
                    left = left.next
                else:
                    merged.next = right
                    right = right.next
                merged = merged.next
            if left:
                merged.next = left
            else:
                merged.next = right
            return merged_start.next

        def mergeSort(head):
            if not head or not head.next:
                return head
            mid = getMid(head)
            left = mergeSort(head)
            right = mergeSort(mid)
            return merge(left, right)

        return mergeSort(head)