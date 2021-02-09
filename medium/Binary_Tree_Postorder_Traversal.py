# Problem Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

'''
문제 요약: 입력으로 들어오는 트리의 postorder 순서로 배열에 반환하는 문제. (단, 재귀함수 사용하지 않고)
ask: [1,null,2,3]
answer: [3,2,1]

해석:
이 문제 또한 재귀함수를 사용하면 안되기에 스택을 활용해 해결하려고 시도.
어떤 규칙을 찾기전에 그냥 왼쪽으로 내려갔다가 오른쪽으로 한칸씩 가고 하는 방법으로 또 하려했지만 visited 같은 배열이 필요하기에 어떤 규칙을 찾어봄.
Postorder의 한가지 특징은 리프노드라면 왼쪽,오른쪽 순서를 출력하고 루트로 올라가는 사실이며 이를 반복.
하지만 문제는 위에서부터 출력을 안하면 코딩이 굉장히 까다로워 지기 때문에, 애초에 위에서부터 출력해서 순서를 뒤집는 방법을 생각해냄.
상위루트부터 출력을 먼저하고, 아래 하위노드를 스택에 저장. (뒤집어야 하므로 right를 먼저 방문해야 하므로 스택에 left, right 순서로 저장)
이렇게 끝까지 들리고 마지막에 뒤집으면 postorder 의 결과와 같아짐.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            ans.append(node.val)
            stack.extend([node.left, node.right])
        return ans[::-1]