'''
Created on 2014-12-23

@author: Jonathan
'''

d = {}
def count_bit(n, k):
    if n == 1 and k == 0:
        return [1,1]
    if n == k:
        return [0,0]

    if k != 0:
        if d.has_key(str(n-1)+" " +str(k-1)):
            temp_0 = d[str(n-1)+" " +str(k-1)]
        else:
            temp_0 = count_bit(n-1,k-1)
            d[str(n-1)+" " +str(k-1)] = temp_0
        if d.has_key(str(n-1)+" " +str(k)):
            temp_1 = d[str(n-1)+" " +str(k)]
        else:
            temp_1 = count_bit(n-1,k) 
            d[str(n-1)+" " +str(k)] = temp_1
        return [temp_1[0]+temp_1[1], temp_0[1] + temp_1[0]]
    elif n != 1:
        if d.has_key(str(n-1)+" " +str(k)):
            temp = d[str(n-1)+" " +str(k)]
        else:
            temp = count_bit(n-1,k) 
            d[str(n-1)+" " +str(k)] = temp
        return [temp[0] + temp[1], temp[0]]

def solution(n, k):
    if n <= k:
        return 0
    return sum(count_bit(n,k))

N = int(raw_input())
for i in xrange(0, N):
    input = raw_input().split()
    print input[0] + " " + str(solution(int(input[1]), int(input[2])))


