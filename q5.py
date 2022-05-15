
def is_triangle(a, b, c):
    if  c>(a+b) or b>(a+c) or a>(b+c):
        print('No')
    else:
        print('Yes')
def triangle():
    a = int(input('Enter the length of the 1st side: '))
    b = int(input('Enter the length of the 2nd side: '))
    c = int(input('Enter the length of the 3rd side: '))
    is_triangle(a, b, c)
    
triangle()
