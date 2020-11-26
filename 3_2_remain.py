'''## +SW 변수 이용 ##'''
''' 홀수 거르기 '''
N = 0 # 자연수
H = 0 # 합
SW = 0 # 제어 조건

while True:
    N = N + 1
    if(SW == 0):
        H = H + N * N
        SW = 1
    else:
        SW = 0
    # print("SW, N, H : ",SW, N, H)   
    if(N<99):continue
    break
print("H는 : ", H)

''' 홀수일때 빼기 '''
# N = 0 # 자연수
# H = 0 # 합
# SW = 0 # 제어 조건

# while(N < 100):
#     N = N + 1
#     if (SW == 0):
#         H = H + N
#         SW = 1
#     else: 
#         H = H - N
#         SW = 0 
#     print ("SW, N, H", SW, N, H)   
# print("H는 : ", H)

''' 홀수일때 빼기 -> SW 1부터 시작 '''
# N = 0 # 자연수
# H = 0 # 합
# SW = 1 # 제어 조건

# while(N < 100):
#     N = N + 1
#     if (SW == 1):
#         H = H + N
#         SW = 0
#     else: 
#         H = H - N
#         SW = 1
#     print ("SW, N, H", SW, N, H)   
# print("H는 : ", H)