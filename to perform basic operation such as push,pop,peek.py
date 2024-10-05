'''To perform basic operations such as push(), pop() and peek() in stack using Arrays'''

def push(stk, item):
    if item % 5 == 0:
        stk.append(item)
        print(item,"has been added to the stack")
    else:
        print("Item is not divisible by 5")

def pop(stk):
    if stk == []:
        print("Stack is empty")
    else:
        print(stk.pop(), "has been removed")

def peek(stk):
    if stk != []:
        print("Top of the stack is:", stk[-1])
    else:
        print("Stack is empty")

# Predefined stack
stk = [1, 2, 3, 4, 5]

while True:
    print('''\n1. PUSH
2. POP
3. PEEK
4. EXIT''')
    
    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = int(input("Enter a number to push: "))
        push(stk, item)
    elif ch == 2:
        pop(stk)
    elif ch == 3:
        peek(stk)
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Please enter a valid choice (1-4)")

    print("Current stack:", stk)

        
