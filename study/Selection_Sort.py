'''
개요: 선택정렬을 실제로 구현하기.
설명:
선택정렬을 이해하고 바로 구현.
괸장히 직관적인 알고리즘이라 버블정렬보다 구현자체는 난이도가 쉬운편.
앞에 정렬된 고정사이즈를 두고 그 자리에 들어갈 숫자를 찾는 방법.
i가 정렬된 배열의 크기를 의미하므로 하나씩 증가해 나가서 결국 끝까지 정렬이 되는 방식.

시간복잡도: Best - O(n^2) / Worst - O(n^2)
공간복잡도: O(1)
'''

class SelectionSort:
    @staticmethod
    def sort(arr):
        a_len = len(arr)
        for i in range(a_len):
            for j in range(i+1, a_len):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [5,4,6,5,4,3,8,7,1]
    SelectionSort.sort(arr)
    print(arr)