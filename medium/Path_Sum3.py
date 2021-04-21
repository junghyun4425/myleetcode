# Problem Link: https://leetcode.com/problems/path-sum-iii/

'''
문제 요약: 바이너리 트리의 path 중에서 합이 targetSum과 동일한 값이 되는 합의 경우의 수를 구하는 문제.
ask: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
answer: 3

해석:
바이너리 트리를 처음 지점부터 더해가면서, 혹은 현재 노드부터의 path 합이 타겟과 일치하는지 확인해야 하는 문제.
우선 처음에는 간단하게 모든 sum들을 리스트에 저장하고 target과 일치하는 경우를 더해서 반환하는 방식으로 해결해봄.
아이디어 자체는 괜찮다고 생각하지만 트리가 커지면 커질수록 공간복잡도는 기하급수적으로 상승하게 되므로, 사실 메모리 초과로 실패를 예상함.
의외로 통과했다는 것에 놀랐지만, 최적화를 바로 시도해봄.

시간복잡도: 리스트레서 해쉬맵으로 바꿔 탐색 시간을 줄임.
공간복잡도: 모든 수를 다 저장하는게 아니라, 여태까지 더해온 합을 해쉬맵에 카운팅하는 방식으로 효과적으로 활용함.
카운팅을 하기 때문에 만약 해쉬맵안에 현재 합과 일치하는 값이 존재한다면 targetSum과 일치하다는 의미이기 때문에 최종적으로 카운팅을 해줌.
처음 sums[0] = 1 을 추가한 이유는 더해서 0이 되는 경우가 있었을때(완벽히 타겟과 맞아떨어 지기 때문) 카운팅이 안되는 경우를 방지하기 위함.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Second Try: Using dictionary to store sums (High performance on both time and space)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.cnt = 0
        sums = defaultdict(int)
        sums[0] = 1
        def dfs(root, cur):
            if not root:
                return
            cur += root.val
            if sums[cur - targetSum] > 0:
                self.cnt += sums[cur - targetSum]
            sums[cur] += 1
            dfs(root.left, cur)
            dfs(root.right, cur)
            sums[cur] -= 1
        dfs(root, 0)
        return self.cnt

# First Try: Using list to store sums (Low performance on memory)
'''
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root, vals):
            if not root:
                return 0
            vals = [root.val + val for val in vals] + [root.val]
            return vals.count(targetSum) + dfs(root.left, vals) + dfs(root.right, vals)
        return dfs(root, [])
'''