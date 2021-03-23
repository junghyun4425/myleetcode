# Problem Link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

'''
문제 요약: preorder 순으로 트리를 직렬화한 문자열이 입력으로 주어질때, 정상적인 트리인지 확인하는 문제.
ask: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
answer: True

해석:
여러 방법으로 풀이가 가능하겠지만 가장 심플한 recursion을 활용해 문제를 해결.
DFS탐색으로 좌측먼저 모두 들리고, 다음으로 우측을 탐색함.
이때 노드의 개수를 더하는데 탐색했을떄의 결과와 문자열의 길이가 같다면 올바른 트리고 아니라면 문제가 있음을 의미.
일반 노드를 만나면 다음으로 이동하고, '#'을 만나면 더이상 자식이 없으니 현재 index값을 반환.
'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        p_len = len(preorder)
        def dfs(i):
            if i >= p_len:
                return i
            if preorder[i] == '#':
                return i
            left = dfs(i+1)
            right = dfs(left+1)
            return right
        return True if dfs(0) == p_len-1 else False