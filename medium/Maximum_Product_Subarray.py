# Problem Link: https://leetcode.com/problems/maximum-product-subarray/

'''
문제 요약: 숫자로 된 배열에서 곱연산으로 최대값을 가지는 subarray의 최대값을 반환하는 문제. (subarray는 연속된 값들의 배열)
ask: [2,3,-2,4]
answer: 6 (subarray = [2,3])

해석:
작은 문제에서 부터 큰문제로 확장해 나가는 Bottum-up 방식의 DP로 풀면 되는 문제.
사실 뺄셈없이 곱셈만 있기 때문에 모든수를 곱하는게 큰수를 찾는 방법이지만, 도중에 음수가 나오면 음수가 짝수일때만 곱해야 함.
하지만 재밌는것은, 음수인 경우라도 곱해서 최소값을 저장하고 있다면 나중에 다시 음수를 마주쳤을때 최대값으로 바꿀수 있다는 점.
그래서 점화식을 세워보면,
dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i]
dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i]
이렇게 ans값을 계속 바꿔나가면 마지막이 정답.

여기서 쓸데없는 메모리 낭비를 방지하기 위해 dp_min[] 배열을 prev_min 으로 변경.
이전값의 정보만 필요하기 때문에 가능한 일.
하지만 주의할 점은, min, max 값이 동시에 바뀌어야 하기 때문에 python에서만 가능한 tuple로 묶어서 unpacking 하는 방법으로 동시에 min, max값을 적용.
(동시에 바뀌어야 하는 이유는 prev_max를 먼저 계산하면 prev_min계산에 문제가 생김. 서로 값을 참조하기 때문.)
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = prev_max = prev_min = nums[0]
        for n in nums[1:]:
            prev_max, prev_min = max(n, prev_max*n, prev_min*n), min(n, prev_max*n, prev_min*n)
            ans = max(ans, prev_max)
        return ans