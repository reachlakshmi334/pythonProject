"""
1. Checking the given number is Negative or Positive number

num =int(input("Enter a number:"))
if num<0:
    print("The given number is Negative number")
if num>0:
    print("The given number is Positive number")



# 2. Checking the largest of Three numbers.

num1=10
num2=20
num3=30
if num1 > num2 & num1 > num3:
    print("Num1 is greater than all the three numbers")
if num2>num1 & num2>num3:
    print("Num2 is greater than all the three numbers")
if num3>num1 & num3>num2:
    print("Num3 is greater than all the three numbers")

# Assignmrnt :3 Print week number if you provide week name as input

weekname = 'coolday'
if weekname=='Monday':
    print("The week number is 1")
elif weekname=='Tuesday':
    print("The week number is 2")
elif weekname=='Wednessday':
    print("The week number is 3")
elif weekname=='Thursday':
    print("The week number is 4")
elif weekname=='Friday':
    print("The week number is 5")
elif weekname=='Saturday':
    print("The week number is 6")
elif weekname=='Sunday':
    print("The week number is 7")
else:
    print("Wrong week name")

"""
# 2. Checking the largest of two numbers.

# num1,num2 =50, 20
# print("num1 is greater") if num1>num2 else print("Num2 is greater")
# if num1>num2:
#     print("Num1 is greaterthen Num2")
# if num1<num2:
#     print("Num2 is greaterthen Num1")


# 2. Checking the largest of Three numbers.

# num1, num2, num3 =80,60,130
# if num1 > num2 and num1 > num3:
#     print("Num1 is greater than all the three numbers")
# elif num2>num1 and num2>num3:
#     print("Num2 is greater than all the three numbers")
# else:
#     print("Num3 is greater than all the three numbers")

# 2. Checking the largest of two numbers.

num1,num2 =50, 120
# print("num1 is greater") if num1>num2 else print("Num2 is greater")
if num1>num2:
     print("Num1 is greaterthen Num2")
else:
     print("Num2 is greaterthen Num1")
