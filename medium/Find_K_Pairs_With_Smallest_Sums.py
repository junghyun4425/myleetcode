# Problem Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

'''
문제 요약: 두개의 배열의 최소값이 되는 조합 k쌍을 반환하는 문제.
ask: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
answer: [[1,2],[1,4],[1,6]]

해석:
최소값을 찾기위해 heapq를 사용하면 쉽게 해결이 가능한 문제.
힙에 n1 + n2 값으로 정렬되게 하면 작은값부터 가져올수 있게 됨.
따라서 모든 조합을 저장하고 k개만큼 빼거나 k보다 힙에 들어있는 값이 작으면 반대로 힙의 사이즈만큼만 빼면 끝.
k개까지만 계산해서 반환하도록 최적화할수도 있을것 같기도 함. 따라서 다음 복습때 최적화 해보는 것으로.
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        for n1 in nums1:
            for n2 in nums2:
                heappush(hq, [n1+n2, n1, n2])
        return [heappop(hq)[1:] for _ in range(min(k, len(hq)))]