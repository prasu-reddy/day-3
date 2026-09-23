'''
 
-----operators-----
-->operator is used to perform a specific task inbetween two oprands
eg: a+b

= ---> specific task that is addition 
a,b ---> are the operands/variables

-------------- Types of operators --------------

1.Arthemetic operators
2.Assigment operators
3.Logical operators
4.comparison operators
5.Membership operators
6.Identity operators


'''

# Arthemetic operators

first_number=int(input("Enter the first number"))
second_number=int(input("Enter the second number"))


#addition of firstnumber and second number is 30

print(f"addition of {first_number} and {second_number} is {first_number+second_number}")
print(f"subraction of {first_number} and {second_number} is {first_number-second_number}")
print(f"Mul of {first_number} and {second_number} is {first_number*second_number}")
print(f"Div of {first_number} and {second_number} is {first_number/second_number}")
#20/5
print(f"Floor division of {first_number} and {second_number} is {first_number//second_number}")
print(f"Modulus of {first_number} and {second_number} is {first_number%second_number}")



radius=float(input("Enter the radius of the circle"))
area=3.14*radius*radius
print(f"area of the circle is: {area}")

# simple intrest

p=int(input("Enter the amount"))
t=float(input("Enter the time period"))
r=float(input("Enter the rate of intrest"))

simple_intrest=p*t*r/100
print(f"simple intrest is :{simple_intrest}")