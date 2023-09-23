#https://www.acmicpc.net/problem/1300
# 다이나믹 프로그래밍 (?)
#
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27

# 1 2 3
# 2 4 6
# 3 6 9

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# 1 이렇게 추가된다. 1x1 
# 2 2 4 이렇게 추가된다 2x2 3개
# 3 3 6 6 9 이렇게 추가된다. 3x3 5개
# 4 4 8 8 12 12 16 이렇게 추가된다. 4x4 7개
# 5 5 10 10 15 15 20 20 25 이렇게 추가된다. 5x5 9개
# 6 6 12 12 18 18 24 24 30 30 36 이렇게 추가된다. 6x6 11개

# 점화식 : N*2-1

# k가 100001이 들어오면
# 100000번째 부터 시작해서 1을 101x101번째에 추가될 첫번째 수를 출력한다 101

# k가 9999가 들어오면
# k가 100x100 의 전 원소값을 출력한다. 100*99

# n이 6이면
# 1, 3 , 5 , 7, 9, 11 순으로 숫자가 추가된다. 총 (36개)
import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

def findK():
    index = 1
    for i in range(1, N+1):
        temp = i
        counter = 0
        for _ in range(1, i*2):
            if counter == 2:
                temp *= 2
                counter = 0

            counter +=1

            if index == k:
                print(temp)
                return
            
            index += 1

findK()