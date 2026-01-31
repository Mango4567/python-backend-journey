#first
age=int(input("Enter your age:"))
if(age)>=18:
    print('You are old enough to learn to drive')
elif(age)<18:
    print(f"you need {18-age} years to learn to drive") # f-string is used for printing values inside string
#second
number=float(input("enter a number"))
if (number>0):
    print("the number is positive",number)
elif (number<0):
    print("the number is negative",number)
elif (number==0):
    print("the number is zero",number)
#third
password=input('enter a password:') #pass is a keyword
if (password=='python123'):
    print("Access Granted")
elif(password!= 'python123'):
    print("Access Denied")
#fourth
num_1=float(input("enter number 1:"))
num_2=float(input("enter number 2:"))
if(num_1>num_2):
    print("first number is greater than second")
elif(num_1<num_2):
    print("second number is greater than first")
else:
    print("numbers are equal")
#fifth
marks=int(input("enter your marks from 1 to 100:"))
if(marks>=90 and marks<=100):
    print("you got A grade")
elif(marks>=75 and marks<=89):
    print("you got B grade")
elif(marks>=50 and marks<=74):
    print("you got C grade")
elif(marks<50 and marks>=0):
    print("you have failed")
else:
    print("invalid marks")
#sixth
N=int(input("enter a number:"))
if(N%3==0 and N%5==0):
    print("FizzBuzz")
elif(N%3==0):
    print("Fizz")
elif(N%5==0):
    print("Buzz")
elif(N%3!=0 and N%5!=0):
    print(N)
#if(year%4==0 and year%400==0and year%100==0): # wrong logic condition here
  #  print("leap year")
#elif(year%4==0 and year%100!=0 and year%400==0): #wrong logic also here
   # print("also a leap year")
#elif(year%4!=0):
#    print("not a leap year")
#seventh
year=int(input("enter year")) #leap year logic main %400==0 and not %4==0 first
if(year%400==0):
    print("leap year")
elif(year%100==0): 
    print("not a leap year")
elif(year%4==0):
    print("leap year")
else:
    print("not leap year")
#eighth
month=input("enter a month of year:").lower().strip()
if(month=='september' or month=='october' or month=='november'):
    print("the season is autumn")
elif(month=='december'or month=='january'or month=='february'):
    print("the season is winter")
elif(month=="march" or month=='april'or month=='may'):
    print("the season is spring")
elif(month=='june'or month=='july'or month=='august'):
    print("the season is summer")
else:
    print("invalid month")

      

          
            
             

           