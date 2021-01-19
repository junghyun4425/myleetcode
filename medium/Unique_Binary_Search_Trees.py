# Problem Link: https://leetcode.com/problems/unique-binary-search-trees/

'''
문제 요약: n만큼의 트리 노드가 주어졌을때, 노드로 구성할 수 있는 BST의 갯수를 반환하는 문제. (Binary Search Tree)
ask: 3
answer: 5 (5가지 만들 수 있음)

해석:
재귀함수로 왼쪽, 오른쪽, 양쪽 탐색해서 갯수를 구할 수 있지만 일정 노드의 수를 넘어가면 시간이 초과됨.
따라서 불필요한 계산을 줄이기 위해 DP방식을 적용.
노드가 4개인것을 oooo 라 표현하고 root를 x라 표현하면 경우의 수는
xooo | oxoo | ooxo | ooox
가 있으며, x를 기준으로 왼쪽이 될수 있는 트리의 수와 오른쪽이 될 수 있는 트리의 수를 곱하면 모든 경우의 수가 됨. 위의 경우를 식으로 표현하면 순서대로,
n_tree[0] * n_tree[3] | n_tree[1] * n_tree[2] | n_tree[2] * n_tree[1] | n_tree[3] * n_tree[0]
n_tree[0] 과 n_tree[1] 은 여럿 만들 수 없고 다른쪽 경우의수에 따라 결정되므로 1이 되어야 하고, 나머지는 이전의 계산값을 참고하면 빠르게 해결이 가능.
'''

class Solution:
    def numTrees(self, n: int) -> int:
        n_tree = [0] * (n + 1)
        n_tree[0] = n_tree[1] = 1

        for n_node in range(2, n + 1):
            for root in range(1, n_node + 1):
                n_tree[n_node] += n_tree[root - 1] * n_tree[n_node - root]
        return n_tree[-1]