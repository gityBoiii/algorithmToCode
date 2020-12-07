'''## +SW 변수 이용 ##'''
''' 홀수일때 빼기 -> 조건 순서 다르게  '''
N = 0 # 자연수
H = 0 # 합
SW = 0 # 제어 조건

while(N < 100):
    N = N + 1
    if (SW == 1):
        H = H - N
        SW = 0
    else: 
        H = H + N
        SW = 1 
    print ("SW, N, H", SW, N, H)   
print("H는 : ", H)

''' 홀수일때 빼기 -> 조건 시작값 다르게'''
N = 0 # 자연수
H = 0 # 합
SW = 0 # 제어 조건

while(N < 100):
    N = N + 1
    if (SW == 1):
        H = H - N
        SW = 0
    else: 
        H = H + N
        SW = 1 
    print ("SW, N, H", SW, N, H)   
print("H는 : ", H)