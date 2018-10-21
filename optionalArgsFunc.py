#!/usr/bin/env python3

# Main function definition
def a_function(arg1, arg2, **kwargs):
  optArg1=None
  optArg2=None
  if("optArg1" in kwargs):
    optArg1=kwargs['optArg1']
  if("optArg2" in kwargs):
    optArg2=kwargs['optArg2']
  print("invoked with following args[", "arg1:", arg1, "arg2:", arg2, "optArg1:", optArg1, "optArg2:", optArg2, "]")
  

# Main function definition
def main():
  a_function(1,2)
  a_function(1,2,optArg1=3333)
  a_function(1,2,optArg1=3333,optArg2=4444)
  a_function(1,2,optArg2=4444)

if __name__== "__main__":
  main()
