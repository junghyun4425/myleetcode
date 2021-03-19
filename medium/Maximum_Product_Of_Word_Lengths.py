# Problem Link: https://leetcode.com/problems/maximum-product-of-word-lengths/

'''
문제 요약: 입력으로 들어오는 단어들의 길이를 곱해서 최대값을 반환하는 문제 (단, 단어에 스펠링 중복이 있다면 0)
ask: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
answer: 16

해석:
두개의 워드를 집합으로 묶어서 intersaction한 결과가 0이 되면 중복된 스펠링이 없다는 의미.
따라서 위의 경우에만 단어길이를 곱해서 임시의 배열에 저장.
마지막에 결과들의 최대값을 반환하고, 만약 비어있다면 0을 반환.
성능 자체는 빠르지 않기 때문에 아마 다른 내가 생각못하는 풀이법이 있으리라 예상.
다음 리뷰때 다시 도전해보는 것으로. (최적화는 생각해봐도 여기서 더 빠르게 하기 어려운것 같음)
'''

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        w_len = len(words)
        muls = []
        for i in range(w_len):
            for j in range(i+1, w_len):
                if len(set(words[i]).intersection(set(words[j]))) == 0:
                    muls.append(len(words[i])*len(words[j]))
        return max(muls) if muls else 0