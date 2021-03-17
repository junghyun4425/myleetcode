# Problem Link: https://leetcode.com/problems/additive-number/

'''
문제 요약: 숫자로 이뤄진 문자열에서 앞의 두개의 숫자를 더해 뒤의 숫자가 되는지를 확인하는 문제. (한자리수 외에도 여러자리수 가능)
ask: "112358"
answer: True (1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8)

해석:
숫자가 한자리 수라면 간단해지겠지만, 모든 자리수까지 고려해야함.
따라서 재귀함수안에 for문을 통해 모든 부분을 검사 하되, 약간의 가지치기를 적용.
2자리수 이상의 숫자에서 앞의 숫자가 0인경우 continue.
그리고 가장 중요한, 이전의 결과 res[-2] res[-1] 두개를 더한값이 현재 적용하려는 값과 다르면 continue.
이 두가지 방식으로 성능을 조금더 끌어올림.
이 외에는 평범한 재귀함수이며, 한가지 주의할점은 Base case에서 res의 길이가 2이하인 경우는 답이될수 없으니 False를 반환해야함.
'''

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n_len = len(num)
        if n_len <= 2:
            return False
        def recursion(i, res):
            if i == n_len and len(res) > 2:
                return True
            for j in range(i, n_len):
                n = num[i:j + 1]
                if len(n) > 1 and n[0] == '0':
                    continue
                if len(res) > 1 and int(res[-2]) + int(res[-1]) != int(n):
                    continue
                if recursion(j + 1, res + [n]):
                    return True
            return False
        return recursion(0, [])
