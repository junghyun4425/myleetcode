# Problem Link: https://leetcode.com/problems/validate-binary-search-tree/

'''
문제 요약: 트리가 BST를 만족하는지 확인하는 문제.
ask: [5,1,4,null,null,3,6]
answer: False (root node 는 5 지만, 오른쪽 자식이 4이므로 BST를 만족하지 못함)

해석:
잘못된 접근방법으로 한번 헤맨 문제. 처음 접근할 때는 그저 부모와 왼쪽자식의 관계, 오른쪽자식의 관계만 파악하면 될 줄 알고 해결을 시도.
특정 케이스에는 될지 몰라도 root = [5,1,6,null,null,4,7] 와 같은 경우는 오답을 냄. 이유는 부모뿐 아니라 부모의 부모와도 그 관계가 성립해야 하기 때문.
따라서, 부모와 자식간의 비교만으론 문제를 해결하기 힘들기 때문에 루트부터 쭉 순서대로 따라가면서 순서에 부합한 경우를 찾아내는 방법으로 해결.
Tree를 순서대로 서치하면서 이전값인 prev와 값을 비교하기만 하면 끝.
스택을 활용해 풀었으며, 연습을 위해 재귀함수로도 풀어봄. prev의 로컬변수 할당을 시도해서 문제가 생겼기에 시간이 걸렸지만 좀더 깊게 이해하는 계기가 됨.
(prev = [root.val] 를 시도하면 에러나는데 처음엔 이해를 잘 못했었음...)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def searchByOrder(root):
            if not root:
                return True
            if not searchByOrder(root.left) or root.val <= prev[0]:
                return False
            prev[0] = root.val
            return searchByOrder(root.right)
        prev = [float('-inf')]
        return searchByOrder(root)

'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev[-1] >= root.val:
                return False
            prev = [root.val]
            root = root.right
        return True
'''