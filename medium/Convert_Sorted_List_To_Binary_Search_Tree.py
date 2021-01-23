# Problem Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

'''
문제 요약: 정렬된 순서의 링크드리스트가 주어질때, balanced BST 로 바꾸는 문제.
ask: -10->-3->0->5->9
answer: [0,-3,9,-10,null,5]

해석:
원리를 몰랐을때 많이 어려운 문제. 단순히 생각했을때 root를 찾고 왼쪽 오른쪽을 재귀함수로 subtree를 생성해 반환하는 방식으로 해결.
링크드리스트를 리스트로 바꿔서 쉽게 해결을 했지만, 메로리를 사용할 수 없다고 하면 몇개의 pointer를 통해 가운데 노드를 찾아야 함.
배열형태면 가운데값을 찾기 굉장히 쉽기 때문에 이런 방법으로 문제를 품.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        def makeTree(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(vals[m], makeTree(l, m-1), makeTree(m+1, r))
        return makeTree(0, len(vals)-1)