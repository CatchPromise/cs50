import sys

if len(sys.argv) < 2:
    print("Too Few Arguments")

for arg in sys.argv [1:]:
    print("hello, my name is", arg)