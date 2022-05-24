a = int(input('Enter the length of the 1st side: '))
b = int(input('Enter the length of the 2nd side: '))
c = int(input('Enter the length of the 3rd side: '))
while (a+b>c) and (b+c>a) and (c+a>b):
    print("Yes")
    break
else:
    print("No")

