# Problem Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

'''
문제 요약: 트리에서 가장 큰값을 가지는 path를 찾아 그 값을 반환하는 문제. (path는 한쪽방향으로만 진행되며 어느위치에서 시작해도 상관없음)
ask: root = [-10,9,20,null,null,15,7]
answer: 42 (15 -> 20 -> 7 또는 7 -> 20 -> 15 /// 단, 20 -> 15 -> 7 은 안됨:양방향 path는 x)

해석:
Brute Force 방식으로 하기엔 시간복잡도가 최악의 상황. 모든 노드를 시작점으로 하면서 가능한 한방향 경로를 모두 탐색해야하기 때문.
그렇기에 Bottom-up 방식으로 가장 아래쪽부터 차근차근 올라가며 최대값을 구하기로 결정.
우선 left와 right 방향으로 재귀함수를 통해 리프노드로 이동한 다음 최상위에 있는 root까지 max값을 찾으며 올라감.
단, 여기서 몇가지 주의사항이 있는데 한번에 2군데의 경로를 갈수 없기 때문에 선택을 해야함.

1. 상위 root로 올라가는 경우 left나 right 둘중 하나만 계산에 포함.
2. 상위 root로 안올라가고 left,right 모두를 포함한 path.

1번은 왼쪽 또는 오른쪽 중에서 큰값을 선택해 값을 반환. ( max(root.val + left, root.val + right, 0) )
여기서 0의 의미는, 혹시 값이 음수라면 없는경로 취급해야 하기 때문.
2번은 그 자리에서 root.val + left + right 값이 ans보다 크면 갱신하고 넘어가면 끝.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        def maxSum(root):
            nonlocal ans
            if not root:
                return 0
            left = maxSum(root.left)
            right = maxSum(root.right)
            if left + right + root.val > ans:
                ans = left + right + root.val
            return max(root.val + left, root.val + right, 0)
        maxSum(root)
        return ans