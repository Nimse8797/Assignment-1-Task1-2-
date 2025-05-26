
num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
num1=float(num1)
num2=float(num2)
a=num1+num2
b=num1-num2
c=num1*num2
if(num2!=0):
   d=num1/num2
   d=float(d)
else:

   d="undefined"

a=float(a)
b=float(b)
c=float(c)

print("Addition: ",a)
print("Subtraction: ",b)
print("Multiplication: ",c)
print("Division: ",d)