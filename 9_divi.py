''' ## 약수 구하기 ## '''
B = 0; MOK = 0; NVG = 0; i = 0; A = list(range(100))
B = int(input("B 입력 : ")) ## 입력 숫자
C = 0; D = 0 ## 순서, 배열위치(0부터 시작)

while True:
    C = C + 1
    if (C <= B): ## 입력 숫자까지
        MOK = int(B/C) ## int(나누기)
        NVG = B - MOK * C ## 원본 - 몫*나누는수
        if (NVG == 0): ## 나눠지면
            A[D] = MOK ## 배열에 저장
            D = D + 1 ## 배열 위치 증가
    else:
        break
print("B : ", B)

for i in range(1, D, 1): ## 배열[0] 무시? : 배열[0] = B 
    print("A[%d] : %d"% (i, A[i]))

