# Problem Link: https://leetcode.com/problems/group-anagrams/

'''
문제 요약: 문자열 리스트에서 같은 char들의 조합으로 이뤄진 문자들을 그룹화 시켜서 반환하는 문제.
ask: ["eat","tea","tan","ate","nat","bat"]
answer: [["bat"],["nat","tan"],["ate","eat","tea"]]

해석:
방금 예시를 아스키코드의 합으로 만들어서 풀어서 테스트 성공했지만, 제출에 오답으로 뜸.
아주 큰 착각을 했던게 아스키코드 값은 문자가 달라도 합이 같은 경우가 있는데 그걸 생각 못함. 고로 다시 짜야함.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_len = len(strs)
        ans = []
        n_strs = [0] * s_len
        for i, s in enumerate(strs):
            for c in s:
                n_strs[i] += ord(c)

        n_strs = [(n, i) for i, n in enumerate(n_strs)]
        n_strs.sort()

        for i in range(s_len):
            if i > 0 and n_strs[i][0] == n_strs[i - 1][0]:
                ans[-1].append(strs[n_strs[i][1]])
            else:
                ans.append([strs[n_strs[i][1]]])
        return ans