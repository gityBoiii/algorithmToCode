'''## 소인수분해(미완) ##'''
A =  list(range(20))
DEC = int(input("DEC 입력 : "))
CNT = 1 ## 순서도는 명시하지 않을시 배열 1부터

while True:
    J = 2
    if (DEC%J == 0): ## 나뉘면
        A[CNT] =  J ## 배열에 넣기
        DEC = int(DEC/J) ## 나눠진 값으로
    else:
        J = J + 1 ## 다음 수로 나누기
    if(DEC != 1):continue ## 다 나뉘기 전까지 계속
    break
if(CNT != 1):
    for i in range(1, 20, 1):
        print("A[i] : ", A[i])
else:
    print("A[CNT] : ", A[CNT])
