# Problem Link: https://leetcode.com/problems/factorial-trailing-zeroes/

'''
문제 요약: 입력으로 들어오는 숫자의 팩토리얼 결과값에 뒤에서부터 0으로 이어지는 최대 개수를 구하는 문제.
ask: 6
answer: 1 (6! = 120, Trailing Zero 의 길이는 1)

해석:
첫 시도는 팩토리얼값을 구해서 그 값의 뒤에서부터 0의 개수를 파악하도록 해결.
하지만 속도가 거의 최악 수준으로 좋지 못함. 따라서 최적화를 위한 어떤 수학 공식이나 패턴이 있다고 판단.
값에 0을 찾는거면 패턴이 없지만, 뒷자리에 연속된 0의 개수는 패턴을 발견함.
팩토리얼이 5의 배수일때 마다 0이 하나씩 증가하는 패턴을 보임. 단, 25의 경우는 5가 두번이라 0이 두개 증가하는 점을 주의.
따라서 패턴을 통해 최적화된 방법으로 해결해서 logarithmic time으로 구현하는데 성공.
'''

# Optimized with pattern: O(logn)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            ans += n // 5
            n //= 5
        return ans

# Not optimized: O(n)
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fac = 1
        for i in range(2, n+1):
            fac *= i
        r = re.search('0*$', str(fac))
        return len(r.group())
'''