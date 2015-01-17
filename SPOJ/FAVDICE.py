'''
Created on 2014-12-23

@author: Jonathan
'''

'''
sum all the expected waiting time of new numbers
'''
def calc_exp(n):
    num_throw = 1.0
    temp_n = n
    while temp_n > 1:
        num_throw += n / (temp_n-1)
        temp_n -= 1
        
    return num_throw
            
if __name__ == '__main__':

    N = int(raw_input())
    toReturn = []
    for i in xrange(0,N):
        toReturn.append(calc_exp(float(raw_input())))
    
    for p in toReturn:
        print("%.2f" % p)
