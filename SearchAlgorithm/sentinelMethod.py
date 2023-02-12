# 선형검색에서의 보초법(Sentinel Method)
# 이전 선형검색의 반복문 내에는 배열이 끝났는지 확인하는 구문이 포함되어 있음.
# 보초법은 확인하고자 하는 원소를 배열의 제일 마지막에 추가한다.
# 배열이 끝났는지 확인하는 구문을 삭제함으로서 반복문 중에 하나의 단계를 생략할 수 있어 판단 횟수를 반으로 줄일 수 있다.

from typing import Any, Sequence
import copy

def seq_senticel_method(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)  # 배열을 복사
    a.append(key)   # 배열 마지막에 찾고자 하는 원소를 추가하여 새로운 배열 완성

    i = 0   # 배열 원소를 스캔하여 검색하는 과정을 반복
    while True:
        if a[i] == key:
            break   # 새로 만든 배열에서 위 조건이 성립하면 스캔 종료
        i += 1
    return -1 if i == len(seq) else i   # 값을 찾았을 때, 해당 값이 보초인지 아닌지 판단, i ==  len(seq)라면 검색 실패

if __name__ == "__main__":
    num = int(input("원소의 수를 입력하세요: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))
    
    key = int(input("검색할 값을 입력하세요: "))

    index = seq_senticel_method(x, key)

    if index == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값을 갖는 원소는 x[{index}]에 있습니다")