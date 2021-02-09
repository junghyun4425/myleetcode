# Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

'''
문제 요약: 입력으로 들어오는 트리의 preorder 순서로 배열에 반환하는 문제. (단, 재귀함수 사용하지 않고)
ask: [1,null,2,3]
answer: [1,2,3]

해석:
재귀함수를 사용하지 않아야 하는 챌린지 덕분에 하나 크게 배워간 문제.
사실 트리의 pre-order 탐색문제가 나오면 모두 재귀함수로 풀어서, 반복문 만으로 하려면 뭔가 어렵게 풀어야할 것 같았음.
따라서 처음에는 stack에 left먼저 진행하면서 노드를 저장함과 동시에 ans 배열에 val값을 저장함.
반복되는 노드들이 ans에 출력됨을 방지하기 위해 visited라는 해쉬맵도 추가.
갈수록 복잡해져가는 구조에 이런 문제가 아닐거라 생각하고 오랫동안 고민한 끝에 스택 하나만으로 해결되는 방법을 깨달음.
스택에 left가 아닌 right먼저 넣어놓으면 해결이 되는걸 정말 멀리 돌아서 온 느낌. 역시 경험이 중요...
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans