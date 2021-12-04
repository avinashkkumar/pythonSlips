# A) Write a python script to find the repeated items of a tuple

lst = list()

while True:
    i = input("enter the number for tuple input : ")
    if i.upper == "EXIT" or i =="":
        break
    else:
        lst.append(i)
print(lst)
tup = tuple(lst)

# tup = (1,2,3,4,5,6,7,8,9,0,2,4,6,8)
dic = dict()

for i in range(len(tup)):
    if tup[i] in dic:
        dic[tup[i]] += 1
    else:
        dic[tup[i]] = 1

for k , v in dic.items():
    if v > 1:
        print(k)