# 삼항문법 *연산자x 
# 자바 삼항연산자 => (조건식) ? a : b;
a = 10
b = 8
result1 = "맞아요" if (a > b) else "틀려요"
print(result1)

result2 = "맞아요" if (a > b and a < 10) else "틀려요"
print(result2)

result3 = "맞아요" if (a < b or a >= 10) else "틀려요"
print(result3)

print("a") if (1 == 2) else "b"
#python2 버전
#(print("a")) if (1 == 2) else print("b")