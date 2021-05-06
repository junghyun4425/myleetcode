# Problem Link: https://leetcode.com/problems/sort-characters-by-frequency/

'''
문제 요약: 단어가 입력으로 들어오면 알파벳의 개수가 많은 철자 순으로 정렬하는 문제.
ask: s = "Aabb"
answer: "bbAa" (대소문자 구분, 같은 개수라면 순서상관없음)

해석:
알파벳 개수를 효율적으로 구하기 위해서 해쉬맵을 활용.
개수를 오름차순으로 정렬하기 위해서 해쉬맵을 배열로 바꿈과 동시에 정렬을 수행.
정렬된 상태로 문자를 개수만큼 찍어주면 O(nlogn)의 시간복잡도로 해결이 가능.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        hm = defaultdict(int)
        for c in s:
            hm[c] += 1
        hm = sorted(hm.items(), key=lambda x: -x[1])
        for c, n in hm:
            ans += c * n
        return ans