# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

'''
문제 요약: 바이너리 트리의 inorder, postorder 순서가 담긴 리스트가 주어졌을때, 트리를 완성해서 반환하는 문제.
ask: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
answer: [3,9,20,null,null,15,7]

해석:
이전 문제와 마찬가지로 몇가지 정보를 통해 Top-down 방식으로 트리를 만들어 나가는 방법으로 문제를 해결.
첫번째 정보는 postorder를 통해 트리의 루트를 알수 있다는 점. (가장 마지막 위치)
두번째 정보는 inorder를 통해 루트 index의 왼쪽과 오른쪽은 트리의 왼쪽과 오른쪽이라는 점.
따라서, root값과 inorder 리스트에서 root의 index를 찾아낸 다음 재귀함수로 left, right를 각각 만들어 나가면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def topDown(inorder, postorder):
            if not inorder:
                return None
            root = postorder[-1]
            root_i = inorder.index(root)
            return TreeNode(root, topDown(inorder[:root_i], postorder[:root_i]), \
                            topDown(inorder[root_i+1:], postorder[root_i:-1]))
        return topDown(inorder, postorder)