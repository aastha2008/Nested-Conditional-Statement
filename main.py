'''

if/elif/else statement


if (Condition):
  Body Statement1

elif (Condition):
  Body Statement2
...
...
...

else:
  Body Statement3

Nested Consitional Statement:
- A consitional statement inside another conditional statement

Indentation is important
- The header/clause of a nested constional statement must be indented from an outer header:

if (Condition):
  Body statement 1
  if (Condition):   <-- starting a nested statement
    Body statement 1a. <-- ending a nested statement

elsif (Condition):
  Body statement 2
  if (Condition):   <-- starting a nested statement
    Body Statement 2a

  elif (Condition):
    Body statement 2b

  else:
    Body Statement 2c.  <--- Ending a nested statement
...
...
else:
  Body Statement3
'''

# Example:
x = y = 10

if (x < y):
  print ("x is less than y")
else:
  if (x > y):
    print ("x is greater than y")
  else:
    print ("x and y must be equal")

## Excercise: Evaluate if your number is positive/negative/zero and odd/even:
userNum = int(input("Enter a number: "))

# Positive
if (userNum > 0):
  print ("positive number")
  if (userNum % 2 == 0):
    print ("even number")
  elif (userNum %2 == 1):
    print ("odd number")



# Negative
elif (userNum < 0):
  if (userNum % 2 == 0):
    print ("even number")
  elif (userNum %2 == 1):
    print ("odd number")
  print ("negative number")

# Zero
else:
  print ("number is zero")



