'''
Created on 2014-12-20

@author: Jonathan
'''

def count_factor_of_five(max_factor):
    num_of_five = 0
    for i in xrange(0, max_factor):
        num_of_five = num_of_five * 5 + 1
    return num_of_five
    
def max_factor_of_five(number):
    for i in xrange(0,14): #number < 10^9
        if 5**i > number:
            return i-1
    return None

#count the total number of 5 in all number's factor
def count_zero(number):
    total_num_of_five = 0
    while(number >= 0):
        max_factor = max_factor_of_five(number)
        total_num_of_five += count_factor_of_five(max_factor)
        number -= 5 ** max_factor
    return total_num_of_five
        
if __name__ == '__main__':
    N = int(raw_input())
    toReturn = []
    for i in xrange(0, N):
        toReturn.append(count_zero(int(raw_input())))
        
    for r in toReturn:
        print r