#숫자를 입력하고 입력받은 숫자가 몇 번 박수를 치는지

#방법 1 : 사람이 생각하는 방법
# a =33
# 문자열 = str(a)
# 
# 카운트=0
# for x in 문자열:
#     if x in ['3','6','9']:
#         카운트+=1
# 
# print(카운트)

#방법 2 : 컴퓨터가 생각하는 방법 : 뒤에서부터 나눠서 구하기
a =33

카운트=0
while a:
    if a%10 in [3,6,9]:  # in을 써서 리스트에 들어있는지 확인한다.
        카운트 +=1
    a = a // 10
print(카운트)