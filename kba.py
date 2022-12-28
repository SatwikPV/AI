##################################InfixToPostFix#####################################################
def infixToPostfix(arr):
    stack = []
    finarr = []
    for i in arr:
        if i == '(':
            stack.append(i)
        
        elif i == ')':
            #while stack isnt empty keep on popping
            while len(stack) != 0 and stack[-1] != '(':
                a = stack.pop()
                finarr.append(a)

            if len(stack) != 0 and stack[-1] != '(':
                return -1
                
            else:
                stack.pop()

        else:
            while(len(stack)!=0):
                #compare the top two elements, if the top element is of lesser priority, then push it back
                top = stack.pop()
                if priority[top] > priority[stack[-1]]:
                    finarr.append(stack.pop)

                else:
                    stack.push(top)

    return finarr

##################################End of InfixToPostfix code###############################################


############################################Postfix eval###################################################
def booleval(symbol1, symbol2, i):
    if i == 'v':
        return bool(symbol1) and bool(symbol2)
    if i == '^':
        return bool(symbol1) or bool(symbol2)


def posteval(arr):
    stack = []
    for i in exp:   
        if i.isdigit():
            stack.push(i)
        else:   
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(str(booleval(val1,val2, i)))
            return stack.pop()
#######################################End of Postfix Eval#####################################################


#compute the result
def baseresult(expr):
    i = 0
    print(infixToPostfix(expr))
    posteval(expr)

    return

#input the expression for KB
exp = input("Enter the expression for KB\n")

#split the expression into list items
exp = exp.split()

#printing the list to check 
print(exp)

#the input
combinations = [(True, True, True), (True, False, True), (False, True, False)]
priority = {'v': 1, '^': 2, '~': 3}

#take the query input
query = input("Enter the query")
query = query.split()

#taking out all the ~'s
for i in range(exp):
    if exp[i] == '~':
         exp.pop(i)

#feed the knowledge base
baseresult(exp)