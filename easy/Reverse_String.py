# Problem Link: https://leetcode.com/problems/reverse-string/

'''
문제 요약: 문자열이 배열에 담겨져서 들어올때, 추가메모리 사용없이 순서를 뒤집는 문제.
ask: ["h","e","l","l","o"]
answer: ["o","l","l","e","h"]

해석:
추가 메모리는 사용할 수 없기 때문에 l, r 두개의 포인터를 가지고 뒤집어야 함.
l과 r이 서로 바꿔가면서 중간까지 오게되면 뒤집은 것과 같은 결과를 보임.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1