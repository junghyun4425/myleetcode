# Problem Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

'''
문제 요약: 바이너리 트리를 depth 단위로 묶어서 출력하는 문제. 단, 지그재그 순으로 반환.
ask: [3,9,20,null,null,15,7]
answer: [[3],[20,9],[15,7]]

해석:
이전의 Binary_Tree_Level_Order_Traversal 문제와 거의 같은 문제.
이 또한 두개의 큐를 사용하여 BFS 방식으로 탐색하면 해결이 가능.
큐는 level안의 트리를 꺼내고 다른 큐는 꺼낸 트리의 자식들을 저장해 level 단위로 큐를 저장시킴.
꺼낸 트리의 val 를 묶은것을 ans 리스트에 붙여놓는데, reverse라는 트리거가 True인 경우 반대로 넣으면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = [root]
        reverse = False

        while queue:
            queue2 = []
            level = []
            while queue:
                tree = queue.pop(0)
                if tree:
                    queue2.extend([tree.left, tree.right])
                    level.append(tree.val)
            if level:
                ans.append(level[::-1] if reverse else level)
                reverse = False if reverse else True
            queue = queue2
        return ans