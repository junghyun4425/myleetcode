# Problem Link: https://leetcode.com/problems/spiral-matrix-ii/

'''
문제 요약: 입력으로 들어온 숫자만큼의 정사각형 사이즈 리스트를 나선형 순서로 1 ~ n^2 까지 채워넣어 반환하는 문제.
ask: n = 3
answer: [[1,2,3],[8,9,4],[7,6,5]]

해석:
Spiral Matrix 첫번째 문제는 바운더리를 하나씩 증가시키면서 결과값을 생성.
이번엔 바운더리방식 말고 맵을 탐색하는 방식으로 수행.
di이 나선형 순서를 가짐으로써 (di + 1 % 4) 를 순서대로 수행하면 나선형으로 진행.
조건문으로 다음 진행될 방향이 옳은지 틀린지(사이즈 넘어가거나 0이 아닌 탐색된 곳으로 가거나) 판단해서 수행.
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        di = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d, r, c, i = 0, 0, 0, 1

        while i <= n * n:
            ans[r][c] = i
            i += 1

            r2, c2 = r + di[d][0], c + di[d][1]
            if r2 < 0 or r2 >= n or c2 < 0 or c2 >= n or ans[r2][c2] != 0:
                d = (d + 1) % 4

            r += di[d][0]
            c += di[d][1]
        return ans