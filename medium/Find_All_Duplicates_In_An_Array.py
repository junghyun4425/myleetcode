# Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

'''
문제 요약: 1부터 n(배열의 길이) 까지 숫자가 있다고 할때, 중복되는 값들을 찾는 문제. (Follow up: O(n) time, O(1) space complexity)
ask: nums = [4,3,2,7,8,2,3,1]
answer: [2,3]

해석:
시간 복잡도는 크게 문제되진 않지만 공간복잡도를 상수로 맞춰야 하는게 핵심.
만약 공간복잡도 제한이 없었다면 해쉬맵을 통해 복제된걸 바로 인지할수 있지만, 아닌경우는 배열 안에서 해결해야 함.
크게 두가지 방법을 생각해냄.
1.어차피 n보다 큰 값은 없으니, n보다 큰수를 인덱스에 더해서 mod 연산을 활용해 안에 들어있는 실제 값을 보존함과 동시에 몇번 중복인지 알도록 함.
2.음수가 없기 때문에 abs를 통해 값을 가져오고 그 값을 음수로 바꿔버려서, 2번 반복이면 양수가 되게끔 해서 해결.
두번째의 경우가 코드에서는 좀더 직관적이지만 코드의 길이가 생각보다 길어질거 같아서 1번 방법을 통해 해결해봄.
mod연산을 활용해 2번 만난다면 n+1을 두번 더해주기 때문에 값이 굉장히 커짐.
커지더라도 mod연산 때문에 원래값을 알수있고, 몇번 더해졌는지도 알수있음. (즉, 2번이면 2*(n+1) 보다 커야함)
다음에 복습할때는 2번으로 풀어보기.
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        end = len(nums)
        for i, n in enumerate(nums):
            nums[(n-1) % (end+1)] += end + 1
        return [i+1 for i, n in enumerate(nums) if n > 2*(end+1)]