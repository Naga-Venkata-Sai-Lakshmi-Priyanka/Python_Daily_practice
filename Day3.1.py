n=5
for i in range(n):
    print("* " * n)
print('----Next logic----')
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
print('----Increasing triangle----')
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
print('----Decreasing triangle----')
for i in range(n):
    for j in range(i,n):
        print('*', end=' ')
    print()
print('-----Increasing Right sided truangle----')
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*', end='')
    print()
print('-----Decreasing Right sided truangle----')
n=5
for i in range(n):
    for j in range (i+1):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()
print('------Hill pattern-------')
for i in range(n):
    for j in range(i,n):
        print('', end=' ')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')
    print()
print('----Inverted Hill pattern----')
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print('*', end='')
    for j in range(i,n-1):
        print('*', end='')
    print()

print('-----Diamond Pattern----')
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for j in range(i,n):
        print('*',end='')
    print()