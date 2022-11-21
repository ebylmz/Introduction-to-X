# everything charachter based is string, there is no such thing as char
# so "" and '' are equivalent to each other

s = input("Do you agree? ")

# if s == 'Y' or s == 'y':
#     print("agreed")
# elif s == 'N' or s == 'n':
#     print("not agreed")

if s.lower() in ["y", "yes"]:
    print("agreed")
elif s.lower() in ["n", "no"]:
    print("not agreed")
