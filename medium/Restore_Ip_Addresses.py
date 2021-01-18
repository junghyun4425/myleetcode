# Problem Link: https://leetcode.com/problems/restore-ip-addresses/

'''
문제 요약: dot이 빠진 IP Address 가 문자열로 주어질때, 유효한 IP주소를 모두 반환하는 문제.
ask: "25525511135"
answer: ["255.255.11.135","255.255.111.35"]

해석:
재귀함수를 통해 1,2,3 자리 수 만큼 끊어서 호출하는 방식으로 해결.
0 ~ 255 를 만족하는지 확인하기 위한 if문을 여럿 만들기 보다는 set에 모든값을 저장해 비교.
이는 메모리를 어느정도 소비해서, "022" 와같은 숫자를 "22" 와 다르다고 표현하기에 재귀함수 내 if문을 여럿 안붙여도 되는 장점이 있음.
cur 이라는 리스트에 유효한 숫자들을 모아두고 4개가 된다면 '.'으로 합쳐서 ans에 추가시킴.
여기서 dots 이 3일때 rest의 길이가 3보다 길다면 유효할 수 없기에 바로 리턴함. (이 한줄 때문에 전체 속도가 2배 가량 상승)
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        all_case = set([str(i) for i in range(256)])
        def recursion(cur, rest, dots):
            if dots == 4:
                if not rest:
                    ans.append(".".join(cur))
                return
            l = len(rest)
            for i in range(1, 4):
                if dots == 3 and l > 3: return
                if l >= i and rest[:i] in all_case:
                    recursion(cur+[rest[:i]],rest[i:],dots+1)
        recursion([], s, 0)
        return ans