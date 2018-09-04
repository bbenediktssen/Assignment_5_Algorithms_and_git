#Á meðan num_int er ekki mínus tala á að stimpla inn tölur, 
#Svo þarf að taka inn stærstu töluna og geyma hana.

num_int = int(input("Input a number: "))  # Do not change this line
max_int = 0
while num_int > 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
else:
    print("The maximum is", str(max_int))    # Do not change this line
