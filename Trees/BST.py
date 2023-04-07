class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def wypisz(root):
    if root is None: return
    print(root.key)
    wypisz(root.left)
    wypisz(root.right)

def insert(root, k):
    prev = None
    n = root
    while n is not None:
        if n.key == k: return root
        elif k < n.key: 
            prev = n
            n = n.left
        else: 
            prev = n
            n = n.right
    temp = BSTNode(k)
    if prev.key < k:
        prev.right = temp
    else: 
        prev.left = temp
    temp.parent = prev
    return root

def find(root, k):
    while root is not None:
        if root.key == k: return root
        elif k < root.key: root = root.left
        else: root = root.right
    return None

def min(root):
    while root.left is not None:
        root = root.left
    return root

def max(root):
    while root.right is not None:
        root = root.right
    return root

def succ(root): #następnik
    if root.right is not None:
        return min(root.right)
    while root.parent is not None and root.parent.right == root:
        root = root.parent
    return root.parent

def pred(root): #poprzednik
    if root.left is not None:
        return max(root.left)
    while root.parent is not None and root.parent.left == root:
        root = root.parent
    return root.parent

def remove(root, k):
    x = find(root, k)
    if x is None: return root
    if x.left is None and x.right is None: 
        if x.parent is None: return None
        if x.parent.left == x:
            x.parent.left = None
        else:
            x.parent.right = None
        x.parent = None
        return root
    if x.left is None:
        if x.parent is None: 
            x.right.parent = None
            root = x.right
            x.right = None
            return root
        x.right.parent = x.parent
        if x.parent.left == x:
            x.parent.left = x.right
        else:
            x.parent.right = x.right
        x.right = None
        return root
    
    if x.right is None:
        if x.parent is None: 
            x.left.parent = None
            root = x.left
            x.left = None
            return root
        x.left.parent = x.parent
        if x.parent.left == x:
            x.parent.left = x.left
        else:
            x.parent.right = x.left
        x.left = None
        return root
    xSucc = succ(x)
    tempK = xSucc.key
    root  = remove(root, tempK)
    x.key = tempK #prowizoryczne przeklejenie następnika x w jego miejsce, nie chciało mi się już bawić w przepinanie tych Nodów
    return root

root = BSTNode(10)
insert(root, 5)
insert(root, 1)
insert(root, 15)
insert(root, 12)
insert(root, 20)
insert(root, 25)
insert(root, 11)
insert(root, 17)
insert(root, 23)
insert(root, 18)
insert(root, 16)
insert(root, 19)
insert(root, 19)
insert(root, 15)
print("Drzewo:")
wypisz(root)
remove(root, 10)
print("Drzewo:")
wypisz(root)
print("Poprzednik: ", pred(find(root, 15)).key)
print("Następnik: ", succ(find(root, 15)).key)