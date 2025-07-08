import sys
s = 1234

for i in str(s):
    print(i)

n = input()

print(n)



n = sys.stdin.readline(int(n)).strip()

print('readline',n)


for  n in sys.stdin:
    print("stdin",n)




