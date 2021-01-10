# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

'''
문제 요약: 정렬된 정수 리스트를 중복된값이 2개 이하로 만드는 문제. (단, space comp O(1)로 해결)
ask: [1,1,1,2,2,3]
answer: [1,1,2,2,3]

해석:
포인터 두개를 사용해 O(1)의 공간 복잡도를 만족.
2칸씩 비교해야 하기 때문에 리스트 길이가 2이하인 경우는 바로 리턴해서 넘겨줌.
ans는 중복된 경우 더하지 않으면서 자리를 유지하고 i값은 꾸준히 증가시킴.
중복된 수가 많을수록 ans와 i간 갭이 커지며, ans 보다 높은 index들의 숫자는 버려도 되는 숫자. (메모리 따로 사용하지 않기위해 중복숫자는 덮어씌우는 전략)
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_len = len(nums)
        ans = 2
        if n_len < 3:
            return n_len
        for i in range(2, len(nums)):
            if nums[i] != nums[ans-2]:
                nums[ans] = nums[i]
                ans += 1
        return ans