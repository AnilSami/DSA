'''
You are given an array of integers arr[]. 
Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 
1 4 3 2 6 5. After reversing the array, 
the first element goes to the last position, 
the second element goes to the second last position and
 so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. 
The reversed array will be 2 5 4.
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, 
hence the reversed array is same as the original.

class Solution:
    def reverseArray(self, arr):
        if len(arr) == 1 :
            return arr
        temp = arr[0]
        s,e = 0,len(arr)-1
        while e>s :
            arr[s],arr[e] = arr[e],arr[s]
            s+=1
            e-=1
        arr[len(arr)-1] = temp
        return arr
'''
#l = [1,4,3,2,6,5]
l = [4,5,2]
temp = l[0]
s,e = 0,len(l)-1
while e>s :
    l[s],l[e] = l[e],l[s]
    s+=1
    e-=1
l[len(l)-1] = temp
print(l)
    




