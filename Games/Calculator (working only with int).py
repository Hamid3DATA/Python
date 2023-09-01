def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Pick an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

answer = int(input("answer: "))
if answer == 1:
    print("What is your first number?")
    add1 = int(input())
    print("Pick a second number")
    add2 = int(input())
    print("The sum of your numbers are", add1 + add2)
    
    
if answer == 2:
    print("Pick first number")
    sub1 = int(input())
    print("Pick your second number")
    sub2 = int(input())
    print("The sum of your numbers are", sub1 - sub2)
    
if answer == 3:
    print("What is your first number")
    mul1 = int(input())
    print("what is your second number")
    mul2 = int(input())
    print("The sum of your numbers are", mul1 * mul2)
    
if answer == 4:
    print("Pick your first number")
    div1 = int(input())
    print("Pick your second number")
    div2 = int(input())
    print("The sum of your numbers are", div1 / div2)
    