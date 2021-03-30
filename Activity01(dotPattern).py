"""
Abdullah Abdulrahman Alahideb (249) (CS046)

A program that construct a dot pattern
"""
n = 5
for x in range(n):
    for y in range(x):
        print('* ', end="")
    print('')
for x in range(n, 0, -1):
    for y in range(x):
        print('* ', end="")
    print('')


