# Problem Link: https://leetcode.com/problems/integer-to-english-words/

'''
문제 요약: 숫자를 영어로 표현하는 문제.
ask: 1234567891
answer: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

해석:
Dictionary에 필요한 문장들을 쓰고 1000 단위씩 끊어서 하면 금방 해결될 줄 알았는데 생각지 못한 몇가지 예외떄문에 시간이 오래걸림.
1.0 일때 "Zero" 를 반환
2.1000 일때 One thousand 뒤에 공백이 하나 붙음 (로직에서 공백 처리를 해줬다고 생각했는데, 생각지 못한 공백이 더 붙음)
3.1000000 일때 One million 뒤에 thousand가 붙음 (세라지 수를 묶은게 0인 경우를 깜빡함)
1,3번은 간단하게 해결했으나, 2번의 경우 조금 까다로웠음. join을 두번해서 결과를 내는데 중간에 빈공백을 제거하려면 코드가 지저분해지기 떄문.
따라서 여러 배열들을 flatten 처리하고 join을 해주기로 결정.
굉장히 재밌는 사실은 flatten을 sum() 함수로 굉장히 쉽게 할수 있다는 점. 두번째 인자에 빈 리스트를 넣으면 리스트 덧셈 연산이 되어서 flatMap 효과가 남.
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']
        ans = []
        while num > 0:
            queue = []
            block = num % 1000
            if block > 99:
                queue.extend([ones[block//100], 'Hundred'])
                block %= 100
            if block > 19:
                queue.append(tens[block//10])
                block %= 10
            if block:
                queue.append(ones[block])
            if queue and len(ans):
                queue.append(thousands[len(ans)])
            ans.append(queue)
            num //= 1000
        return ' '.join(sum(reversed(ans), []))