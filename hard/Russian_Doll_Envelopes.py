# Problem Link: https://leetcode.com/problems/russian-doll-envelopes/

'''
문제 요약: 작은 사이즈부터 최대한의 포장이 가능한 개수를 구하는 문제. (높이, 너비 둘다 커야만 감쌀수 있음)
ask: envelopes = [[5,4],[6,4],[6,7],[2,3]]
answer: 3 ( [2,3] -> [5,4] -> [6,7] )

해석:
가장 먼저 해결했던 방법이 DP를 활용하는 것.
넓이와 높이에 대해 각각 정렬시킨 다음, 모든 포장에 대해 각각 가능한 경우의 수를 더해가며 최대값을 찾으면 쉽게 해결이 가능.
문제는 O(n^2) 시간복잡도를 가지는데, 이는 시간초과가 됨. 따라서 다른 방법을 생각해야함.
넓이와 높이에대해 정렬을 수행하게된다면 넓이에 대해서는 비교를 굳이 할필요가 없음.
다만, 넓이가 같을때 높이가 다른경우는 문제가됨. ([3,5], [3,7] 이 경우 3,5 혹은 3,7 둘중 하나만 포함되어야 하기 때문)
따라서 두번째 높이에 대해서는 역순으로 정렬해 중복으로 들어가는걸 막는 방법을 선택.
이제 높이에 대해서만 Longest Increasing Search 알고리즘을 통해 가장 긴 증가하는값을 찾음.
이때 LIS를 바이너리 서치로 탐색하는게 효율적.
결론은, 작은값에서부터 순차적으로 정답을 기록하되, 최고값보다 작은값이 들어왔다면 추가하지않고 ans에 보다 큰값 하나와 교체해줌.
'''

class Solution:
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                pos = m
                r = m - 1
        return pos

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        ans = [envelopes[0][1]]
        for _, h in envelopes[1:]:
            if h > ans[-1]:
                ans.append(h)
            else:
                pos = self.binarySearch(ans, h)
                ans[pos] = h
        return len(ans)