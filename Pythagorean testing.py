#From the given three numbers the code will tell whether they form a Pythagorean triplet or not

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if((a*a+b*b==c*c) | (a*a+c*c==b*b) | (b*b+c*c==a*a)):
        print("It is a pythagorean triplet")
else:
        print("It is not a pythagorean triplet")