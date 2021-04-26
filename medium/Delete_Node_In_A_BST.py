# Problem Link: https://leetcode.com/problems/delete-node-in-a-bst/

'''
문제 요약: BST와 key가 주어질때 key값을 가진 노드를 삭제하는 문제.
ask: root = [5,3,6,2,4,null,7], key = 3
answer: [5,4,6,2,null,null,7]

해석:
노드를 삭제하는것 자체는 크게 어렵지 않았으나, 재귀를 효율적으로 구현하는데 많은 시간이 걸렸던 문제.
삭제를 위해서는 필요한 노드가 삭제해야 할 노드의 이전노드, 삭제될 노드 위치에 올 노드 등을 상황에 따라 필요하게 됨.
우선, 노드가 삭제되는 위치를 찾은다음 노드의 왼쪽과 오른쪽 자식이 있는지 확인해야함.
만약 자식노드가 둘중 하나라도 없으면 굉장히 편해지는데, 한쪽이 없다면 반대쪽 노드를 땡겨오면 끝나기 때문.
자식노드가 둘다 있다면 두가지 방법이 있으며 오른쪽 자식에서 최소값을 찾고 그 노드를 삭제된 노드자리에 옮기는 방법을 선택.
(다른 방법은 왼쪽에서 최대값을 찾아 옮기면 됨)
최소값을 가지는 노드를 찾았다면, 삭제 위치로 옮기고 기존의 노드에서는 지움.
그리고 자식들은 기존의 왼쪽과 오른쪽 그대로 데려오면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def findMin(root):
            if not root.left:
                return root
            return findMin(root.left)
        def deleteKey(root, key):
            if not root:
                return
            if root.val > key:
                root.left = deleteKey(root.left, key)
            elif root.val < key:
                root.right = deleteKey(root.right, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                node = findMin(root.right)
                node.right = deleteKey(root.right, node.val)
                node.left = root.left
                root = node
            return root
        return deleteKey(root, key)