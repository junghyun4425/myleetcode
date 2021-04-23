# Problem Link: https://leetcode.com/problems/string-compression/

'''
문제 요약: 문자들이 들어있는 배열을 압축하는 문제. (추가 메모리 사용 금지, 원래 배열을 압축해서 길이를 반환)
ask: ["a","a","b","b","c","c","c"]
answer: 6 (배열은 다음과 같이 바뀌어 있어야 함: ["a","2","b","2","c","3"])

해석:
추가 배열을 사용하지 않고 현재 배열 그대로 사용해야 하는 제약조건이 있음.
같은 단어가 연속해서 있는 경우를 슬라이딩 윈도우 방법을 적용시켜 해결했던 문제.
단어가 반복되는 경우, 시작점 i 끝점 j 로 위치를 찾아냄.
그리고 ans라는 위치값이 실제 배열을 바꾸게되는 위치.
따라서 윈도우 사이즈를 알아내고 ans 위치에 단어와 길이를 저장해나감.
위의 과정을 반복하면 최종 ans의 위치를 알수있으며, 시간복잡도 O(n) 공간복잡도 O(1) 로 해결이 가능함.
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = j = 0
        while i < len(chars):
            cnt = 0
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
                cnt += 1
            if cnt > 1:
                chars[ans] = chars[i]
                ans += 1
                for c in str(cnt):
                    chars[ans] = c
                    ans += 1
            else:
                chars[ans] = chars[i]
                ans += 1
            i = j
        return ans