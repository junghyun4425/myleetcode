# Problem Link: https://leetcode.com/problems/binary-search-tree-iterator/

'''
문제 요약: 트리를 inorder 순으로 탐색하는 클래스를 구현하는 문제.
ask:
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
answer:
[null, 3, 7, true, 9, true, 15, true, 20, false]

해석:
inorder 순서로 트리를 미리 탐색한 다음 배열에 저장.
cur 포인터와 현재 길이만 알고 있으면 next() 와 hasNext() 함수를 모두 O(1)의 시간복잡도를 가지게 구현이 가능.
단, Initialize 할 때에는 O(n)의 탐색시간이 걸림.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = []
        self.cur = 0
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.inorder.append(root.val)
            root = root.right
        self.size = len(self.inorder)

    def next(self) -> int:
        self.cur += 1
        return self.inorder[self.cur-1]

    def hasNext(self) -> bool:
        return self.cur < self.size


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()