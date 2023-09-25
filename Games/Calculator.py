print("Pick an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

answer = input("answer: ")
if answer == "1":
    add1 = input("What is your first number?")
    try:
      add1 = int(add1)
    except ValueError:
      try:
        add1 = float(add1)
      except ValueError:
        print("you did not type a number!")
        quit()
      
    add2 = input("Pick a second number")
    try:
      add2 = int(add2)
    except ValueError:
      try:
        add2 = float(add2)
      except ValueError:
        print("you did not type a number!")
        quit()
    print("The sum of your numbers are", add1 + add2)
    
    
elif answer == "2":
    sub1 = input("Pick first number")
    try:
      sub1 = int(sub1)
    except ValueError:
      try:
        sub1 = float(sub1)
      except ValueError:
        print("you did not type a number!")
        quit()
      
    sub2 = input("Pick your second number")
    try:
      sub2 = int(sub2)
    except ValueError:
      try:
        sub2 = float(sub2)
      except ValueError:
        print("you did not type a number!")
        quit()
    print("The sum of your numbers are", sub1 - sub2)
    
elif answer == "3":
    mul1 = input("What is your first number")
    try:
      mul1 = int(mul1)
    except ValueError:
      try:
        mul1 = float(mul1)
      except ValueError:
        print("you did not type a number!")
        quit()
      
    mul2 = input("what is your second number")
    try:
      mul2 = int(mul2)
    except ValueError:
      try:
        mul2 = float(mul2)
      except ValueError:
        print("you did not type a number!")
        quit()
    print("The sum of your numbers are", mul1 * mul2)
    
elif answer == "4":
    div1 = input("Pick your first number")
    try:
      div1 = int(div1)
    except ValueError:
      try:
        div1 = float(div1)
      except ValueError:
        print("you did not type a number!")
        quit()
      
    div2 = input("Pick your second number")
    try:
      div2 = int(div2)
    except ValueError:
      try:
        div2 = float(div2)
      except ValueError:
        print("you did not type a number!")
        quit()
    print("The sum of your numbers are", div1 / div2)
    
else:
  print("please select from 1-4")
    
