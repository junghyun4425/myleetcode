# Problem Link: https://leetcode.com/problems/reconstruct-original-digits-from-english/

'''
문제 요약: 숫자의 철자들이 랜덤한 순서로 있을때, digit숫자로 바꿔서 오름차순으로 정렬해 반환하는 문제.
ask: s = "owoztneoer"
answer: "012"

해석:
처음 문제를 접했을때는 단순히 해쉬맵안에 키를 set으로 나열해놓고 값을 digit으로 해서 해결하려 함.
이럴경우 중복되는 철자 때문에 판별이 어려워 지지만, 여기서 알수 있었던 것은 z나 u는 특정 숫자에만 있는 철자라는걸 깨닫게 됨.
즉, z는 zero에만 있으니 이 철자를 먼저 다 제거해주고, u는 four에만 있으니 또 제거.
이런식으로 우선순위를 두고 제거해 나가면 굉장히 쉽게 해결이 됨.
f는 four에도 있고 five에도 있지만, four를 'u'로 모두 제거하기 떄문에 남은 f는 모두 five가 되므로 이런식의 순서를 정해야 함.
이렇게 모든 숫자들을 찾아내고 정렬해서 digit으로 출력만 해주면 끝.
'''

class Solution:
    def originalDigits(self, s: str) -> str:
        cnts = Counter(s)
        num_char = {'z': ('zero', '0'), 'w': ('two', '2'), 'u': ('four', '4'), 'x': ('six', '6'), 'f': ('five', '5'), 'r': ('three', '3'), 't': ('eight', '8'), 's': ('seven', '7'), 'i': ('nine', '9'), 'n': ('one', '1')}
        ans = []
        for key, (word, digit) in num_char.items():
            digit_cnt = cnts[key]
            ans.append(digit * digit_cnt)
            for c in word: cnts[c] -= digit_cnt
        return ''.join(sorted(ans))