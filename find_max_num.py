a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))
c = int(input("Enter your Third number :"))

if a>b and a>c:
    print("First number is larger in all three numbers: ",a)
elif b>a and b>c:
    print("second number is larger than in all three numbers :",b)    
elif c>a and c>b:
    print("Third number is larger than in all three numbers :",c)    
elif a==b==c:
    print("All three number is equal ")
elif a==b>c:
    print("first and second is greater than third number ")
elif b==c>a:
    print("second and third number is greater than first number")        
elif c==a>b:
    print("third and first number is greater than second number ")
else:
    print("error")        