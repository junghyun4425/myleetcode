# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

'''
문제 요약: 두개의 배열에 intersection을 구하는 문제. (단, 중복된 숫자도 포함시켜야 함)
ask: nums1 = [1,2,2,1], nums2 = [2,2]
answer: [2,2]

해석:
간단한 해결법으로 두가지 방법이 떠오름.
1.두 배열을 정렬해서 i, j 포인터 두개로 중복된 값을 찾기. ( time: O(nlogn), space: O(1) )
2.해쉬맵을 통해 카운팅해서 중복되는걸 찾는 방법. ( time: O(n), space: O(n) )
여기서는 해쉬맵을 통해 문제를 풀기로 결정.
nums1 에 대한 카운팅을 완료하고, nums2 를 통해 해쉬맵에 있는지 여부를 판단함.
있다면 ans에 넣고 카운트를 하나 줄이는 방식으로 해결.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = defaultdict(int)
        ans = []
        for n in nums1:
            hm[n] += 1
        for n in nums2:
            if n in hm and hm[n] > 0:
                ans.append(n)
                hm[n] -= 1
        return ans