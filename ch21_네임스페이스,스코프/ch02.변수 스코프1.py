# 스코프(scope)
a = '홍길동'
b = 99

def function1():
    a = '이순신'
    c = [1 ,2 ,3]
    print('Local a =',a)
    print('Local b =',b)
    print('Local c =',c)

function1()
print('Global a =',a)
print('Global b =',b)
# print('Global c =',c) # error