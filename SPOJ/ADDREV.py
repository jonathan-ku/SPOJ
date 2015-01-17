'''
Created on 2014-12-20

@author: Jonathan
'''
def add_reverse(x, y):
    x = list(x)
    y = list(y)
    x.reverse()
    y.reverse()
    x_reverse = "".join(x)
    y_reverse = "".join(y)
    z = list(str(int(x_reverse) + int(y_reverse)))
    z.reverse()
    return int("".join(z))
    
if __name__ == '__main__':
    N = int(raw_input())
    out = []
    for i in xrange(0,N):
        num = raw_input().split()
        out.append(add_reverse(num[0], num[1]))
    for o in out:
        print o