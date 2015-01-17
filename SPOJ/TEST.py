'''
Created on 2014-12-20

@author: Jonathan
'''

if __name__ == '__main__':
    output = []
    input = raw_input()
    while (input != "42"):
        output.append(input)
        input = raw_input()
    for o in output:
        print(o)
    