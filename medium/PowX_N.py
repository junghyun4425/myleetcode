# Problem Link: https://leetcode.com/problems/powx-n/

'''
문제 요약: 제곱의 결과를 반환하는 문제. (따로 조건은 없으나 속도제한으로 O(logn))
ask: x = 2.10000 n = 3
answer: 9.26100

해석: 쉽게 푼 방법으로는 역시나 O(n) 시간복잡도를 생각해 볼 수 있는데, 역시나 시간초과로 실패.
그렇다는 말은 O(logn)까지 속도를 줄여야 함. 좀 더 고민해봐야함.

-수정-
보통 O(n)을 O(logn)으로 성능향상 시키려면 반씩 나눠서 뭔가를 할수 있는 규칙을 찾으면 됨.
제곱의 규칙을 자세히 살펴보면, x^8 = x^4 * x^2 * x^1 * x^0 으로 나눌수 있는것을 알수있음.
홀수의 경우엔, x^10 = x^5 * x^2 * x^1 * x^0 으로, 이전의 x값에 x를 한번 더 곱해주면 됨.
따라서 재쉬함수를 통해 뒤에서 부터 (x^0) 쭉 곱해오면 O(logn)의 속도로 완성시킬 수 있음.
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        minus = False
        if n < 0:
            n = abs(n)
            minus = True

        def div_pow(x, n):
            if n == 0:
                return 1
            pre_x = div_pow(x, n // 2)
            if n % 2 == 0:
                return pre_x * pre_x
            else:
                return x * (pre_x * pre_x)

        ans = div_pow(x, n)
        return ans if not minus else 1 / ans