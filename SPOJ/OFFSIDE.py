'''
Created on 2014-12-23

@author: Jonathan
'''

if __name__ == '__main__':
    while (raw_input() != "0 0"):
        A = map(int, raw_input().split())
        D = map(int, raw_input().split())
        D_sorted = sorted(D)
        att_pos = min(A)
        def_pos = D_sorted[1]
        if att_pos < def_pos :
            print "Y"
        else:
            print "N"