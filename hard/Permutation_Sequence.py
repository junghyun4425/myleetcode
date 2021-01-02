# Problem Link: https://leetcode.com/problems/permutation-sequence/

'''
문제 요약: n크기 순열의 k번째 숫자조합을 반환하는 문제.
ask: n = 3, k = 3
answer: "213"

해석:
지난번에 풀었던 next_permutation 코드를 활용해 풀었지만 속도는 거의 최악 수준의 결과.
따라서 뭔가 수학적 알고리즘이 있다고 판단하여 다시생각.
우선, 1xxx 가 끝나면 2xxx. 다음은 3xxx 4xxx 순으로 생성되는것을 확인.
뒷자리 xxx의 경우의수는 남은갯수의 팩토리얼로 구성되는걸 알기 때문에 k번째에 1로 시작하는지 아니면 2,3,4로 시작하는지 확인이 가능.
이를 반복적으로 수행해서 n이 0보다 클때까지 수행하게되면 모든 x번째 자리수까지 k번째의 순열을 구할 수 있음.
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            s = 1
            for i in range(1, n + 1):
                s *= i
            return s

        ns = list(range(1, n + 1))
        ans = ''
        while n > 0:
            n_fac = factorial(n - 1)
            i = k // n_fac
            if k % n_fac == 0:
                i -= 1
            k %= n_fac
            n -= 1
            ans += str(ns[i])
            del(ns[i])
        return ans