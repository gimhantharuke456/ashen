#Balanced BST Algorithm:
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def create_balanced_bst(arr):
    if not arr:
        return None
    arr.sort()
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = create_balanced_bst(arr[:mid])
    root.right = create_balanced_bst(arr[mid+1:])
    return root

# Function to print the BST (In-Order Traversal)
def print_in_order(node):
    if not node:
        return
    print_in_order(node.left)
    print(node.val, end=" ")
    print_in_order(node.right)

# Test with given dataset
arr = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]
balanced_bst = create_balanced_bst(arr)
print("In-Order Traversal of Balanced BST:")
print_in_order(balanced_bst)

#Complete BST Algorithm:
def create_complete_bst(arr):
    if not arr:
        return None
    root = Node(arr[0])
    node_queue = [root]
    value_queue = arr[1:]
    while value_queue:
        curr_node = node_queue.pop(0)
        if value_queue:
            curr_node.left = Node(value_queue.pop(0))
            node_queue.append(curr_node.left)
        if value_queue:
            curr_node.right = Node(value_queue.pop(0))
            node_queue.append(curr_node.right)
    return root

# Test with another dataset
arr = [45, -8, 21, 34, 55, 65, 9, 14, 0, 18, 90, 46, 49, 82, 84, 99, 80, 132, 57, 66]
complete_bst = create_complete_bst(arr)
print("\nIn-Order Traversal of Complete BST:")
print_in_order(complete_bst)
