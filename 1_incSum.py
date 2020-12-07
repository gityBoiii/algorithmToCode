
## int i, j;
i=0;j=0

# for i in range(100): ## 이러면 0부터 시작
#     j=j+i
#     #print(i,j)
# print(i,j)

while True:
    i = i + 1
    j = j + i
    print('i, j : ', i,j)
    if(i<100):continue
    break
print('최종 i, j : ', i,j)