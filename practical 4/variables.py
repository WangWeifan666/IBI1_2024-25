a=15
b=75
c=a+b
d=90
e=5
f=d+e
print(c)
print(f)
#f>c
if c > f:
    print("Driving is faster")
elif c == f:
    print("The time for the two transport is the same")
else:
    print("Taking bus is quicker")
#Taking bus is faster
X=True
Y=False
W=X and Y
print(W)

'''
Truth table for W:
X     | Y     | W
-----------------------
True  | True  | True
True  | False | False
False | True  | False
False | False | False
'''

