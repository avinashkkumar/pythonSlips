# A)Write a Python program to compute element-wise sum of given tuples.
# Original lists:(1, 2, 3, 4)(3, 5, 2, 1)(2, 2, 3, 1)
# Element-wise sum of the said tuples: (6, 9, 8, 6)

def sumt(lst):
    add = 0
    for i in lst:
        add += i
    return add
        

tup = [(1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1)]
w = []
x = []
y = []
z = []

for i in tup:
    for j in range(len(i)):
        if j == 0:
            w.append(i[j])
        elif j == 1:
            x.append(i[j])
        elif j == 2:
            y.append(i[j])
        elif j == 3:
            z.append(i[j])

tsum = (sumt(w),sumt(x),sumt(y),sumt(z))
print("Element-wise sum of the said tuples : ",tsum)

