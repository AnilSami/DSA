class Node :
    def __init__(self,val) :
        self.val = val
        self.left = None
        self.right = None 
    def Max_node(self,root,ma=-99) :
        if root == None :
            return ma
        if root.val>ma :
            ma = root.val
        ma = self.Max_node(root.left,ma)
        ma = self.Max_node(root.right,ma)
        return ma
    def Min_node(self,root,ma=99) :
        if root == None :
            return ma
        if root.val<ma :
            ma = root.val
        ma = self.Min_node(root.left,ma)
        ma = self.Min_node(root.right,ma)
        return ma
    def Sum_Nodes(self,root) :
        if root == None :
            return 0
        return root.val+self.Sum_Nodes(root.left)+self.Sum_Nodes(root.right)
    def Height_Tree(self,root,ma=0) :
        if root == None :
            return 0
        ma = 1+self.Height_Tree(root.left,ma)
        ma = 1+self.Height_Tree(root.right,ma)
        return ma
    def Mirror(self,root) :
        if root == None :
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.Mirror(root.left)
        self.Mirror(root.right)
    def Travel(self,root) :
        if root == None :
            return 
        print(root.val)
        self.Travel(root.left)
        self.Travel(root.right)
    def SameTree(self,T1,T2) :
        '''
        Checking Where 2 tree are identical or not
        it mean it should be both left and right all 
        the node, i.e not mirrors.
        '''
        if T1 == None and T2 == None :
            return True
        if T1 == None or T2 == None :
            return False
        if T1.val != T2.val :
            return False
        return self.SameTree(T1.left, T2.left) and self.SameTree(T1.right, T2.right)
    def SymmetricTree(self,root1,root2) :
        if root1 is None and root2 is None :
            return True
        if root1 is None or root2 is None :
            return False
        if root1.val != root2.val :
            return False
        return self.SymmetricTree(root1.left, root2.right) and self.SymmetricTree(root1.right, root2.left)
    

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(60)
g = Node(70)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
print("Max Node", a.Max_node(a))
print("Min Node", a.Min_node(a))
print("Sum of all node values :", a.Sum_Nodes(b))
print("Height of the Tree",a.Height_Tree(a)-1)
print(f'Mirror Before : {a.Travel(a)}')
print(f'Mirror After : {a.Mirror(a)} {a.Travel(a)}')

print("------")

T11 = Node(1)
T12 = Node(2)
T13 = Node(3)

T21 = Node(1)
T22 = Node(2)
T23 = Node(3)

T11.left = T12
T11.right = T13

T21.left = T22
T21.right = T23

ab = T11.SameTree(T11,T21)
if ab :
    print("Same Tree")
else :
    print("Not Same Tree")

print("Example 1 Symmetric-------")

r1 = Node(1)
a = Node(2)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(4)
f = Node(3)

r1.left = a
r1.right = b
a.left = c
a.right = d
b.left = e
b.right = f

ab = r1.SymmetricTree(r1,r1)

if ab :
    print("Symmetric")
else :
    print("Not Symmetric")

print("-Example 2 Symmetric------")

r1 = Node(10)
a = Node(20)
b = Node(20)
c = Node(30)
d = Node(20)


r1.left = a
r1.right = b
a.left = c
b.right = d

ab = r1.SymmetricTree(r1,r1)

if ab :
    print("Symmetric")
else :
    print("Not Symmetric")