# Problem Link: https://leetcode.com/problems/remove-k-digits/

'''
문제 요약: k개의 숫자를 제거해서 가장 작은 숫자로 만드는 문제.
ask: num = "1432219", k = 3
answer: "1219"

해석:
Brute Force로 풀기엔 굉장히 비효율적이기 때문에 시도하진 않고 바로 최적화 방법을 찾아봄.
문제를 보면 숫자가 증가하고있을때는 제거하는게 비효율적이지만 감소할때 이전값을 제거해서 높은자리수가 더 작은값을 가지게끔 해줘야 함.
따라서 문자열을 왼쪽에서 부터 k개를 제거해가며 오름차순으로 만들면 해결됨.
stack을 활용해 k개 만큼만 오름차순임을 보장하여 구현함.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            if stack or n != '0':
                stack.append(n)
        while stack and k > 0:
            k -= 1
            stack.pop()
        if not stack:
            return '0'
        return "".join(stack)