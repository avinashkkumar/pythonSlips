# A) Write a Python program to check if a given key already exists in a dictionary.
#  If     key exists replace with another key/value pair.
dic = dict()
while True:
    i = input("enter a key for checking : ")
    if i.upper() == "EXIT" or i  == "":
        break
    else:
        if i in dic :
            print("the key has been found in the dictonay")
            dic[i] = input("enter the replacement value ")
        else:
            dic[i] = input("the key was not found in the dictonary please enter the valur for it : ")

print(dic)