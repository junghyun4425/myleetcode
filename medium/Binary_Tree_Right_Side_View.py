# Problem Link: https://leetcode.com/problems/binary-tree-right-side-view/

'''
문제 요약: 트리의 오른쪽에서 봤을때 가장 먼저 보이는 노드들의 숫자를 순서대로 리스트에 반환하는 문제.
ask: [1,2,3,null,5,null,4]
answer: [1,3,4]

해석:
큐를 두개 사용해서 트리의 레벨단위로 묶은 다음, 마지막 노드만 ans에 추가하는 방식으로 해결.
물론 dfs나 bfs와 같이 효율적으로 푸는 방법도 있지만 이 방법으로 도전해봄.
다음에 복습하게 된다면 재귀함수 형태로 문제를 풀어볼 것.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            nxt_queue = []
            ans.append(queue[-1].val)
            while queue:
                root = queue.pop(0)
                if root.left:
                    nxt_queue.append(root.left)
                if root.right:
                    nxt_queue.append(root.right)
            queue = nxt_queue
        return ans