#AVL Tree Class Definitions and Methods:

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return AVLNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if val < node.left.val:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance < -1:
            if val > node.right.val:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.get_min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        if not node:
            return node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

# Testing the AVL Tree methods
avl_tree = AVLTree()
values = [60, 80, -30, 19, 41, 76, 30, 6, 0, -1, 98, 94, 44, 85, 54, 47, 48, 49, 45, 75, 91]
for val in values:
    avl_tree.insert(val)

print("\nPre-Order Traversal of AVL Tree:")
avl_tree.preorder(avl_tree.root)
print("\n\nPost-Order Traversal of AVL Tree:")
avl_tree.postorder(avl_tree.root)

#Menu System for AVL Tree Application:
def avl_main_menu():
    avl_tree = AVLTree()
    while True:
        print("\nAVL Tree Menu:")
        print("1. Insert a value into AVL Tree")
        print("2. Delete a value from AVL Tree")
        print("3. Print Pre-Order Traversal")
        print("4. Print Post-Order Traversal")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            val = int(input("Enter value to insert: "))
            avl_tree.insert(val)
        elif choice == 2:
            val = int(input("Enter value to delete: "))
            avl_tree.delete(val)
        elif choice == 3:
            print("Pre-Order Traversal:")
            avl_tree.preorder(avl_tree.root)
            print()
        elif choice == 4:
            print("Post-Order Traversal:")
            avl_tree.postorder(avl_tree.root)
            print()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    avl_main_menu()
