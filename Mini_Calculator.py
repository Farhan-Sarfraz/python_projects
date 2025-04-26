def is_oper(token):
    return token in ['+','-','*','/','^']

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_oper(token):
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix):
    stack =[]

    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
    return stack[0]

def calc():
    print("CREATING MINI CALCULATOR.")
    print("Mini calculator (infix to postfix)")
    print("space between number or operator . e.g. , (3 + 4) * 2")
    expr = input("enter the infix expression:")
    postfix = infix_to_postfix(expr)
    result = evaluate_postfix(postfix)
    print("postfix expression :", ' '.join(postfix))
    print("results:",result)

if __name__ == "__main__":
    calc()



