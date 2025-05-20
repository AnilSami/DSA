class Node :
    def __init__(self,val) :
        self.val = val
        self.left = None
        self.right = None
    def Pre_Order(self,root) :
        if root == None :
            return
        print(root.val)
        self.Pre_Order(root.left)
        self.Pre_Order(root.right)
        
    def In_Order(self,root) :
        if root == None :
            return 
        self.In_Order(root.left)
        print(root.val)
        self.In_Order(root.right)
        
    def Post_Order(self,root) :
        if root == None :
            return 
        self.Post_Order(root.left)
        self.Post_Order(root.right)
        print(root.val)
    def size(self,root) :
        if root == None :
            return 0
        return 1 + self.size(root.left) + self.size(root.right)
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
a.Pre_Order(a)
print("-----")
a.In_Order(a)
print("-----")
a.Post_Order(a)
print("-----")
print(a.size(b))