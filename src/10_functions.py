# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
  if x % 2 == 0:
    print(x)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def even_number(x):
  if x % 2 == 0:
    print("Even!")
  else: 
    print("Odd.")

even_number(num)