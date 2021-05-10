
# get input from the user
N = input("What is the number: ")


#initialize the first two numbers of the fibonacci sequence
a = 0
b = 1

# get the number that corresponds to N from the fibonacci sequence, subtracting 1 because b is initialized to the first position already
for i in range(int(N)-1):
  # get the next number in the sequence
  val = a + b

  # set a and b to their new values
  a = b
  b = val

print("val is: " + str(val))

# get the sum of the digits

# initialize the sum
sum = 0

# mod the number by 10, store that number
while val > 10:
  m = val % 10
  sum = sum + m
# subtract modded number from the original number

  val = val - m
# divide number by 10, check if result is greater than 10

  val = val / 10
  # two cases:
  # 1. result is less than 10, add mod number to sum variable
    # 2 is less than 10, sum = 2+3 = 5
  # 2. result is greater than 10, mod the number and repeat 
  if val < 10:
    sum = sum + val    
   

print("the sum of the digits is: " + str(int(sum)))