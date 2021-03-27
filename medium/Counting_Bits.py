# Problem Link: https://leetcode.com/problems/counting-bits/

'''
문제 요약: 0부터 num까지 비트가 1인 개수를 각각 세는 문제.
ask: num = 5
answer: [0,1,1,2,1,2]

해석:
비트단위기 떄문에 비트연산을 사용해 해결했고, 이전 값이 영향을 주기 떄문에 DP를 활용.
2진수로 나열하다보면 규칙이 보이는데, 2로 나눴을때 1의 비트수와 같다는 점이 특징. (2로 나눔을 쉬프트 연산으로 생각하면 이해가 더 빠름)
단, 홀수일때는 1개가 더 많음.
이 외에도 여러 규칙들이 보이지만 위의 규칙이 구현에 있어서 굉장히 간단하기 떄문에 이를 활용.
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num+1):
            n, odd = i >> 1, i & 1
            ans.append(ans[n] + (1 if odd else 0))
        return ans