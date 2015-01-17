'''
Created on 2014-12-20

@author: Jonathan
'''
def simp_div(n, x, y):
    return [str(i) for i in range(x, n, x) if i%y !=0]
    
if __name__ == '__main__':
    N = int(raw_input())
    toPrint = []
    
    for i in xrange(0,N):
        input = raw_input().split()
        n = int(input[0])
        x = int(input[1])
        y = int(input[2])
        toPrint.append(simp_div(n,x,y))
    
    
    for p in toPrint:
        print " ".join(p)