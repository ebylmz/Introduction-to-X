import sys

if len(sys.argv) != 2:  
    print("missing command-line argument")
    sys.exit(1) # like returning main function

print(f"Hello {sys.argv[1]}")