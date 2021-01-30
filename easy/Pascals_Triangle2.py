# Problem Link: https://leetcode.com/problems/pascals-triangle/

'''
문제 요약: 입력으로 들어오는 높이의 파스칼삼각형 배열을 반환하는 문제. (공간 복잡도 O(k) 를 만족시키기)
ask: 5
answer: [1,4,6,4,1]

해석:
2차원 배열로 한줄씩 업데이트 하는 방식으로 시도. 공간복잡도는 O(2k) 이기에 조건을 만족.
한줄을 파스칼삼각형으로 바꾸고 다른줄에 다음 레벨의 파스칼삼각형으로 바꾸는걸 반복.
논리적으로 오류가 전혀없음에도 자꾸 오답이 나왔는데, 얕은카피를 한줄도 모르고 시간을 보내다 뒤늦게 깨달음...
딥카피를 하기위해 배열 뒤에 슬라이싱을 붙여서 해결.
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1] * (rowIndex+1) for _ in range(2)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                ans[1][j] = ans[0][j] + ans[0][j-1]
            ans[0] = ans[1][:]
        return ans[1]