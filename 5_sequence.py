'''## 증가하는 수열의 합 ##'''
''' 예시 '''
#1 2 4 7 11 16 22
# 1 2 3 4  5  6

i = 0
J = 1 
K = 1

while True:
    i = i + 1 #1씩 증가
    J = J + i #2번째 항의 값
    K = K + J #+2번째항 -> 초기 시작값 J의 첫번째항
    print("i, J, K의 값 : ", i, J, K)
    if (i < 20):continue
    break
print("K의 값 : ", K)

    