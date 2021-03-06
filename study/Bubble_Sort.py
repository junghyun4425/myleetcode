'''
개요: 버블정렬을 실제로 구현하기.
설명:
버블정령을 이해하고 바로 구현.
처음에는 자꾸 첫번째 for문 i를 어딘가에 쓸려고 했는데 필요없다는걸 조금 늦게 깨달음.
그래서 j와 j+1 이거 두개만으로 수행을 하되, 처음부터 끝까지 가는 행동을 배열 길이만큼 해주면 완성.
너무 쉽게 봤다가 구현할때 시간이 걸린... 쉬운문제도 방심하지 않도록 해야함.

시간복잡도: Best - O(n^2) / Worst - O(n^2)
공간복잡도: O(1)
'''

class BubbleSort:
    @staticmethod
    def sort(arr):
        a_len = len(arr)
        for _ in range(a_len):
            for j in range(a_len-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = [5,4,6,5,4,3,8,7,1]
    BubbleSort.sort(arr)
    print(arr)