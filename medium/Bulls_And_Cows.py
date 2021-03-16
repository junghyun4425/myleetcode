# Problem Link: https://leetcode.com/problems/bulls-and-cows/

'''
문제 요약: 정답과 제시한답안이 얼마나 일치하는지 알아내는 문제. (정답과 일치한 위치, 숫자면 bull (A). 정답의 숫자만 일치하면 cow (B))
ask: secret = "1807", guess = "7810"
answer: "1A3B"

해석:
한국에서는 숫자야구게임으로 알려진 게임. 숫자와 위치가 맞은 개수랑 숫자만 맞은 개수를 리턴함.
First Try
처음에는 원리보다는 hashmap을 써서 어떻게든 해결해야 겠다는 생각으로 구현하다보니 조건절이 굉장히 많아 복잡해짐.
생각보다 많은 예외를 만나면서 if문이 점점 추가되어 덕지덕지 붙은 형태.
1.bull일때는 cow에도 적용되면 안되기 때문에 bull을 만날시 cow를 1 빼줌.
2.cow가 중복해서 여러번 만나면 안되기 때문에 hashmap에 카운팅을 하나씩 제거해주고 0보다 작으면 더이상 cow를 증가시키지 않음.
3.숫자가 secret에 존재하지 않으면 무시.
이런 원칙을 설계없이 쭉 구현한게 첫번째 방법.

Second Try
필요없는 조건절을 싹 합친형태. bull을 먼저 찾고 그다음 cow를 찾는게 훨씬 효율적.
bull을 찾으면 증가시켜주고 그외에는 해쉬맵에 secret과 guess를 각각 저장.
카운팅 된 값 중에서 가장 적은값이 cow가 되어야 함. (많다고 다 cow가 되는게 아니기 때문. ex) 1000, 0333 에서 0은 하나의 cow만 가짐)
메모리는 좀 더 쓰게되겠지만 사실 0~9의 범위라 constant 증가 수준.
'''

# Second Try: Clean Version
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        hm_g = defaultdict(int)
        hm_s = defaultdict(int)
        for g, s in zip(secret, guess):
            if g == s:
                bulls += 1
            else:
                hm_g[g] += 1
                hm_s[s] += 1
        for k in hm_g.keys():
            cows += min(hm_g[k], hm_s[k])
        return f'{bulls}A{cows}B'

# First Try: Messy Version
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hm = collections.Counter(secret)
        bulls = cows = 0
        for i in range(len(guess)):
            if guess[i] in hm:
                if guess[i] == secret[i]:
                    bulls += 1
                    if hm[guess[i]] <= 0:
                        cows -= 1
                else:
                    if hm[guess[i]] > 0:
                        cows += 1
                hm[guess[i]] -= 1
        return f'{bulls}A{cows}B'
'''