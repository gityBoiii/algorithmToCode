'''## 1씩 증가, 모두 곱하기 ##'''
''' 2부터 곱 '''
# N = 1
# H = 1

# while True:
#     N = N + 1 ## 먼저 더하고 
#     H = H * N ## 곱
#     print("N,H : ",N,H)
#     if(N<100):continue
#     break
# print("H 출력 : ", H)

''' 1부터 곱 '''
# N = 1
# H = 1

# while True:
#     H = H * N ## 먼저 곱하고 
#     print("N,H : ",N,H)
#     N = N + 1 ## 더하기. 표시/처리 결과 달라 문제 발생 가능
#     if(N<=100):continue # 표시후 조건값이 달라질시 -> 경우의 수 따질 필요성
#     break
# print("H 출력 : ", H)

''' 음, 양 번갈아 곱 '''
# i = 0
# J = 1

# while True:
#     i = i + 1
#     if (i%2 == 0):
#         J = J * i 
#     else:
#         J = J * -i
#     print("i,J : ",i,J)
#     if(i<100):continue
#     break
# print("J 출력 : ", J)

''' 음, 양 번갈아_분수로 합 '''
i = 0
J = 0

while True:
    i = i + 1
    if (int(i/2) == (i/2)):
        J = J + (i/(i+1))
    else:
        J = J - (i/(i+1))
    print("i,J,(i/(i+1)) : ",i,J,(i/(i+1)))
    if(i<99):continue ## 99번째 항까지
    break
print("J 출력 : ", J)
