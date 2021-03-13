# Problem Link: https://leetcode.com/problems/summary-ranges/

'''
문제 요약: 정렬된 배열에서 숫자가 1씩 증가하는 range들을 모아서 출력해주는 문제.
ask: [0,1,2,4,5,7]
answer: ["0->2","4->5","7"]

해석:
이전값에서 1보다 더 큰 값들의 경우는 range가 다르기 때문에 따로 배열에 저장하도록 함.
nums마지막에 무한대의 숫자를 뒤에 붙였는데 이유는 nums의 마지막값을 결과에 넣기위해 하나 가짜로 값을 넣은것.
1씩 증가하는 경우만 range를 묶어서 문자열로 정리해주면 문제가 쉽게 해결됨.
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n_len = len(nums)
        nums.append(float('inf'))
        start = nums[0]
        points = []
        ans = []
        for i in range(n_len):
            if nums[i]+1 != nums[i+1]:
                points.append([start, nums[i]])
                start = nums[i+1]
        for s, e in points:
            if s == e:
                ans.append(str(s))
            else:
                ans.append(f'{s}->{e}')
        return ans