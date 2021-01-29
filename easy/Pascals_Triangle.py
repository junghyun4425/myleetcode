# Problem Link: https://leetcode.com/problems/pascals-triangle/

'''
문제 요약: 숫자만큼의 높이를 가지는 파스칼삼각형을 배열 형태로 반환하는 문제.
ask: 5
answer: [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

해석:
편법없이 단순하게 이중 for loop를 통해 수행.
처음부터 [[1]*i for i in range(1, numRows+1)] 과 같은 리스트 컴프레헨션을 사용하면 더 간단하게 해결이 가능함.
그러면 append()함수 호출 없이 값만 바꾸면 끝.
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            new_line = [1]
            for j in range(1, i):
                new_line.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(new_line+[1])
        return ans