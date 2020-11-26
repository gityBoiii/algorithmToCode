'''## if, else 이용 ##'''
''' 홀수 거르기 '''
N = 0 # 자연수
H = 0 # 합

while True:
    N = N + 1
    if (N%2 == 1):
        H = H + N * N
        # print("N, H : ",N, H)
    if (N < 99):continue
    break
print("H는 : ", H)