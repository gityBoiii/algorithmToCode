''' ## 진법 변환 ## '''
# B=0; BB=0; C=0; MOK=0; NMG=0; i=0; A = [0]*10

# B = int(input("B 입력 : ")) ## 10진수 
# BB = B ## B대입
# C = 0 ## 배열의 위치

# while True:
#     C = C + 1 ## 배열 저장
#     MOK = int(B/2) ## 몫 
#     NMG = B - MOK*2 ## 나머지
#     print("C, MOK, B : ", C, MOK, B)
#     A[C] = NMG;  ## 각 자릿수 = 나머지
#     if(MOK == 0):
#         break
#     else:
#         B = MOK    
# print("BB(원본) : ", BB)
# for i in range(1, C+1, 1): ##C번째 배열 포함 출력
#     print("A[%d] : %d" %(i, A[i]))

''' ## 선 처리, 후 i++ ## '''

A = [0]*10
i = 1
NUM = int(input("10진수 입력 : "))

while (NUM != 0):
    MOK = int(NUM/2)
    REM = NUM % 2  # NUM - MOK*2
    A[i] =  REM ## 배열에 넣기
    NUM = MOK ## 줄어든 수 적용
    i = i + 1 ## 인덱스 증가

while True:
    if(i <= 1):
        break
    else:
        print("A[%d] : %d" %(i-1, A[i-1])) ## 저장 인덱스보다 +1이므로
        i = i -1
