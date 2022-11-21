def main():
    i = getPositiveInt()
    print(i)

def getPositiveInt():
    # unfortunetly there is no do-while loop
    while True: # infinite loop
        n = int(input("Enter an integer"))
        if n > 0:
            break
    return n    # no scope rule (n is defined in while loop)

main()    