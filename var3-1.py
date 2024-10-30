A,B = map(int,input().split())
s = 0
for i in range(A,B + 1):
    s += i ** 2
print(s)