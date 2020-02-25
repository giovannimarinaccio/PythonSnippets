#!/usr/bin/env python3

#Globally executed Code
print("Global Block (Before Main)")

# Main function definition
def a_function():
  print("Function Execution")
  

# Main function definition
def main():
  print("Main Execution")
  a_function()
  
# Tests if this module was launched as main 
# or imported in another main (still Global Code)
if __name__== "__main__":
  print("Main clause was triggered ")
  main()

#Globally executed Code
print("Global Block (After Main)")