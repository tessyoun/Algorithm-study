import sys

# 부분 수열이 반복되는지 체크하는 함수
def is_goodSeq(temp):
    l = len(temp)
    # 부분 수열이 반복되는지 확인
    for length in range(1, l // 2 + 1):
        if temp[-length:] == temp[-2*length:-length]:
            return False
    return True

def dfs():
    # 길이가 N이면 수열 출력 후 종료
    if len(temp) == N:
        print(*temp, sep='')  # 띄어쓰기 없이 출력
        sys.exit()  # 프로그램 종료
        return

    # 1부터 3까지 수열 생성
    for i in range(1, 4):
        # 이전에 넣은 숫자와 현재 넣을 숫자가 다를 때만 추가
        if not temp or temp[-1] != i:
            temp.append(i)
            # 부분 수열이 유효한지 확인
            if is_goodSeq(temp):
                dfs()
            temp.pop()

N = int(input())
temp = []
dfs()
