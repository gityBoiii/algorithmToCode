''' ## 피보나치 수열 합 ## '''
''' 1 + 1 + 2 + 3 + 5 + 8 + 13 '''
'''  시 작  합                  '''
'''     시  작  합'''
A = 1; B = 1
HAP = 2
CNT = 2

while True:
    C =  A + B  ## 전의 항 더하기
    HAP = HAP + C ## 항의 합
    CNT = CNT + 1 ## 카운트 증가
    print("A, B, C, HAP : ", A, B, C, HAP)
    if (CNT<20): ## 20항까지
        A = B ## 위치
        B = C ## 바꾸기
    else:
        print("HAP : ", HAP)
        break
