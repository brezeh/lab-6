#lab 6 breze hoawrd

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data # Store the data for the node
        self.next = None # Initialize the next pointer to None (no next node yet)

# Create individual nodes with data values
node1 = Node(10) # First node with data 10
node2 = Node(20) # Second node with data 20
node3 = Node(30) # Third node with data 30

# Link the nodes together to form a chain (a simple linked list)
node1.next = node2 # Link node1 to node2
node2.next = node3 # Link node2 to node3

# Function to traverse the list and print each node's data
def print_linked_list(head):
    current = head # Start with the head node
    while current: # Continue until reach the end of the list (None)
        print(current.data, end= "->") # Print the data and follow with "->"
        current = current.next # Move to the next node in the list
    print('none') # Indicate the end of the list

# Test the print function by printing the linked list from node1
print('original linked list: ')
print_linked_list(node1)

# Exercise 1: Update node2's data and print the list again
node2.data = 25 # Change data in the second node
print('\nlinked list after updating nodes data: ')
print_linked_list(node1) # Print the list again to see the change

# Exercise 2: Add a new node (node4) with a new value and link it to the list
node4 = Node(40) # Create a new fourth node with data 40
node3.next = node4 # Link node3 to the new node4
print('\nLinked list after adding node4: ')
print_linked_list(node1)  # Print the updated list

# Exercise 3: Modify the print function to count nodes and print the count
def print_linked_list_with_count(head):
    current = head # Start with the head node
    count = 0 # Initialize a counter for the nodes
    while current: # Traverse until the end of the list
        print(current.data, end= "->") # Print the data for each node
        current = current.next # Move to the next node
        count += 1 # Increment the count for each node visited
    print('none') # Indicate the end of the list
    print(f"total node count: {count}") # Print the total node count

# Test the new function to print the list and count nodes
print('\nLinked list with node count: ')
print_linked_list_with_count(node1)  # Print the list and count nodes