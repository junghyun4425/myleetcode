# Problem Link: https://leetcode.com/problems/group-anagrams/

'''
문제 요약: 문자열 리스트에서 같은 char들의 조합으로 이뤄진 문자들을 그룹화 시켜서 반환하는 문제.
ask: ["eat","tea","tan","ate","nat","bat"]
answer: [["bat"],["nat","tan"],["ate","eat","tea"]]

해석:
방금 예시를 아스키코드의 합으로 만들어서 풀어서 테스트 성공했지만, 제출에 오답으로 뜸.
아주 큰 착각을 했던게 아스키코드 값은 문자가 달라도 합이 같은 경우가 있는데 그걸 생각 못함. 고로 다시 짜야함.

-수정-
이번엔 정렬을 사용해서 해결하려함. 문자열을 정렬하고 dictionary에 튜플로 하나씩 비교해가는 방법으로 수행.
원래는 정렬된 리스트로 하려했으나 리스트들의 char를에 비교하기 위해서는 손이 많이가는 편이므로 튜플로 하는것이 좋음.
정렬된 char들을 hashmap의 key로 활용해서 anagram들을 한곳에 묶어놓고 반환할때 value들을 반환.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            t = tuple(sorted(s))
            if not t in hmap:
                hmap[t] = [s]
            else:
                hmap[t].append(s)
        return [s for s in hmap.values()]