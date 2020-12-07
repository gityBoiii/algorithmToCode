'''## 소인수분해 ##'''
A =  [0]*20
DEC = int(input("DEC 입력 : "))
CNT = 1 ## 순서도는 명시하지 않을시 배열 1부터

while True:
    print("처음 시작 점")
    J = 2
    while True:
        if(DEC%J == 0):
            A[CNT] =  J ## 약수 추가
            DEC = int(DEC/J) ## 나눠진 값으로
            print("DEC : ", DEC) 
            break 
        else:
            J = J + 1 ## 다음 수로 나누기 
    print("두번쨰 시작 점")     
    if(DEC == 1):
        break ## 다 나뉘기 전까지 계속
    else:
        print('CNT : ', CNT)
        CNT = CNT + 1

if(CNT != 1):
    for i in range(1, CNT, 1): ##마지막 배열 전까지
        print("A[i] : ", A[i]) 
print("A[CNT] : ", A[CNT]) ## 마지막 배열
