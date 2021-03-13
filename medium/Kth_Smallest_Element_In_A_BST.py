# Problem Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

'''
문제 요약: BST가 들어올때 k번째 값을 반환하는 문제.
ask: root = [3,1,4,null,2], k = 1
answer: 1

해석:
BST의 정렬된 값을 찾으려면 inorder 순서로 값을 가져오면 됨.
따라서 처음 시도에는 recursive한 방법으로 간단하게 해결해봄.
여기서 단점은 쓸데없는 계산과 메모리를 소비한다는 점. 중간에 return해서 결과를 바로 받아올 수 없기 때문.

따라서 두번째 시도는 while문으로 iterative하게 해결함.
공간적, 시간적 모두 성능이 향상됨.
left를 우선적으로 탐색하고 좌측으로 더이상 갈곳이 없다면 실제 첫번째 순서에 도착.
이후, k를 하나씩 빼주면서 1이 될때까지 반복하고 만약 k가 1이된다면 바로 결과를 리턴해서 수행을 종료함.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Second Try (iteration with inorder) - Better performance in both time and space than First Try.
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if k == 1:
                return cur.val
            k -= 1
            cur = cur.right
        return -1


# First Try (recursion with inorder)
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans[k-1]
'''