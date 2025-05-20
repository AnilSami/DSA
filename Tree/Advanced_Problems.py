class Node :
    def __init__(self,val) :
        self.val = val
        self.left = None
        self.right = None
    def LevelOrderTravel(self,root) :
        if root is None :
            return 
        print(root.val)
        pass
    def HeightOfTree(self,root) :
        if root is None :
            return 0
        return max(1 + self.HeightOfTree(root.left),1 + self.HeightOfTree(root.right))
    def PreOrder(self,root,Dia=0,maxDia=0) :
        if root is None :
            return 
        Dia = self.HeightOfTree(root.left) + self.HeightOfTree(root.right)
        self.ma = max(self.ma,Dia)
        self.PreOrder(root.left)
        self.PreOrder(root.right)
        
    def DiameterOfTree(self,root) :
        '''
        Diameter = HeightOfLeftSubTree + HeightOfRightSubTree
        '''
        if root is None :
            return 0
        self.ma = 0
        self.PreOrder(root)
        return self.ma
    
'''
HeightOfTree,
PreOrder,
DiameterOfTree - All these functions are interlinked so need,
to work together to get the diameter.
'''
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(60)
g = Node(70)
h = Node(80)
i = Node(90)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

print(f'Height of Tree {a.HeightOfTree(a)}')
print(f'Diameter of Tree {a.DiameterOfTree(a)}')