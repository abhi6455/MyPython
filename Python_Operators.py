#Arithmatic Operrations 
a=10
b=5

print("Addition =",a+b)
print("Substraction=",a-b)
print("Multiplication",a*b)
print("Float division",a/b)
print("Integer Division",a//b)
print("Modulus",a%b)
print("Pow",a**b)

#STR operation 
str1="Abhishek"
str2="Chaturvedi"
full_name=str1+" "+str2
print("FullName =",full_name)


# Assignment operators
# =  , x = 5
# += , x += 5 -> x = x + 5
# -= , x -= 5 -> x = x - 5
# *= , x *= 5 -> x = x * 5
# /= , x /= 5 -> x = x / 5
# //= , x //= 5 -> x = x // 5
# %= , x %= 5 -> x = x % 5


# Comparison Operators ( we compare operand values)
# == , Equals to condition , x == y
# != , Not Equals to condition , x != y
# > , Greater than condition , x > y
# < , Less than condition , x < y
# >= , Greater than and Equals to condition , x >= y
# <= , Less than and Equals to condition , x <= y

a = 10
b = 5
print("Result of a == b , ", a == b)
print("Result of a != b , ", a != b)
print("Result of a > b , ", a > b)
print("Result of a < b , ", a < b)
print("Result of a >= b , ", a >= b)
print("Result of a <= b , ", a <= b)


# logical operators in Python ( Logical check will happen for expression result)
# and -> Returns true if both statements are true 
# or -> Returns true if one of statements are true
# not -> Reverse the result, returns false if the result is true

m = 10
n = 8
print("m>10 and n<10 Result " , m>10 and n<10) # False and True -> False
print("m>20 or n<10 Result " , m>10 or n<10) # False or True -> 
print("not(m>20 and n<10) Result " , not(m>10 and n<10)) 
# not(False and True) -> not(False) -> True
