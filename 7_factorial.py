''' ## 팩토리얼 합 ## '''
''' 1! + 2! + 3! + 4! ... 10! '''
# i = 1 ## 순서
# K = 1 ## 총합
# J = 1 ## 각 항

# while True:
#     i = i + 1 ## 2부터 시작
#     J = J * i * i
#     K = K + J
#     print("i, J, K : ", i, J, K)
#     if (i < 10):continue ## i가 10일때 종료
#     break
# print("K : ", K)

''' ## 팩토리얼 합 ## '''
''' 1! + 2! + 3! + 4! ... + 10! '''
# i = 0 ## 순서
# SUM = 0 ## 총 합
# F = 1 ## 각 항

# while True:
#     i = i + 1
#     F = F * i ## 1 * 2 * 3 * 4 ... 마지막 항 : i
#     if (i < 11): ## 선조건 후 계산 : 11이면 계산x 종료
#         SUM = SUM + F
#         print("i, F, SUM : ", i, F, SUM)
#     else:
#         print("SUM : ", SUM)
#         break

''' ## 팩토리얼 합 ## '''
''' 1! - 2! + 3! - 4! ... - 10! '''
i = 0 ## 순서
SUM = 0 ## 총 합
SW = 0 ## 부호 반전
F = 1 ## 각 항

while True:
    i = i + 1
    F = i * F ## 각 항 처리
    if (i<11): ## 11에서 계산 안함
        if(i%2 == 0): #짝수일때 
            SUM = SUM - F ## 합에 더함
            SW = 1 ## 처리 후 1
        else:
            SUM = SUM + F
            SW = 0
        print("i, F, SUM : ", i, F, SUM)
    else:
        print("SUM : ", SUM)
        break

            
        