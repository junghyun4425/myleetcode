# Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

'''
문제 요약: 전화 다이얼에 적혀있는 알파벳 조합의 모든 경우의 수를 구하는 문제. (2번엔 abc, 3번엔 def ....)
ask: "23"
answer: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

해석:
Dictionary에 다이얼에 적힌 영문을 저장한 후, 이중 for문으로 간단하게 해결이 가능. 처음엔 규칙을 정확하게 몰라서 헤메긴 했음.
경우의 수를 적어보고 그 원리가 이중포문으로 간단하게 해결된다는 것을 알게되어 해결.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        digits_len = len(digits)
        ans = []
        if digits_len == 0:
            return ans
        elif digits_len == 1:
            return hmap[int(digits)]

        pre_d = hmap[int(digits[0])]
        for i in range(1, digits_len):
            ans = hmap[int(digits[i])]
            ans = [a + b for a in pre_d for b in ans]
            pre_d = ans

        return ans