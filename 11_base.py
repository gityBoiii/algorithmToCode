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
# A = [0]*10
# i = 1
# NUM = int(input("10진수 입력 : "))

# while (NUM != 0):
#     MOK = int(NUM/2)
#     REM = NUM % 2  # NUM - MOK*2
#     A[i] =  REM ## 배열에 넣기
#     NUM = MOK ## 줄어든 수 적용
#     i = i + 1 ## 인덱스 증가

# while True:
#     if(i <= 1):
#         break
#     else:
#         print("A[%d] : %d" %(i-1, A[i-1])) ## 저장 인덱스보다 +1이므로
#         i = i -1

''' ## 인덱스 윗자리부터 (몇자린지 어케암?) ## '''
# def range1(start, end): ## 순서도처럼 for문 range 정의
#     return range(start, end+1)

# DEC = int(input("10진수 입력 : ")) ## 수 입력

# S = [1] * 9
# for i in range1(1, 8): ## 1 <= i <= 8
#     S[i] = 0
#     print(i, S[i])
# M = 1; R = 0 ## 몫, 나머지
# i = 8 ## 인덱스

# while True:
#     if(M == 0):
#         break
#     else:
#         M = int(DEC/2)
#         R = DEC - (M*2)
#         S[i] =  R
#         DEC = M
#         i = i - 1
# for i in range1(1, 8):
#     print('S[%d] : %d' %(i, S[i]))

''' ## 2진수 -> 10진수 ## '''
# S = [0] * 8 ## 2진수
S1 = (list(input("2진수 8자리 입력 : "))) ## 각 자리 배열로
S1 = [int(i) for i in S1] ## int로 변환

S = ['dummy']
for i in range(len(S1)): ## 한자리씩 옮기기 (1~8로 만들기)
    S.append(S1[i])

DEC = 0 ##합계
P = 2 ## 인덱스
while True:
    K = 2**(8-P) ## 각 자리값
    DEC = DEC + (K*S[P]) ## 각 자리값 * 있는지
    print("K, P, DEC : ", K, P, DEC)
    P = P + 1
    if(P < 9):continue
    break
if(S[1] == 0): ## 부호가 0일때
    pass
else : ## 음수일때
    DEC = 128 - DEC ## 양수(2) + 2의 보수 = 큰 자릿수
    DEC = DEC * (-1) ## 부호 붙여줌
print("DEC : ", DEC)
