'''
개요: 삽입정렬을 실제로 구현하기.
설명:
삽입정렬을 이해하고 바로 구현.
이전에 구현한 선택정렬, 버블정렬과 성능차이가 크게 나지는 않지만 베스트 케이스일 때 조금 효율이 좋음.
그렇다고해서 O(n^2)의 성능이 좋아진다거나 하진 않음.
i가 key를 의미하고 j는 key가 위치할 곳을 탐색하는 인덱스의 역할을 함.

시간복잡도: Best - O(n) / Worst - O(n^2)
공간복잡도: O(1)
'''

class InsertionSort:
    @staticmethod
    def sort(arr):
        a_len = len(arr)
        for i in range(1, a_len):
            for j in range(i):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [5,4,6,5,4,3,8,7,1]
    InsertionSort.sort(arr)
    print(arr)