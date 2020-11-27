'''## 1씩 증가, 모두 곱하기 ##'''
''' 2부터 곱 '''
# N = 1
# H = 1

# while True:
#     N = N + 1
#     H = H * N
#     print("N,H : ",N,H)
#     if(N<100):continue
#     break
# print("H 출력 : ", H)

''' 1부터 곱 '''
# N = 1
# H = 1

# while True:
#     H = H * N
#     print("N,H : ",N,H)
#     N = N + 1 #처리 후 합. 표시/처리 결과 달라 문제 발생 가능
#     if(N<=100):continue # 표시후 조건값이 달라질시 -> 경우의 수 따질 필요성
#     break
# print("H 출력 : ", H)

''' 음, 양 번갈아 곱 '''
i = 0
j = 1

while True:
    i = i + 1
    if (i%2 == 0):
        j = j * i 
    else:
        j = j * -i
    print("i,j : ",i,j)
    if(i<100):continue
    break
print("j 출력 : ", j)

''' 음, 양 번갈아_분수로 합 '''
# i = 0
# j = 0

# while True:
#     i = i + 1
#     if (int(i/2) == (i/2)):
#         j = j + (i/(i+1))
#     else:
#         j = j - (i/(i+1))
#     print("i,j,(i/(i+1)) : ",i,j,(i/(i+1)))
#     if(i<100):continue
#     break
# print("j 출력 : ", j)
