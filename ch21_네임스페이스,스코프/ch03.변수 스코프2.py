# 스코프(scope)
a = '홍길동'
b = 99

def function1():
    a = '이순신'
    c = [1 ,2 ,3]
    
    def function2():
        d = (1, 2, 3)
        print('Local a =',a)
        print('Local b =',b)
        print('Local c =',c)
        print('Local d =',d)
    
    function2()
    print('Enclosing a =',a)
    print('Enclosing b =',b)
    print('Enclosing c =',c)
    # print('Enclosing d =',d) # error

function1()
print('Global a =',a)
print('Global b =',b)
# print('Global c =',c) # error
# print('Global d =',d) # error