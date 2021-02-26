# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

'''
문제 요약: 주어진 문자열 내에서 중복 문자가 없는 최대길이의 문자열 찾기.
ask: "abcabcbb"
answer: 3

해석:
바로 떠오른 방법인 모든 경우의 수를 다 탐색하는 방법으로 풀어냈지만 속도면에서 굉장히 안좋음.
중복 문자를 찾을때까지 무한히 반복해서 찾았지만, 동적알고리즘을 통해 최적화가 가능함.
i와 j를 window slice방식으로 적용하면 하나의 반복문 만으로 결과을 구할 수 있음.
값 j를 움직이면서 중복된 값을 발견하면 i를 중복된 index + 1로 바꿔주기만 하면 간단하게 해결.

Review
이전과 같은 방법으로 풀었지만 한군데 막힌 부분이 존재.
왼쪽을 의미하는 값을 수정할때 max() 함수를 쓴점.
그 이유는 왼쪽의 값쪽 l이 예전에 만난 값을 중복해서 만나면 거기에 있는 index에 1을 더하기 때문에, 오히려 l의 인덱스가 줄어듬.
이런 현상을 방지하고자, l이 줄어들지 않게하기 위해 max()함수로 index를 설정함.
그 외에는 크게 어렵지 않았던 문제.
'''

# Reviewing
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = l = 0
        hm = {}
        for r in range(len(s)):
            if s[r] in hm:
                l = max(l, hm[s[r]]+1)
            hm[s[r]] = r
            max_len = max(max_len, r-l+1)
        return max_len

# First Try: Failed (Time Limit)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = len(s)
        if max_len == 0:
            return 0

        longest = 1
        for i in range(max_len):
            hmap = {}
            hmap[s[i]] = True
            for j in range(i + 1, max_len):
                if s[j] in hmap:
                    break
                else:
                    hmap[s[j]] = True
                    if longest < (j - i + 1):
                        longest = j - i + 1
        return longest
'''

# Optimized version
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = len(s)
        ans, i = 0, 0
        hmap = {}

        for j in range(max_len):
            if s[j] in hmap:
                i = max(hmap[s[j]] + 1, i)
            hmap[s[j]] = j
            ans = max(j - i + 1, ans)

        return ans
'''