# Problem Link: https://leetcode.com/problems/sliding-window-maximum/

'''
문제 요약: 왼쪽부터 한칸씩 움직이는 window size 안에서 최대값을 출력하는 문제.
ask: nums = [1,3,-1,-3,5,3,6,7], k = 3
answer: [3,3,5,5,6,7]

해석:
First Try: Brute Force + DP
우선 간단하게 Brute Force방식에 DP를 대입해 풀어봤지만 시간초과.
O(n*k) 의 시간복잡도를 가져서 k가 크고 worst case인 경우에는 만족할만한 성능이 나오지 않음.
다음으로 개선한 방법을 고민해보면 MaxHeap queue를 활용하는 방법이 떠오름.
값들을 저장해놓고 가장 큰값만 가져오기 때문에 nlogn의 시간복잡도로 해결이 가능.
Max heap queue가 가장 최선의 방법인지 알아봤는데 deque를 쓰면 더 효율적으로 구현이 가능.
Max heap은 여러번 써봤지만 deque를 활용해본적은 없는지라 이쪽으로 풀어보기로 결정.

Second Try: Deque
Maxheap은 무조건 최대값을 가져올수 있다면, deque는 최대값의 index를 가지고 오게 할수도 있기 떄문에 효율적으로 구현이 가능.
새로들어온 값이 max면 가장 왼쪽으로 넣을 수 있도록 함. (while문을 통해서 기존의 값들과 비교해가며 자리를 찾음)
sliding window 안의 index를 벗어날때 벗어난값이 최대값이면 popleft() 로 빼냄.
슬라이딩 윈도우 크기가 k면 이제부터 max값을 ans에 추가함.
구현 자체는 간단해 보이는데 의외로 굉장히 오래걸린 편. (deque의 활용능력이 많이 떨어지는듯)
다음에 리뷰할때도 deque로 다시한번 구현해봐야함.
'''

# Second Try with Deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i, n in enumerate(nums):
            while dq and n > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if dq[0] == i-k:
                dq.popleft()
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans

# First Try (Time Limit Exceeded)
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n_len = len(nums)
        pre_max = max(nums[:k])
        ans = [pre_max]
        for i in range(n_len-k):
            if nums[i] == pre_max:
                pre_max = max(nums[i+1:i+k+1])
            else:
                pre_max = max(pre_max, nums[i+k])
            ans.append(pre_max)
        return ans
'''