# Ways of storing string into a variable
name='Welcome'
name="Welcome"
name=str('Welcome')
name=str("Welcome")

#Creating empty strings
# string with out any value with function str saying it is of type string

name=str()
name=''
name=""

# Mutable and Imutable
#Mutable = Changable
#Imutable=Not changable

str1='Welcome'
print(id(str1))
print(str1)
str1=str1+" to Python"
print(id(str1))
print(str1)

