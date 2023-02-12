# 선형검색
# 정의 : 직선 모양(선형)으로 늘어선 배열에서 검색하는 경우에 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘

# 선형검색의 종료 조건
# 1. 검색할 값을 찾지 못하고 배열의 맨 끝을 지나간 경우
# 2. 검색할 값과 같은 원소를 찾는 경우

from typing import Any, Sequence #함수 어노테이션(annotation, 주석달기))

def seq_linear_search(a: Sequence, key: Any) -> int:
    
    # for문 구현
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

    # while문 구현
"""    i = 0 
    while True :
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1  """
    

if __name__ == "__main__": # 스크립트 프로그램이 직접 실행되었는지, 임포트되었는지 파악. 직접 실행될 때는 "__main__", 임포트될 때는 원래의 모듈 이름
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    key = int(input("검색할 값을 입력해주세요: "))

    index = seq_linear_search(x, key)

    if index == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{index}]에 있습니다.")
