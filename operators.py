#area of triangle
h= float(input("enter the height of triangle:"))
b=float(input("enter the base of triangle:"))
A=0.5*h*b
print("the area of triangle is:",A)
#perimeter
side_1=float(input("Enter Side A:"))
side_2=float(input("Enter Side B:"))
side_3=float(input("Enter Side C:"))   
Peri=side_1+side_2+side_3
print("the perimeter of triangle is",Peri) 
#pay calculator
hrs=float(input("Enter worked hours:"))
rate_perhour=float(input("Enter payrate per hour:"))
days=int(input("Enter days worked in a month:"))
salary_usd=(hrs*rate_perhour*days)
print("monthly salary of the employee in USD is:",salary_usd)
#length comparison
print(len('python') > len('dragon'))


         
                             