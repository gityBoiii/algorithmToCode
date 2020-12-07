
i = 0
SUM = 0

while True:
    i = i + 1
    if ( i%2 == 0 ): ## i 나머지가 0일때
        SUM = SUM + i
        print(i, SUM)

    if (i<100):continue ## i 100까지
    break

print("SUM 출력 : ", SUM)

    
