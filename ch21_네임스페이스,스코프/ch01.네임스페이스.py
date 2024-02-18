# 네임스페이스(namespace)
a = '홍길동'
b = 99

def function1():
    a = '이순신'
    c = [1 ,2 ,3]
    
    def function2():
        d = (1, 2, 3)
        print('Local =>', locals())

    function2()
    print('Enclosing =>', locals())
    print('-' * 30)

function1()
print('Global =>', globals())
print('-' * 30)