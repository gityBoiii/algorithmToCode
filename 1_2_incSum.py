
''' 조건 나중에 '''

'''int i,J;'''
# i = -1; J=0

# while True:
#     i = i + 2 ## 항
#     J = J + i ## 합
#     print(i,J)
#     if (i<99): continue ## i가 99일떄 종료
#     break
# print("최종 : ", J)



''' for문으로 '''
J=0
for i in range(-1, 99, 2): ## 조건먼저 선언 안됨
    i = i + 2
    J = J + i
    print(i,J)
print("최종 : ", J)

