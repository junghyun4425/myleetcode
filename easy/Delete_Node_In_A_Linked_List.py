# Problem Link: https://leetcode.com/problems/delete-node-in-a-linked-list/

'''
문제 요약: 링크드 리스트에서 삭제되어야 하는 노드가 주어질때 노드를 삭제하는 문제.
ask: 4->1->5->9, node = 1
answer: 4->5->9

해석:
연결리스트가 안주어져 처음에 당황했던 문제. 알고보니 링크드 리스트는 따로 주어지지 않고, 그 리스트의 삭제해야할 노드만 주어짐.
생각보다 고민을 깊게 해서 풀게됨.
현재 노드의 정보만 가지고 있기 때문에 이전노드에서 노드의 링크를 끊는게 불가능한 상황.
사용할수 있는 데이터는 다음단계의 값.
따라서 다음단계의 값을 현재 노드에 복사하면 '삭제 + 다음노드 복사' 두가지 일이 발생하는 격.
그럼 다음노드 복사한 링크를 끊어주면 삭제가 되어버리므로 해결.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next