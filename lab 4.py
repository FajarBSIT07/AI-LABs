"""Lab 4 - Stack, Queue and Binary Search in Python"""
# ---------------------------------------------------------------
# Question 1: Stack (LIFO - Last In, First Out)
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack :", self.items)


# EXMAPLE: Stack
print("=== Question 1: Stack ===")
s = Stack()
for x in (10, 20, 30):
    s.push(x)
s.display()
print("Peek:", s.peek())
print("Popped:", s.pop())
s.display()
print("Size:", s.size(), "| Empty?", s.is_empty())


# ---------------------------------------------------------------
# Question 2: Queue (FIFO - First In, First Out)
# ---------------------------------------------------------------
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: cannot dequeue from an empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue (front -> rear):", self.items)


# Example: Queue
print("\n=== Question 2: Queue ===")
q = Queue()
for x in (10, 20, 30):
    q.enqueue(x)
q.display()
print("Front:", q.front())
print("Dequeued:", q.dequeue())
q.display()
print("Size:", q.size(), "| Empty?", q.is_empty())


# ---------------------------------------------------------------
# Question 3: Binary Search (array must be sorted)
# ---------------------------------------------------------------
def binary_search(arr, target, show_steps=False):
    low, high = 0, len(arr) - 1
    step = 1
    while low <= high:
        mid = (low + high) // 2
        if show_steps:
            print(f"#{step}  Low={low}  High={high}  Mid={mid}  (arr[mid]={arr[mid]})")
        if arr[mid] == target:
            return mid                  # found
        elif arr[mid] < target:
            low = mid + 1              
        else:
            high = mid - 1              
        step += 1
    return -1                           # not found


# Example: Binary Search
print("\n=== Question 3: Binary Search ===")
numbers = [6, 12, 17, 23, 38, 45, 77, 84, 90]
target = 83
result = binary_search(numbers, target, show_steps=True)
if result != -1:
    print(f"Successful Search!! {target} found at index {result}")
else:
    print(f"{target} not found in the array")
