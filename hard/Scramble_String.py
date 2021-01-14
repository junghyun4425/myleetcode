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