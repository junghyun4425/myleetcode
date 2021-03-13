# Problem Link: https://leetcode.com/problems/contains-duplicate-iii/

'''
문제 요약: 배열에서 abs(i - j) <= k 와 abs(nums[i] - nums[j]) <= t 를 만족하는 값이 있는지 확인하는 문제.
ask: nums = [1,2,3,1], k = 3, t = 0
answer: true

해석:
미디엄 치고는 굉장히 어려웠던 문제. 아마 Bucket이라는 개념이 생소해서 이해하는데 오래걸려서 어려웠던것 같음.
처음에는 역시나 for loop 를 두번 돌면서 모든 경우의수를 찾아봤지만 제한시간 초과.
어떤 자료구조를 써볼까 생각을 해봐도 마땅히 답이 떠오르지 않음. 위치도 중요하기 떄문에 정렬을 하려면 index포함해서 해야하는데 번거로운편.
이래저래 시도해보다가 결국 다른 사람의 풀이를 보게됐는데, 복잡해보이지만 복잡하지 않은 구조.
hashmap + bucket + sliding window 세가지 방식을 모두 적용한 문제임.

풀이를 하자면,
bucket에 담을 수 있는 값은 t안에 들어가있는값이어야 함. 따라서 t보다 작으면 0에 담길것이고, t보다 크면 1, t보다 2배크면 2 ...
정리하면 bucket = {0: 0 ~ t, 1: t ~ 2t-1, 2: 2t ~ 3t -1 .... }
만약 i값이 k보다 커지면 그때부터는 버켓을 하나씩 줄여나가야 함. 고로 이전에 담았던 k보다 작은범위의 값 i-k-1 // (t+1) 을 버켓에서 제거.
이때 하나의 값만 지우는게 아니라 bucket의 키값 자체를 제거해버려도 되는데, 왜냐면 안에 여럿이 있을수 없기 떄문. 여럿이 있기 전에 True를 반환하고 종료됨.
검사할때 bucket_id+1, bucket_id-1 도 함께하는 이유는 bucket_id의 끝자리 수와 bucket_id+1의 처음자리 수를 빼면 t를 만족하는 경우가 있기 때문.
따라서 이 모든 경우를 다 판단해서 True를 반환해주고 아무것도 없다면 False를 반환.

Bucket의 개념을 이 문제를 통해 확실히 깨우침. 나중에 범위별로 작업을 해야하는 경우 고려해볼법한 좋은 아이디어.
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for i in range(len(nums)):
            if i > k:
                del bucket[nums[i-k-1]//(t+1)]
            bucket_id = nums[i] // (t+1)
            cond1 = bucket_id in bucket
            cond2 = bucket_id+1 in bucket and abs(nums[i]-bucket[bucket_id+1]) <= t
            cond3 = bucket_id-1 in bucket and abs(nums[i]-bucket[bucket_id-1]) <= t
            if cond1 or cond2 or cond3:
                return True
            bucket[bucket_id] = nums[i]
        return False