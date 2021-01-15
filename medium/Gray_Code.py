# Problem Link: https://leetcode.com/problems/gray-code/

'''
문제 요약: n에 대한 그레이 코드를 반환하는 문제.
ask: 2
answer: [0,1,3,2] (00 01 11 10)

해석:
Gray Code를 학부때 배웠기 때문에 어떤식으로 쉽게 구할 수 있는지 알 수 있었던 문제.
비트단위로 생각해 봤을때 그레이 코드는 현재 숫자의 이진수 i와, 이를 한칸 오른쪽으로 쉬프트하고 XOR을 하면 되는 방식.
따라서 굉장히 간단하게 해결.
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [(i>>1)^i for i in range(1<<n)]