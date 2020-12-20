# Problem Link: https://leetcode.com/problems/divide-two-integers/

'''
문제 요약: 두개의 숫자를 받아 몫을 구하는 문제. (overflow는 2^31 - 1로 반환, 곱셈 나눗셈 mod 사용 불가)
ask: 10, -3
answer: -3

해석:
처음에는 단순히 값을 하나씩 빼주면서 몫을 구했지만 역시나 시간초과.
속도를 exponential 하게 올리기 위해서 가산연산을 추가하기로 결정. 이는 쉬프트연산으로 대체.
처음에는 가장 몫에 근접한 n_divisor를 찾아서 dividend를 빼고 나머지는 그냥 반복문으로 빼줌. 하지만 여기서도 시간초과가 걸림.
이유는 2^32 - 2 가 답이라면, 2^31 부터 반복문을 돌기때문에 쉬프트연산을 안쓸때와 별 다를바 없음.
따라서 n_divisor 또한 쉬프트연산을 반복적으로 해줘서 결국 해결. 생각보다 어려웠던 문제...
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        minus = (dividend < 0) ^ (divisor < 0)

        if dividend < 0:
            dividend = abs(dividend)
        if divisor < 0:
            divisor = abs(divisor)

        quot = 0
        while dividend >= divisor:
            n_divisor, n = divisor, 1
            while (n_divisor << 1) <= dividend:
                n_divisor <<= 1
                n <<= 1

            quot += n
            dividend -= n_divisor

        quot = -quot if minus else quot
        if quot > 2 ** 31 - 1 or quot < -2 ** 31:
            quot = 2 ** 31 - 1

        return quot