# Write a Python program to accept n numbers in list and remove duplicates from a list.


lst = list()
while True:
    i = input("Enter a number to add to the linst or break if you are done :  ")
    if i.upper() == 'EXIT' or i == '':
        break
    else:
        i = int(i)
        if i in lst:
            continue
        else:
            lst.append(i)

print(lst)