'''
Created on 2014-12-24

@author: Jonathan
'''


def to_RPN(expr):
    removed_all_bracket = False
    while (removed_all_bracket == False):
        if expr[0] == "(":
            counter = 0
            for i in xrange(0, len(expr)):
                if expr[i] == "(":
                    counter += 1
                if expr[i] == ")":
                    counter -= 1
                if counter == 0:
                    if i+1 >= len(expr):
                        expr = expr[1:len(expr)-1]
                    else:
                        removed_all_bracket = True
                        break
        else:
            removed_all_bracket = True
    counter = 0
    d = {}
    for i in xrange(0, len(expr)):
        if expr[i] == "(":
            counter += 1
        if expr[i] == ")":
            counter -= 1
        if counter == 0:
            if expr[i] == "+" or "-" or "*" or "/" or "^":
                d[expr[i]] = i
    if d.has_key("+"):
        i = d["+"]
    elif d.has_key("-"):
        i = d["-"]
    elif d.has_key("*"):
        i = d["*"]
    elif d.has_key("/"):
        i = d["/"]
    elif d.has_key("^"):
        i = d["^"]
    else:
        return expr
    left_rpn = to_RPN(expr[0:i])
    right_rpn = to_RPN(expr[i+1:])
    return left_rpn + right_rpn + expr[i]


N = int(raw_input())
for i in xrange(0, N):
    expr = raw_input()
    print to_RPN(expr)
