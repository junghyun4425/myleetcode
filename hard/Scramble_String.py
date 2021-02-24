# Problem Link: https://leetcode.com/problems/scramble-string/

'''
문제 요약: 같은길이 문자열 s1, s2 에서 s1을 랜덤 위치에서 나누고 스왑한 결과가 s2가 될수있다면 True를 반환하는 문제.
ask: s1 = "great", s2 = "rgeat"
answer: True (gr/eat -> r/g / eat)

해석:
재귀함수로 i사이를 잘라서 스왑했을때 혹은 안했을때 둘중 하나라도 같은 문자라면 True를 반환.
더이상 자를수 없을때까지 반복하고, 최종적으로 True을 반환하지 못하면 False반환하고 끝.
하지만 예상대로 시간제한을 초과해 버렸기에, 뭔가 다른방법이 있는지 생각해봤지만 떠오르지 않음.

결국 어떤식으로 풀었나 확인해봤는데 정렬을 통해 문자열이 같은지(비교할 가치가 있는지)를 앞서 판단해주면 뒤에 불필요한 재귀함수 호출을 모두 줄여줌.
처음엔 정렬에 필요한 시간복잡도 nlogn 만큼 느려지는거라 매번 재귀함수 때 마다 수행하면 역효과가 나지 않을까 생각도 함.
하지만 예시를 들어 생각해 보면, great rgeat를 1번째에서 나눴을때, g / reat 와 r / geat 의 경우 정렬의 결과가 False -> 나머지 불필요한 재귀함수 호출 x
생각보다 많은 계산을 줄여줌. 재귀를 상당히 줄여줄수만 있다면 정렬과같은 알고리즘이 득이된다는 점을 깨달음...

Review
DP관련된 문제로 분류되어 있어서 DP방식으로 문제를 해결해봄.
우선, Top-down 방식이기에 작은 크기의 s1, s2 부터 False인지 True인지를 저장. Key = (s1, s2) 튜플. Value = boolean값.
따라서 재귀식들을 트리구조로 나열해보면 아래로 내려갈때 중복계산이 존재하니, 이런 경우 DP에 저장된 값을 바로 반환해줌.
여기서 재밌는 결과가 나오는데,
1. DP를 쓰지않은 평범한 재귀함수에서는 Time Limited.
2. DP를 썼을때는 200ms 이상.
3. 여기에 sorting 알고리즘을 추가하면 40ms
4. DP없이 sorting 알고리즘만 수행하면 40ms
즉, DP를 쓰든 안쓰든 sorting 알고리즘이 핵심이었던 문제. DP로 풀어도 통과가 되긴하나 최적화가 필요한 문제.
'''

# Second Try: Added DP with sorting algorithm
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}
        def recursion(s1, s2):
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            if (s1, s2) in dp:
                return dp[(s1, s2)]
            dp[(s1, s2)] = False
            for i in range(1, len(s1)):
                if (recursion(s1[:i], s2[:i]) and recursion(s1[i:], s2[i:])) or (recursion(s1[i:], s2[:-i]) and recursion(s1[:i], s2[-i:])):
                    dp[(s1, s2)] = True
                    return True
            return dp[(s1, s2)]
        return recursion(s1, s2)

# First Try: No DP, but sorting algorithm
'''
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def recursive(s1, s2):
            s_len = len(s1)
            if s_len == 1:
                return s1 == s2
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1, s_len):
                if (recursive(s1[:i], s2[:i]) and recursive(s1[i:], s2[i:])) or (recursive(s1[i:], s2[:-i]) and recursive(s1[:i], s2[-i:])):
                    return True
            return False
        return recursive(s1, s2)
'''