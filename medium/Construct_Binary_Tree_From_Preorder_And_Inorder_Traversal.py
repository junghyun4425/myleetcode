# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

'''
문제 요약: 바이너리 트리의 inorder, preorder 순서가 담긴 리스트가 주어졌을때, 트리를 완성해서 반환하는 문제.
ask: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
answer: [3,9,20,null,null,15,7]

해석:
몇가지 정보를 통해 Top-down 방식으로 트리를 만들어 나가는 방법으로 문제를 해결.
첫번째 정보는 preorder를 통해 트리의 루트를 알수 있다는 점.
두번째 정보는 inorder를 통해 루트 index의 왼쪽과 오른쪽은 트리의 왼쪽과 오른쪽이라는 점.
따라서, root값과 inorder 리스트에서 root의 index를 찾아낸 다음 재귀함수로 left,right를 각각 만들어 나가면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def topDown(preorder, inorder):
            if not preorder:
                return None
            root = preorder[0]
            root_i = inorder.index(root)
            return TreeNode(root, topDown(preorder[1:root_i+1],inorder[:root_i]), \
                            topDown(preorder[root_i+1:], inorder[root_i+1:]))
        return topDown(preorder, inorder)