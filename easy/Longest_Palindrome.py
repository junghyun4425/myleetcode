# Problem Link: https://leetcode.com/problems/longest-palindrome/

'''
문제 요약: 주어진 문자에서 가장 길게 Palindrome을 만들수 있는 길이를 구하는 문제.
ask: "abccccdd"
answer: 7

해석:
Palindrome 특성상, 짝수개의 같은 문자는 무조건 포함시킬 수 있음.
거기에, 가운데 하나를 추가하면 최대길이가 완성됨. (단, 모든 문자들이 짝수개면 추가시키면 안됨)
따라서 total과 짝수를 구하는 카운팅 해쉬맵 두개를 가지고 최대길이를 찾아가면 끝.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = defaultdict(int)
        ans = 0
        total = 0
        for c in s:
            hm[c] += 1
        for val in hm.values():
            total += val
            ans += (val // 2) * 2
        return ans if total == ans else ans + 1