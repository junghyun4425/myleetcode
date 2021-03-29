# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/

'''
문제 요약: 가장 많이 반복되어 나온 숫자들을 k번째 까지 찾아내는 문제.
ask: nums = [1,1,1,2,2,3], k = 2
answer: [1,2] (가장 많은 빈도수 2개를 찾아보면 1과 2가 정답)

해석:
해쉬맵을 사용해 풀면 간단하게 해결이 가능.
해쉬맵으로 카운팅하고, 카운팅을 기준으로 정렬을 수행. (O(nlogn))
카운팅으로 정렬되었기 때문에 그 키값이 실제 최다중복의 숫자이므로 이를 출력해주면 끝.
공간복잡도 최상위 시간복잡도 상위를 차지함.
따라서 어떤 방법으로 공간복잡도를 낮추고 시간복잡도를 O(n)으로 해결하는 방법이 있을거라 예상.
다음에 복습하게된다면 다른방법으로 풀어보는 것으로.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        ans = sorted([(val,key) for key, val in hm.items()], key=lambda x: -x[0])
        return [k for v, k in ans[:k]]