BLACK = "black"
RED = "red"

class RealRoot:
    def __init__(self):
        self.root = None
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = BLACK #0 - czarny, 1 - czerwony

def wypisz(root):
    if root is None: return
    if root.parent is None:
        print(root.key, root.color, " parent: None")
    else:
        if root.left is not None and root.right is not None:
            print(root.key, root.color, " left: ", root.left.key, "right: ", root.right.key, " parent: ", root.parent.key)
        elif root.left is not None:
            print(root.key, root.color, " left: ", root.left.key, "right:", root.right, " parent: ", root.parent.key)
        elif root.right is not None:
            print(root.key, root.color, " left: ", root.left, "right:", root.right.key, " parent: ", root.parent.key)
        else: 
            print(root.key, root.color, " left: ", root.left,  " right: ", root.right,  " parent: ", root.parent.key)
    wypisz(root.left)
    wypisz(root.right)

def left_rotate(root, realRoot):
    if root.right is None: return root
    y = root.right
    y.parent = root.parent
    if root.parent is None:
        pass
    elif root.parent.left == root:
        root.parent.left = y
    else:
        root.parent.right = y
    root.right = y.left
    if y.left is not None: y.left.parent = root.right
    root.parent = y
    y.left = root
    if root == realRoot.root:
        realRoot.root = y
        realRoot.root.color = BLACK
    return root

def right_rotate(root, realRoot):
    if root.left is None: return root
    y = root.left
    y.parent = root.parent
    if root.parent is None:
        pass
    elif root.parent.left == root:
        root.parent.left = y
    else:
        root.parent.right = y
    root.left = y.right
    if y.right is not None: y.right.parent = root.left
    root.parent = y
    y.right = root
    if root == realRoot.root:
        realRoot.root = y
        realRoot.root.color = BLACK
    return root

def przywroc_czerwono_czarnosc(z, realRoot):
    while z != realRoot.root and z.parent.color != BLACK:
        if z.parent.parent.left == z.parent: 
        #A - ojciec z jest lewym synem dziada
            if (z.parent.parent.right is None or z.parent.parent.right.color == BLACK) and z.parent.right == z: 
            #2. stryj z jest czarny i z jest prawym synem
                z = z.parent #ustawiamy z na ojca 
                left_rotate(z, realRoot) #rotujemy ojca, zeby dostac sytuacje A3
            elif (z.parent.parent.right is None or z.parent.parent.right.color == BLACK) and z.parent.left == z: 
            #3. stryj z jest czarny i z jest lewym synem
                z.parent.color = BLACK #ojciec na czarno
                z.parent.parent.color = RED #dziadu na czerwono
                right_rotate(z.parent.parent, realRoot) #rotacja dziada, nie przesuwamy z bo będzie gitara
            elif z.parent.parent.right.color == RED:
            #1. stryj z jest czerwony
                z.parent.color = BLACK #ojciec czarny
                z.parent.parent.right.color = BLACK #stryju czarny
                z = z.parent.parent #ustawiamy z na dziada
                if z != realRoot.root: z.color = RED #dziadu czerwony, o ile to nie korzen
        
        else:
        #B - ojciec z jest prawym synem dziada - na odwrót wszystkie righty i lefty
            if (z.parent.parent.left is None or z.parent.parent.left.color == BLACK) and z.parent.right == z: 
            #2. stryj z jest czarny i z jest prawym synem
                z.parent.color = BLACK #ojciec na czarno
                z.parent.parent.color = RED #dziadu na czerwono
                left_rotate(z.parent.parent, realRoot) #rotacja dziada, nie przesuwamy z bo będzie gitara
            elif (z.parent.parent.left is None or z.parent.parent.left.color == BLACK) and z.parent.left == z: 
            #3. stryj z jest czarny i z jest lewym synem
                z = z.parent #ustawiamy z na ojca 
                right_rotate(z, realRoot) #rotujemy ojca, zeby dostac sytuacje B3
            elif z.parent.parent.left.color == RED:
            #1. stryj z jest czerwony
                z.parent.color = BLACK #ojciec czarny
                z.parent.parent.left.color = BLACK #stryju czarny
                z = z.parent.parent #ustawiamy z na dziada
                if z != realRoot.root: z.color = RED #dziadu czerwony
    return realRoot.root


def insert(realRoot, k):
    #wstawienie normalnie do drzewa BST
    prev = None
    n = realRoot.root
    while n is not None:
        if n.key == k: return realRoot.root
        elif k < n.key: 
            prev = n
            n = n.left
        else: 
            prev = n
            n = n.right
    z = BSTNode(k)
    if prev.key < k:
        prev.right = z
    else: 
        prev.left = z
    z.parent = prev
    #wstawienie normalnie do drzewa BST
    z.color = RED #czewrony

    #przywracanie własności czewrono-czarnych
    przywroc_czerwono_czarnosc(z, realRoot)

    return realRoot.root

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

def remove(root, k): #to ze zwykłego drzewa bst
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

r = RealRoot()
r.root = BSTNode(13)
insert(r, 8)
insert(r, 6)
insert(r, 17)
insert(r, 22)
insert(r, 11)
insert(r, 15)
insert(r, 27)
insert(r, 25)
insert(r, 1)
insert(r, 26)
insert(r, 30)
insert(r, 31)
insert(r, 32)
insert(r, 33)
print("Drzewo:")
wypisz(r.root)
# remove(root, 10)
# print("Drzewo:")
# wypisz(root)
# print("Poprzednik: ", pred(find(root, 15)).key)
# print("Następnik: ", succ(find(root, 15)).key)