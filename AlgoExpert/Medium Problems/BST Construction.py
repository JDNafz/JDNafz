'''
Construct a Binary Search Tree that has insert, 
remove, contains, and remove methods

🔵 Medium Difficulty

'''




# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
       
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left    
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else: 
                    currentNode = currentNode.right        
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
            

    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:

                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # print("removing",value,"from",currentNode.value)
                # Start removing it
                
                #has two children
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                    currentNode = None
                    
                
                    
                #rootNode case
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else: #if the BST is only the root
                        # currentNode.value = None
                        currentNode = None


                 # has one child
                elif currentNode.left is not None or currentNode.right is not None:
                    #if it has a right node
                    if currentNode.left is None:
                        #if currentNode is to the left of it's parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        else:
                            parentNode.right = currentNode.right
                        
                    
                    #else it has a left node
                    else:                   
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        else:
                            parentNode.right = currentNode.left
                    currentNode = None

                # has no children:
                elif currentNode.left is None and currentNode.right is None:
                    if currentNode.value < parentNode.value:
                        parentNode.left = None
                    else:
                        parentNode.right = None
                    #not sure if the following is needed.
                    currentNode = None
                else:
                    print("MAJOR BUG")
              
                        
                        
               
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

        
        # Do not edit the return statement of this method.
        return self



















