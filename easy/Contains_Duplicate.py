# Problem Link: https://leetcode.com/problems/contains-duplicate/

'''
문제 요약: 배열에 중복된 값이 있는지 없는지 확인하는 문제.
ask: nums = [1,1,1,3,3,4,3,2,4,2]
answer: True

해석:
대충 세가지 방법으로 풀수 있음.
1.정렬 후 같은값이 있는지 확인하는 방법
2.hashmap을 통해 중복된 값이 있는지
3.set을 활용해 배열에 중복이 있는지
가장 효율적인 set을 활용해 빠른속도로 문제를 해결함.
set하면 중복값이 사라지므로 길이를 비교해보면 중복이 있는지 없는지 알아볼 수 있음.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) - len(set(nums)) > 0