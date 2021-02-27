# Problem Link: https://leetcode.com/problems/repeated-dna-sequences/

'''
문제 요약: 10개의 길이로 반복되는 패턴을 가진 DNA 구조를 모두 찾아내는 문제. (A,C,G,T)
ask: "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
answer: ["AAAAACCCCC","CCCCCAAAAA"]

해석:
문제가 정확히 어떤걸 요구하는지 잘 몰랐음. (10개씩 완벽히 반복되는걸 찾는지, 10개 안에 들은 값도 반복패턴에 포함되는지)
10개안의 비교할 DNA도 반복패턴에 포함이 되는것을 알고, 두가지 방법을 고민함.
첫번째는 Brute Force 지만, 메모리를 거의 사용하지 않는 방법. 시간복잡도는 O(n^2)
두번째는 Hash map으로 메모리를 많이 사용하는 경우도 있겠지만, 시간복잡도는 O(n)
문제에서 원하는 바가 속도인 것 같아 해쉬맵을 활용해 문제를 해결.
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        s_len = len(s)
        if s_len < 10: return []
        ans = []
        hm = {}
        for i in range(s_len-9):
            cur = s[i:i+10]
            hm[cur] = hm.get(cur, 0) + 1
            if hm[cur] > 1 and cur not in ans:
                ans.append(cur)
        return ans