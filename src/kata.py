import shlex
import sys


#
# Apply Method
# @param input
# @return
#    
def apply(input):
    #your code here
    return input

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply([5, 0, -5]))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 