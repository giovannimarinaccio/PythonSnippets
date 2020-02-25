#!/usr/bin/env python3

import argparse

# Main function definition
def main():
    # Positional arg (parsed by position position)
    parser = argparse.ArgumentParser(description="DESCRIPTION: positional args") # define parser
    parser.add_argument("position1")
    parser.add_argument("position2")
    args = parser.parse_args("pos1arg pos2arg".split())
    parser.print_help()
    print("parsed args: ")
    print(vars(args))
    # Optional arguments (any position)
    parser = argparse.ArgumentParser(description="DESCRIPTION: optional args") # define parser
    # option with limited values accepted
    parser.add_argument("--verbosity", metavar='LEVEL', help="verbosity level", type=str, choices=["INFO", "DEBUG"] )
    # flag option
    parser.add_argument("--flag", help="flag is true if specified", action='store_true')
    # count options like -vvvv in ansible
    parser.add_argument("-c", help="flag is counted to generate arg value", action='count')
    # short / long options
    parser.add_argument("-s","--silent", help="flag silent is false if specified", action='store_false')
    parser.print_help()
    args = parser.parse_args("--verbosity INFO --flag -ccc -s".split())
    print("parsed args: ")
    print(vars(args))

  
# Tests if this module was launched as main 
# or imported in another main (still Global Code)
if __name__== "__main__":
    main()
