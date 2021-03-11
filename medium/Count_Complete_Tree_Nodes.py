# Problem Link: https://leetcode.com/problems/count-complete-tree-nodes/

'''
문제 요약: 완전이진 트리의 노드개수를 반환하는 문제.
ask: [1,2,3,4,5,6]
answer: 6

해석:
중위, 후위 전위 순회아무거나 골라도 문제를 해결할수 있음. 단, 시간복잡도는 O(n).
문제의 조건에서 시간복잡도를 더 줄일수 있는지에 대한 제약조건을 가짐.
따라서 O(1) 혹은 O(logn) 방식으로 해결하라는 건데, O(1)은 도저히 생각나지 않아서 패스.
O(logn)은 모두 순회하지 않고 높이탐색으로만 알아내야 가능함.
이를 top-down방식으로 해결함.
가장 높은 노드에서 왼쪽과 오른쪽으로 쭉 내려갔을때 높이가 같다면 완전이진트리+포화이진트리이기 때문에 그 개수를 넘겨주면 끝.
만약 다르다면, root를 왼쪽과 오른쪽으로 하나씩 내려서 다시 그 작업을 반복하면 O(logn)으로 해결이 가능.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def recursion(root):
            if not root:
                return 0
            l = r = root
            hl = hr = 0
            while l:
                l = l.left
                hl += 1
            while r:
                r = r.right
                hr += 1
            if hl == hr:
                return 2 ** hl - 1
            return 1 + recursion(root.left) + recursion(root.right)
        return recursion(root)