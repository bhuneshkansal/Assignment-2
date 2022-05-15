def countBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
     
def FlippedCount(a , b):
    return countBits(a^b)
 
a = int(input("enter n1: "))
b = int(input("enter n2: "))
print(FlippedCount(a, b))
