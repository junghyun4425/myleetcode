# Problem Link: https://leetcode.com/problems/increasing-triplet-subsequence/

'''
문제 요약: i < j < k 에서 nums[i] < nums[j] < nums[k] 를 만족하는지 확인하는 문제.
ask: [1,2,3,4,5]
answer: True

해석:
First Try
약간 어렵게 접근한 방법으로, 재귀함수를 호출해 해결해보려 했음.
숫자를 하나씩 진행해나가면서 이전값보다 큰값이 나타나면 계속 진행, 작은값이면 이전결과를 버리는경우와 현재값을 무시하는 경우 둘다 재귀호출.
정확성 테스트에는 문제없으나 성능쪽에서 Time Limit Exceeded 결과를 확인함.

Second Try
보통 이런 문제는 쉽게 접근해야 해결이 가능해서 단순히 생각해봄.
그냥 변수 두개를 가지고 서로 비교해가면서 v1 < v2 < nums[i] 를 만들수 있지 않을까 고민.
1. 만약 값이 v1보다 nums[i]가 작다면 v1 = nums[i]
2. v1 < nums[i] < v2 면 v2 = nums[i]
3. v1 < v2 < nums[i] 면 True를 리턴.

위의 공식이 정답과 달라도 정답을 찾는데 문제가 없음을 증명할 수 있음.
우선 정답과 다른경우는 [1,5,0,6,2] 를 예로들게 됨.
정답은 1 < 5 < 6 이지만, 위의 알고리즘대로 하면 0 < 5 < 6 으로 잘못된 결과를 받아볼 수 있음.
하지만 이게 실제 오답에 영향을 주지 않음.
이유는 0이 뒤의 자리에 위치하지만 어차피 그전에 어떤값이 5 혹은 6 (v2 or nums[i]) 보다 작은게 들어갔다는걸 알수있음.
왜냐면 위의 알고리즘의 조건절 순서 때문에 v1은 v2 or nums[i]보다 큰값을 항상 가질수 없기때문.
따라서 실제로는 0이 들어왔지만 1이란 값을 내포하고 있게 되므로 오답이 아니라 정답의 결과를 받아볼 수 있음.
'''

# Second Try with simple algorithm
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float('inf')
        for n in nums:
            if n < min1:
                min1 = n
            elif min1 < n < min2:
                min2 = n
            elif min1 < min2 < n:
                return True
        return False

# First Try with BFS (Time Limit Exceeded)
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n_len = len(nums)
        def bfs(prev, cnt, i):
            if i == n_len:
                return False
            if cnt == 3:
                return True
            res = False
            if prev < nums[i]:
                res = bfs(nums[i], cnt+1, i+1)
            else:
                res = any([bfs(nums[i], cnt, i+1), bfs(prev, cnt, i+1)])
            return res
        return bfs(nums[0], 1, 1)
'''