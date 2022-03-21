# 구현
# 왕실정원 = 체스판 형태의 8x8 좌표
# 나이트 : L자 형태로만 이동, 정원 밖 이동불가
    # 1. 수평으로 두 칸 이동 뒤에 수직으로 한칸 이동
    # 2. 수직으로 두칸 이동 뒤에 수평으로 한칸 이동
# 나이트가 이동할 수 있는 경우의 수 출력하기
# 조건) 행 위치 표현> 1~8 / 열 위치 표현 > a~h

# 풀이 계획
# 상하좌우 문제와 비슷
# 한번에 최대 8가지 경우의 수
# dir = [(-2,-1),(-2,1),(+2,-1),(+2,1)]
# x,y 입력받기

# 함수
# for - 4
    # 수평체크
    # y += dir[i][0] 
    # x += dir[i][1]
    
    # 수직체크
    # x += step[i][0]
    # y += step[i][1]

def check(x,y):
    nx,ny = x,y
    cnt=0
    step = [(-2,-1),(-2,1),(+2,-1),(+2,1)]
    for i in range(4):
        x = nx+step[i][0]
        y = ny+ step[i][1]
        if x >=1 and x<=8 and y>=1 and y<=8:
            cnt+=1
    return cnt

data = input()
x = int(data[1])
y = int(ord(data[0]))- int(ord('a')) +1 # a부터 숫자를 세서 몇번째인지
print(check(x,y)+check(y,x))

# step 으로 8가지 경우의 수를 모두 저장해도 되지만 양쪽이 같은 것에서
# 재활용 힌트를 얻어 함수로 만들었다.
# check() 매개변수로 수평, 수직을 두번 체크하였다
# 디버깅 : x = nx+step[i][0] 코드를 원래 x+= 로 만들어서 x,y값 초기화가 매번 안되었던 점이 있다.