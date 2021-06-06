# Balanced Parenthesis problem.[Imp]
# Can be done with or without stack


# Without Stack
def findClosing(c):
    if  c == '(':
        return ')'
    elif c == '{':
        return '}'
    elif c == '[':
        return ']'
    return -1

# function to check if paranthesis are balanced
def check(expn, n):
    
    # Base case
    if n == 0:
        return True

    if n == 1:
        return False

    if expn[0] == ')' or expn[0] == '}' or expn[0] == ']':
        return False

    # Search for closing bracket for first opening bracket
    closing = findClosing(expn[0])

    # count is used to handle cases like "((()))"
    # We basically need to consider matching closing bracket
    i = -1
    count = 0
    for i in range(1, n):
        if expn[i] == expn[0]:
            count += 1
        if expn[i] == closing:
            if count == 0:
                break
            count -= 1

    # if we did not find a closing bracket
    if i ==n:
        return False
    

    # If closing bracket was next to open
    if i == 1:
        return check(expn[2:], n - 2)

    # If closing bracket was somewhere in the middle
    return check(expn[1:], i -1) and check(expn[i + 1:], n - i - 1)


# Driver Code
expn = "[(])"
n = len(expn)
if check(expn, n):
    print("Balanced")
else:
    print("Not Balanced")

eexp = "[()]{}{[()()]()}"
n1 = len(eexp)
if check(eexp, n1):
    print("Balanced")
else:
    print("Not Balanced")


#=============================================================================
# Using Stack
def check1(expn):
    stack = []

    # Traversing the expression
    for char in expr:
        if char in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(char)
        else:
            # If current character is not opening bracket, then it must be closing.
            # So stack cannot be empty at this point
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != '}':
                    return False
    # Check empty estack
    if stack:
        return False
    return True

# Driver Code
expr = "{()}[]"
 
# Function call
if check1(expr):
    print("Balanced")
else:
    print("Not Balanced")