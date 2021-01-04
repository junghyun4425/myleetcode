# Problem Link: https://leetcode.com/problems/plus-one/

'''
문제 요약: 숫자 리스트에서 1을 더한 값을 리스트로 반환하는 문제.
ask: [1,2,3]
answer: [1,2,4]

해석:
1의자리 부터 하나를 더한 다음, 10이면 0으로 만들고 다음자리수를 1 더해주는 방식으로 문제를 해결.
맨 앞자리가 9에서 10이 된 경우는, 하나를 추가해줘야하기 때문에 insert(0,1) 으로 처음엔 추가했으나,
속도가 느린것을 확인하고, [1] + digits 와 같이 삽입이 아닌 리스트 추가를 통해 훨씬 나은 속도로 추가함.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            else:
                break
        return digits