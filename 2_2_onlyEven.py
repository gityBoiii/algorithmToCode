
i = 0
SUM = 0

while True:
    i = i + 2 # i가 2씩 증가
    SUM = SUM + i
    
    # print(i, SUM)
    if (i < 100) : continue
    break

print("SUM 출력 : ", SUM)