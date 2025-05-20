'''
Problem Statement
Given an Array arr, return the second largest distinct 
element 
from an array. 
If the second largest element doesn't exist then return -1.

12,35,1,10,34,1 - 34
10,5,10 - 5
10,10,10 - -1
'''
'''
Approch 1 - sorting
Approch 2 - using 2 iterations 
in 1st Iteration finding the max and 
In second iteration finding second max
Approch 3 - 
'''

'''
#Approch = 1
l = [10,10,10]
flg = True
for i in range(len(l)-1) :
    for j in range(i+1,len(l)) :
        if l[i]<l[j] :
            l[i],l[j] = l[j],l[i]
for i in range(len(l)-1) :
    if l[i]!=l[i+1] :
        print(l[i+1])
        flg = False
if flg :
    print(-1)
  
'''
# Approch - 3
#l = [12,35,1,10,34,1]
#l = [10,10,5]
l = [10,5]

ma = -1 # First Maximum
sema = -1 # Second Maximum

for i in range(len(l)) :
    if l[i]>ma :
        ma = l[i]
    if l[i]<ma and l[i]>sema :
        sema = l[i]
if sema == -1 :
    print(-1)
else :
    print(sema)

"""
In the above Approch, we are inititally want to keep max and 
second max element as -infinite and then if element if greater than
max and if it is greater than second max, we are updating second
max

"""






