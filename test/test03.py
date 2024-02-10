sum3 = 0
sum5 = 0

for i in range(1, 101):
    if i%3==0:
        sum3+=i
    if i%5==0:
        sum5+=i

print(sum3)
print(sum5)