#Skrifa kóða sem að tekur inn tölu "n" og prentar út algorithmann "n" sinnum.
#Talan þarf að vera jákvæð 
#n1+n2+n3=n4
#n2+n3+n4=n5
#n3+n4+n5=n6
#n4+n5+n6=n7

n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 1
b = 2
c = 3

sum = 0

if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
elif n == 3:
    print(a)
    print(b)
    print(c)
else:
    print(a)
    print(b)
    print(c)

    if n > 3:
        for i in range(0, n-3):
            print(a + b + c)
            if a < b and a < c:
                a = a + b + c
            elif b < c and b < a:
                b = a + b + c
            elif c < a and c < b:
                c = a + b + c
    
    
        

    
