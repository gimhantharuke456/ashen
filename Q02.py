#Class Definitions and Methods:
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inverse_inorder(self, node):
        if node:
            self.inverse_inorder(node.right)
            print(node.val, end=" ")
            self.inverse_inorder(node.left)

    def print_leaf_nodes(self, node):
        if node:
            if not node.left and not node.right:
                print(node.val, end=" ")
            else:
                self.print_leaf_nodes(node.left)
                self.print_leaf_nodes(node.right)

    def print_non_leaf_nodes(self, node):
        if node:
            if node.left or node.right:
                print(node.val, end=" ")
            self.print_non_leaf_nodes(node.left)
            self.print_non_leaf_nodes(node.right)

    def insert(self, val):
        if self.root is None:
            self.root = BSTNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = BSTNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = BSTNode(val)
            else:
                self._insert(node.right, val)

# Testing the BST methods
bst = BST()
values = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]
for val in values:
    bst.insert(val)

print("\nInverse In-Order Traversal of BST:")
bst.inverse_inorder(bst.root)
print("\n\nLeaf Nodes of BST:")
bst.print_leaf_nodes(bst.root)
print("\n\nNon-Leaf Nodes of BST:")
bst.print_non_leaf_nodes(bst.root)

#Menu System for BST Application:
def main_menu():
    bst = BST()
    while True:
        print("\nMenu:")
        print("1. Insert a value into BST")
        print("2. Print Inverse In-Order Traversal")
        print("3. Print Leaf Nodes")
        print("4. Print Non-Leaf Nodes")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            val = int(input("Enter value to insert: "))
            bst.insert(val)
        elif choice == 2:
            print("Inverse In-Order Traversal:")
            bst.inverse_inorder(bst.root)
            print()
        elif choice == 3:
            print("Leaf Nodes:")
            bst.print_leaf_nodes(bst.root)
            print()
        elif choice == 4:
            print("Non-Leaf Nodes:")
            bst.print_non_leaf_nodes(bst.root)
            print()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
