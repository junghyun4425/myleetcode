# Problem Link: https://leetcode.com/problems/balanced-binary-tree/

'''
문제 요약: 트리가 들어오면 height-balanced 트리인지 확인하는 문제. (자식들의 depth 차이가 2이상이면 False)
ask: [3,9,20,null,null,15,7]
answer: True

해석:
두가지 방법으로 풀 수 있는 문제. queue를 이용해 BFS 방식으로 node의 자식이 왼쪽 오른쪽 둘다 None일때 depth를 저장하는 방법.
다른 하나는 재귀함수를 통해 차이를 구하는 방법.
BFS방식으로 푸는게 성능면에서 빠를거라 생각되지만 재귀함수방식의 코드구상이 잘 안떠올라 연습겸 재귀함수로 풀어봄.
depth() 함수는 말 그대로 트리든, 서브트리든 depth의 max값을 구하는 함수.
실제 차이를 구하기 위해 왼쪽의 서브트리, 오른쪽의 서브트리에 대한 depth를 각각 구해서 차이를 구하면 끝.
만약 차이가 2이상이면 False를 반환, 그외엔 True를 반환해서 마지막까지 한번의 False라도 존재하면 Balanced Tree가 아님을 최종적으로 반환.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 1
            return 1 + max(depth(root.left), depth(root.right))

        def searching(root):
            if not root:
                return True
            if abs(depth(root.left) - depth(root.right)) > 1:
                return False
            return searching(root.left) and searching(root.right)

        return searching(root)