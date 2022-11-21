# dictionary, key and values
phonebook = {
    "Brian": "+1-617-495-2000",
    "David": "+1-624-334-1237"
}

name = input("Name: ")
# searches all of the keys
# dictionary uses hash table and search is close to constant time
# set uses hash table to prevent dublication
if name in phonebook:   
    print(f"Number {phonebook[name]}")
else:
    print("Not Found")
