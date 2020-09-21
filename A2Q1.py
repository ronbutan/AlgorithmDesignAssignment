import sys

class TreeNode:
    def __init__(self, l, v, p):
        self._level = l
        self._value = v
        self._parent = p
        self._left = None
        self._right = None
    def insert(self, v):
        if v < self._value:
            if self._left is None:
                self._left = TreeNode(self._level + 1, v, self)
                return self._left
            else:
                return self._left.insert(v)
        else:
            if self._right is None:
                self._right = TreeNode(self._level + 1, v, self)
                return self._right
            else:
                return self._right.insert(v)
    def __reduce_level(self):
        self._level -= 1
        if self._left is not None:
            self._left.__reduce_level()
        if self._right is not None:
            self._right.__reduce_level()
    def __replace(self, n):
        if self._parent is not None:
            if n is not None:
                n._parent = self._parent
            if self._parent._left == self:
                self._parent._left = n
            else:
                self._parent._right = n
    def delete(self, root):
        if self._left is None and self._right is None:
            if self._parent is None:
                return None
            else:
                self.__replace(None)
                return root
        else:
            if self._left is None or self._right is None:
                if self._left is not None:
                    repl = self._left
                else:
                    repl = self._right
                repl.__reduce_level()
            else:
                repl = self.successor()
                if repl._parent == self:
                    repl._left = self._left
                    repl._level = self._level
                    if repl._right is not None:
                        repl._right.__reduce_level()
                else:
                    if repl._right is not None:
                        repl.__replace(repl._right)
                        repl._right.__reduce_level()
                    repl._level, repl._left, repl._right = self._level, self._left, self._right
            if self._parent is None:
                repl._parent = None
                return repl
            else:
                self.__replace(repl)
                return root
    def pre_order_traversal(self, n):
        if n is not None:
            print(n._value, '@ level', n._level, 'root' if n._parent is None else 'left child' if n._parent._left == n else 'right child', 'Parent', n._parent._value if n._parent is not None else 'nil')
            self.pre_order_traversal(n._left)
            self.pre_order_traversal(n._right)
    def pre_order_traversal2(self, n, arr):
        if n is not None:
            arr.append(n._value)
            self.pre_order_traversal2(n._left,arr)
            self.pre_order_traversal2(n._right,arr)
    def in_order_traversal(self, n):
        if n is not None:
            self.pre_order_traversal(n._left)
            print(n._value, '@ level', n._level, 'root' if n._parent is None else 'left child' if n._parent._left == n else 'right child', 'Parent', n._parent._value if n._parent is not None else 'nil')
            self.pre_order_traversal(n._right)
    def in_order_traversal2(self, n, arr):
        if n is not None:
            self.pre_order_traversal2(n._left,arr)
            arr.append(n._value)
            self.pre_order_traversal2(n._right,arr)

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def converttobst(root, arr): 
    # Base Case 
    if root is None: 
        return 
    # First update the left subtree 
    converttobst(root._left, arr) 
    # now update root's data delete the value from array 
    root._value = arr[0]
    arr.pop(0)
    # Finally update the right subtree
    converttobst(root._right, arr) 

""" def constructHeap2(a):
    val = 0
    left = 1
    right = 2
    lstNodes = [n[0] for n in a]
    lstLeftChild = [n[left] for n in a if n[left] != 'x']
    lstRightChild = [n[right] for n in a if n[right] != 'x']
    lstLeftChild.extend(lstRightChild)
    s = set(lstLeftChild)
    diff = set(lstNodes) - s
    print(diff) """

def constructHeap(a):
    dictNodes = {}
    left = 1
    right = 2
    tn = None
    root = None
    for node in a:
        if node[left] == 'x' and node[right] == 'x':
            tn = TreeNode(0,int(node[0]),None)
            n = dictNodes.get(node[0])
            if n is None:
                dictNodes[node[0]] = tn
        else:
            tn = dictNodes.get(node[0])
            if tn is None:
                tn = TreeNode(0,int(node[0]),None)
            if node[left] != 'x':
                n = dictNodes.get(node[left])
                if n == None:
                    n = TreeNode(0,int(node[left]),tn)
                n._parent = tn
                dictNodes[str(n._value)] = n
                tn._left = n
            
            if node[right] != 'x':
                n = dictNodes.get(node[right])
                if n == None:
                    n = TreeNode(0,int(node[right]),tn)
                n._parent = tn
                dictNodes[str(n._value)] = n
                tn._right = n
            dictNodes[node[0]] = tn

    #loop to identiy Root node
    for k,v in dictNodes.items():
        if v._parent is None:
            root = v
            break
    return root

def swap(n):
    if n is None:
        return
    temp = n._left
    n._left = n._right
    n._right = temp


def mirror_BST2(node):
    if node is None:
        return
    swap(node)
    mirror_BST2(node._left)
    mirror_BST2(node._right)
    
def mirror_BST(a):
    root = constructHeap(a) # 2n
    mirror_BST2(root) # n
    arr = []
    root.in_order_traversal2(root, arr) # n
    #arr.sort() #n**2
    mergeSort(arr)
    converttobst(root,arr) # n lg n
    arr = []
    root.pre_order_traversal2(root, arr) # n
    return ' '.join(str(x) for x in arr)

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]   
    print(mirror_BST(a))


#a = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
#a = [['0', '1', '2'], ['1', '3', 'x'], ['3', 'x', 'x'], ['2', '4', 'x'],['4', 'x', '5'],['5', 'x', 'x']]
#a = [['3','x','x'],['1','2','x'],['2','3','x'],['0','1','x']]
#a = [['0','x','1'],['1','x','2'],['2','x','3'],['3','x','x']]
#a = [['0','1','x'],['1','x','2'],['2','3','x'],['3','x','4'],['4','x','x']]
#print(mirror_BST(a))