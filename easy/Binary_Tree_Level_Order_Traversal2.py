# Problem Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

'''
문제 요약: 바이너리 트리를 레벨단위로 출력하되, 반대 순서대로 출력하는 문제.
ask: [3,9,20,null,null,15,7]
answer: [[15,7],[9,20],[3]]

해석:
Binary_Tree_Level_Order_Traversal 문제와 굉장히 유사한 문제.
큐 두개를 활용해 레벨단위로 값을 리스트로 만들고 저장. 마지막에 반대로 리턴만 해주면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        ans = []
        while queue:
            queue2 = []
            level = []
            while queue:
                tree = queue.pop(0)
                if tree:
                    queue2.extend([tree.left, tree.right])
                    level.append(tree.val)
            if level:
                ans.append(level)
            queue = queue2
        return ans[::-1]