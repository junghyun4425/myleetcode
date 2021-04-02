# Problem Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

'''
문제 요약: 가로와 세로에 대해 정렬된 2D Matrix가 입력으로 들어올때 k번째 큰 숫자를 찾는 문제.
ask: matrix = [
[1,5,9],
[10,11,13],
[12,13,15]
], k = 8
answer: 13

해석:
여러방법이 있겠지만 선택한 방법은 heapq를 활용하는 것.
단, heapq를 2차원 배열에대해서 사용하면 굉장히 효율이 떨어지게 됨. O(n^2logn)
하지만 heapq를 각 행에대해서 대표로 하나만 저장하는 방식으로 해결하면 O(nlogn) 수행이 가능함.
이를 위해 heap에 (matrix[i][0], i, 0) 과 같은 튜플로 저장하는 방식.
heap에서 어떤 값을 빼내게되면 j값을 1증가시켜 다시 저장하게 되어 정렬된 숫자로 빼내게끔 함.
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h, w = len(matrix), len(matrix[0])
        hq = []
        ans = 0
        for i in range(h):
            heappush(hq, (matrix[i][0], i, 0))
        while k > 0:
            ans, i, j = heappop(hq)
            if j+1 < w:
                heappush(hq, (matrix[i][j+1], i, j+1))
            k -= 1
        return ans