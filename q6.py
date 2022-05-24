print ("enter n1")
number_1=int(input())

print ("enter n2")
number_2=int(input())

ex_or=number_1^number_2
bin_exor=bin(ex_or)
check_string= str(bin_exor)

a=check_string.count('1')
print(a)
