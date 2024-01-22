# Part 1
class BinaryTreeNode:
    data_field = None
    left_child = None
    right_child = None
    
    # Default Constructor
    def __init__(self,value):
        self.data_field = value
    # Getters
    def get_value(self):
        return self.data_field
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
    # Setters
    def set_value(self,updated_value):
        self.data_field = updated_value
    def set_left_child(self,entry):
        self.left_child = entry
    def set_right_child(self,entry):
        self.right_child = entry
# End of Part 1

# Part 2
class BinaryTree:
    root = None
    def __init__(self):
        pass
    
    def insert(self,value):
        traversal = self.root
        if (traversal == None):
            traversal = self.root = BinaryTreeNode(value)
            return
        else:
            switch = True
            while(switch):
                if value == traversal.get_value():
                    print(f"Value {value} already included")
                    return
                elif value<traversal.get_value():
                    if traversal.get_left_child() is None: 
                        traversal.set_left_child(BinaryTreeNode(value))
                        switch = False
                    traversal = traversal.get_left_child()
                else:
                    if traversal.get_right_child() is None:
                        traversal.set_right_child(BinaryTreeNode(value)) 
                        switch = False
                    traversal = traversal.get_right_child()
    
    def search(self,value):
        # This exploits BST structure to use weak ordering rule and find the element according to its value
        # Since it only returns True and False, user is responsible for deciding what to do with boolean
        traversal = self.root
        if(traversal == None):
            return False
        
        while True:
            if(traversal.get_value() == value):
                return True
            elif(traversal.get_value() < value):
                if(traversal.get_right_child() == None):
                    return False
                else:
                    traversal = traversal.get_right_child()
            else:
                if(traversal.get_left_child() == None):
                    return False
                else:
                    traversal = traversal.get_left_child()
    
    def delete_node(self,value, subtree=None, subtree_rear= None):
        # Default parameters on the right can be ignored by user, it is designed for initial call in recursion and internal use
        if(subtree_rear == None):
            # This is to handle an initial call
            subtree = self.root
        if(subtree_rear != None and (subtree.get_left_child() == None and subtree.get_right_child() == None)):
            # This is base case handling when we want to remove a child and it does not have further items downward at risk of loss
            if(subtree_rear.get_left_child() is subtree):
                subtree_rear.set_left_child(None)
            else:
                subtree_rear.set_right_child(None)
        else:
            # This is our recursive case, where we avoid immediately removing a node in case it has its own children, so we recursively call removal of a node until we reach our base case 
            traversal_rear = None
            traversal_front = subtree
            while True:
                # This while loop is designed to search for the first element which we want to remove
                if traversal_front is None:
                    # While we search for element in BST, we ran into a NoneType value, so it is not in the tree. We print the error code and terminate
                    print(f"The item {value} could not be found for removal")
                    return
                elif(traversal_front.get_value() == value):
                    break
                elif(traversal_front.get_value() < value):
                    traversal_rear = traversal_front
                    traversal_front = traversal_front.get_right_child()
                else:
                    traversal_rear = traversal_front
                    traversal_front = traversal_front.get_left_child()
            if(traversal_front.get_left_child() == None and traversal_front.get_right_child() == None):
                # No complex recursion required since there are no elements below which run the risk of being lost
                if(traversal_rear.get_value() < value):
                    traversal_rear.set_right_child(None)
                else:
                    traversal_rear.set_left_child(None)
            elif(traversal_front.get_left_child() == None and traversal_front.get_right_child() != None):
                find_smallest_rear = traversal_front
                find_smallest = traversal_front.get_right_child()
                while True:
                    # This searches for the value to replace it, then recursively calls for the removal of the value we put to replace the initial deleted element
                    if(find_smallest.get_left_child() != None):
                        find_smallest_rear = find_smallest
                        find_smallest = find_smallest.get_left_child()
                    elif(find_smallest.get_left_child() == None):
                        break
                traversal_front.set_value(find_smallest.get_value())
                self.delete_node(find_smallest.get_value(),find_smallest,find_smallest_rear)
            else:
                find_largest_rear = traversal_front
                find_largest = traversal_front.get_left_child()
                while True:
                    # This also does something similar by using a replacement value,then recursively calling to remove that replacement value until we reach a base case with no further elements below which risk getting lost
                    if(find_largest.get_right_child() != None):
                        find_largest_rear = find_largest
                        find_largest = find_largest.get_right_child()
                    elif(find_largest.get_right_child() == None):
                        break
                traversal_front.set_value(find_largest.get_value())
                self.delete_node(find_largest.get_value(),find_largest,find_largest_rear)


    def in_order_append(self,list, BinaryTreeNode):
        # For internal use only, can be ignored by user
        if(BinaryTreeNode == None):
            return
        else:
            # This recursively calls on the left child, then inserts the current element to a list, then recursively calls the right child.
            self.in_order_append(list, BinaryTreeNode.get_left_child())
            list.append(BinaryTreeNode.get_value())
            self.in_order_append(list, BinaryTreeNode.get_right_child())
    def in_order_traversal(self):
        # This was designed for the user, where we provide an empty list to the other dependent recursive function to save the traversal and return it.
        result = []
        self.in_order_append(result,self.root)
        return tuple(result)
        
    def pre_order_append(self,list, BinaryTreeNode):
        # For internal use only, can be ignored by user
        if(BinaryTreeNode == None):
            return
        else:
            # This calls in a different order from current node, left child to right child.
            list.append(BinaryTreeNode.get_value())
            self.pre_order_append(list, BinaryTreeNode.get_left_child())
            self.pre_order_append(list, BinaryTreeNode.get_right_child())
    def pre_order_traversal(self):
        # Similar approach to previous traversal function
        result = []
        self.pre_order_append(result,self.root)
        return tuple(result)

    def post_order_append(self,list, BinaryTreeNode):
        # For internal use only, can be ignored by user
        if(BinaryTreeNode == None):
            return
        else:
            # This follows traversal rule to use left child, right child, then current node.
            self.post_order_append(list, BinaryTreeNode.get_left_child())
            self.post_order_append(list, BinaryTreeNode.get_right_child())
            list.append(BinaryTreeNode.get_value())
    def post_order_traversal(self):
        # Similar approach to other two traversal functions, to use an internal function and update our empty list and return.
        result = []
        self.post_order_append(result,self.root)
        return tuple(result)
# End of Part 2

# Part 3
# This initializes a tree, inserts values, attempts to put duplicates which puts an error message, and deletes a node
trees = BinaryTree()
trees.insert(7)
trees.insert(3)
trees.insert(11)
trees.insert(1)
trees.insert(5)
trees.insert(9)
trees.insert(11)
trees.insert(13)
trees.insert(4)
trees.insert(6)
trees.insert(1)
trees.insert(8)
trees.insert(12)
trees.insert(14)
trees.delete_node(11)

# This shows the traversals, I will also use a special function to print elements and indicate their parents or if it is a root
print("The pre-order traversal is:",trees.pre_order_traversal())
print("The post-order traversal is:",trees.post_order_traversal())
print("The in-order traversal is:",trees.in_order_traversal())

# To search for elements in our tree. Assignment said to make search a true/false function, so user is responsible for what to do with result.
if(trees.search(9)):
    print("We found the value 9")
else:
    print("We could not find 9")
# This 23 was never inserted, so it must say not found
if(trees.search(23)):
    print("We found the value 23")
else:
    print("We could not find the value 23")
    
if(trees.search(12)):
    print("We found the value 12")
else:
    print("We could not find the value 12")

# Since we deleted this above, it has to say 11 is not found
if(trees.search(11)):
    print("We found the value 11")
else:
    print("We could not find the value 11")


def printElements(Node,depth = 0,ParentNode = None):
    # This was not required for assignment but I created it for visual purposes
    indent = 2*'\t'
    if(Node!=None):
        printElements(Node.get_right_child(),depth+1,Node)
        print()
        if(ParentNode == None):
            print(indent*depth,Node.get_value(),"(Root)")
        else:
            print(indent*depth,Node.get_value(),f"(Parent {ParentNode.get_value()})")
        print()
        printElements(Node.get_left_child(),depth+1,Node)

# Here, I'll print the design of a tree before and after removing an element to prove it maintains BST structure

# Let's print before we remove 9        
printElements(trees.root)

# Let's skip lines, remove 9 and print the tree
print()
print("This is a gap")
print()
trees.delete_node(9)
printElements(trees.root)
# You'll see it rearranges elements to remove 9 and still has BST structure



# To demonstrate we get an error when trying to remove a non existent value, I will use the following command
trees.delete_node(25)
# End of part 3

# This is the extra credit question
def Height(TreeNode):
    # This is internal use only for recursion
    if(TreeNode == None):
        # Since root has a height of 1, we must set an empty tree to a height of 0
        return 0
    elif(TreeNode.get_left_child() == None and TreeNode.get_right_child() == None):
        # I follow the rules given in assignment, root only with no children means a height of 1
        return 1
    else:
        # Here, i recursively call on height for each subtree, then only take the result from the greater sized portion so we can get the longest size possible, giving the definition of height of tree
        l_height = Height(TreeNode.get_left_child())
        r_height = Height(TreeNode.get_right_child())
        return (l_height + 1) if (l_height>r_height) else (r_height+1)

def PrintHeight(TreeClass):
    # This is the function created for the user. It was created so user can provide only instance of binary tree instead of having to explicitly give the root.
    return Height(TreeClass.root)

print("The height of the tree is",PrintHeight(trees))
# End of extra credit question