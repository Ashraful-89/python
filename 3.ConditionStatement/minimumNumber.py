a = int(input("Enter the 1st Number : "))
b = int(input("Enter the 2nd number :"))
c = int(input("Enter the third number :"))

if(a < b and a < c) :
    print("The minimum umber is :" , a)

elif(b < a and b < c) :
    print("the minimum number is : " , b)

else :
    print("The minimum number is : ",c)