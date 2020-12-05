''' ## 증가 값 합하는 수열 ## '''
''' 1 + 2 + 4 + 7 + 11 + 16 + 22 '''
'''   1   2   3   4    5    6    '''
# i = 0 ## 1씩 증가
# J = 1 ## 수열
# K = 1 ## 합

# while True:
#     i = i + 1
#     J = J + i 
#     K = K + J
#     print('i, J, K : ', i, J, K)
#     if(i<19):continue ## i항 = 피보나치 항 + 1
#     break
# print('최종 i, J, K : ', i, J, K)

''' ## 증가 값 합하는 수열2 ## '''
''' - 1 + 2 - 4 + 7 - 11 + 16 - 22 '''
'''     1   2   3   4    5    6    '''
# i = 0 ## 1씩 증가
# J = 1 ## 수열
# K = -1 ## 합
# L = -1 ## 음, 양

# while True:
#     i = i + 1
#     J = J + i 
#     L = L * -1 ## 부호 바꾸기
#     K = K + (J * L) ## 부호 곱하기
#     print('i, J, K, L : ', i, J, K, L)
#     if(i<19):continue ## i항 = 피보나치 항 + 1
#     break
# print('최종 i, J, K, L : ', i, J, K, L)

''' ## 증가 값 합하는 수열3 ## '''
'''  1 + 3 + 6 + 10 + 15 + 21 + 28 '''
'''1   2   3   4    5    6    7    '''
i = 0 ## 1씩 증가
J = 0 ## 수열
K = 0 ## 합

while True:
    i = i + 1
    J = J + i
    K = K + J
    print('i, J, K : ', i, J, K)
    if(i < 20):continue ## 20번쨰 항까지
    break
print("K : ", K)
