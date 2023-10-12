# if(conditions):
#     statement;
# else;
#     statements

if(10>5):
  print("true")

if(5>10):
  print("true")
else:
  print("false")
age1=12
if(age1>18):
   print("You are adult")
else:
  print("You are child")

num2=0
if(num2>0):
  print("Positive")
elif num2==0:
  print("Zero")
else:
  print("Negative")

age=int(input("Enter your age:"))
if(age>18):
    print("You can vote")
else:
    print("You can't vote")

num1=int(input("Enter a number:"))
if(num1>0):
   print("Positive Number")
elif num1==0:
   print("Zero")
else:
   print("Negative Number")

print("Alwase execute")

num=int(input("Enter a number:"))
if(num<0):
    print("Negative number")
elif(num>0):
    if(num<10):
        print("Number between 1 to 10")
    elif(num<20):
        print("Number between 11 to 20")
    else:
        print("Number is more than 20")
else:
    print("Zero number")


#Ends If-Else Statments