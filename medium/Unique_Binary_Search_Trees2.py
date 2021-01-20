# Problem Link: https://leetcode.com/problems/unique-binary-search-trees-ii/

'''
문제 요약: n만큼의 트리 노드가 주어졌을때, 노드로 구성할 수 있는 모든 BST를 반환하는 문제.
ask: 3
answer: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

해석:
이전 문제 Unique_Binary_Search_Trees 에서는 가능한 모든 갯수를 구했다면 이번엔 트리들을 리스트에 담아서 반환하는 방식.
하지만 기본 원리는 똑같기 때문에 root를 x 그 사이 왼쪽을 left 오른쪽을 right라고 잡아서 재귀함수를 수햄.
xooo | oxoo | ooxo | ooox
tree를 자식노드에서부터 하나씩 올라오면서 구성하기 때문에, 재귀함수의 base case는 좌측과 우측이 같아질때 (사이즈가 1) 트리 배열을 반환.
그리고 root를 중심으로 왼쪽과 오른쪽을 붙여야 하는데, 좌측과 우측에 존재하는 모든 경우의 수를 트리로 만들어 반환.
코드는 간단해 보이지만 재귀함수 연습이 부족한 탓인지 오래걸린 문제. 재귀함수 문제를 여럿 풀어보고 숙달해야함...
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def recursion(first, last):
            if first == last:
                return [TreeNode(first)]
            sub_trees = []
            for root in range(first, last+1):
                left, right = root - first, last - root
                left_trees = recursion(first, root-1) if left > 0 else [None]
                right_trees = recursion(root+1, last) if right > 0 else [None]
                sub_trees += [TreeNode(root, l, r) for l in left_trees for r in right_trees]
            return sub_trees
        return recursion(1,n)