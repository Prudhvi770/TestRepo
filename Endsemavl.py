class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1

class AVLTrees:
    #preamble:-return the height of the tree
    #Time complexity:- O(1)
    def get_height(self,root):
        if not root:
            return 0
        return root.height
    #preamble:-we are going to check the balence tree in height of left tree minus
    #          height of right tree
    #Time Complexity:-O(1)
    def get_balenced(self,root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)
    #preamble:-It will perfornm the rotation into fix the right -Right imbalence tree
    #Time Complexity:-O(1)
    def left_rotate(self,x):
        y=x.right
        t=y.left
        y.left=x
        x.right=t
        x.height= 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height= 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y
    #preamble:-It will perfornm the rotation into fix the left-left imbalence tree 
    #Time Complexity:-O(1)
    def right_rotate(self,x):
        y=x.left
        t=y.right
        y.right=x
        x.left=t
        x.height= 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height= 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y
    #preamble:-we are going update the element like normal bst and update the height and compute
    #          the balence of the tree and we are going to check the rotation cases on LL,RR,LR,RL
    #Time Complexity:-O(logn)
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif key<root.key:
            root.left=self.insert(root.left,key)
        elif key>root.key:
            root.right=self.insert(root.right,key)
        else:
            return root
        root.height= 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance=self.get_balenced(root)

        if balance > 1 and key<root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key>root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key>root.left.key:
            root.left=self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key<root.right.key:
            root.right=self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    #preamble:- Searching a element in the tree
    #Time complexity:-O(logn)
    def search(self,root,key):
        if not root:
            return False
        if root.key==key:
            return True
        elif key<root.key:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
    #Preamble:- it going sort element left to node to right
    #Time Complexity:-O(n)    
    def inorder(self,root,reverse=False):
        if not root:
            return []
        if reverse:
            return self.inorder(root.right,True) + [root.key] + self.inorder(root.left,True)
        else:
            return self.inorder(root.left) + [root.key] + self.inorder(root.right)
    #Preamble:- it going sort element node to left to right
    #Time Complexity:-O(n)      
    def preorder(self,root,reverse=False):
        if not root:
            return []
        if reverse:
            return [root.key] + self.preorder(root.right,True)  + self.preorder(root.left,True)
        else:
            return [root.key] + self.preorder(root.left) +  self.preorder(root.right)
    #preamble:-It performs bst deletion and update the height of current node
    #          and balence the tree and it will rectify the impractle positions with rotation
    #Time Complexity:- O(logn)
    def delete(self,root,key):
        if not root:
            return root
        elif key<root.key:
            root.left=self.delete(root.left,key)
        elif key>root.key:
            root.right=self.delete(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ=root.right
                while succ.left:
                    succ=succ.left
                root.key=succ.key
                root.right=self.delete(root.right,succ.key)
        
        root.height= 1 + max(self.get_height(root.left),self.get_height(root.right))
        balance =self.get_balenced(root)
        if balance>1 and self.get_balenced(root.left) >=0:
            return self.right_rotate(root)
        if balance>1 and self.get_balenced(root.left) <0:
            root.left=self.left_rotate(root)
            return self.right_rotate(root)
        if balance<-1 and self.get_balenced(root.right)<=0:
            return self.left_rotate(root)
        if balance<-1 and self.get_balenced(root.right)>0:
            root.right=self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
Tree=AVLTrees()
root=None
numbers=[11,22,33,44,55,26]

for num in numbers:
    root=Tree.insert(root,num)

print("Inorder Traversal:",Tree.inorder(root))
print("Preorder Traversal:",Tree.preorder(root))
print("search:",Tree.search(root,22))
print("search:",Tree.search(root,24))
root=Tree.delete(root,44)
print("After deletion:",Tree.inorder(root))
print("Height:",Tree.get_height(root))  