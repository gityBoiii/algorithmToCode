''' ## 나누어 떨어지는 지 ## '''
# A = int( input("A를 입력 : ") ) ## 입력값
# i = A - 1 ## 입력값 -1
# J = 2 ## 2부터 1씩 증가

# while True:
#     if(J <= i): ## J가 A까지 도달하면 소수
#         if(A%J == 0):
#             print("소수 아님") ## 나뉘므로
#             break
#         else:
#             J = J + 1 ## 다음수 시험
#         print("A, i, J : ", A, i, J)
#     else:  ## 모든 수로 판별 완료시
#         print("소수") ## 자기자신 이외 수로 안나뉘므로
#         break
    
''' ## 제곱근 ## '''
''' A의 약수는 sqrt(A)안에 있다 '''
''' 2*18, 3*12, 6*6, 12*2, 18*2 << 대칭구조. 가운데 sqrt까지만 구하면 됨 '''
from math import sqrt

A = int( input("A를 입력 : " ) ) 
J = 2 ## 2부터 자기자신-1에 나뉘면 소수 아님

while True:
    if(J <= sqrt(A)): ## sqrt(A)보다 작으면
        if( A%J == 0 ):
            print("A, J : ", A, J)
            print("소수 아님")
            break
        else:
            print("A, J, sqrt(A) : ", A, J, sqrt(A))
            J = J + 1 ## 판별 수 +1
    else:
        print("소수")
        break

