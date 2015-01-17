'''
Created on 2014-12-29

@author: Jonathan
'''

'''
Brute force - TLE
'''
import numpy

def count_pattern_BF(text, pattern):
    if len(pattern) > len(text):
        return []
    pattern_loc = []
    for i in xrange(0, len(text) - len(pattern) + 1):
        if text[i: i+len(pattern)] == pattern:
            pattern_loc.append(str(i+1))
    return pattern_loc

'''
Rabin-Karp algorithm - TLE
''' 
def count_pattern_RK(text, pattern):
    if len(pattern) > len(text):
        return []
    pattern_loc = []
    pattern_hash = rolling_hash(pattern, len(pattern))[0]
    subStr_hash_list = rolling_hash(text, len(pattern))
    for i in xrange(0, len(text) - len(pattern) + 1):
        if subStr_hash_list[i] == pattern_hash:
            if text[i: i+len(pattern)] == pattern:
                pattern_loc.append(str(i+1))
    return pattern_loc

def rolling_hash(text, sub_str_len):
    prime_base = 101
    hash_val_list = []
    hash_val = 0
    for i in xrange(0, sub_str_len):
        hash_val += ord(text[i]) * prime_base ** (sub_str_len - 1 - i)
    hash_val_list.append(hash_val)
    for i in xrange(1, len(text) - sub_str_len + 1):
        hash_val = (prime_base * (hash_val - (ord(text[i-1]) * prime_base ** (sub_str_len-1)))) \
            + ord(text[i+sub_str_len-1])
        hash_val_list.append(hash_val)
    return hash_val_list

'''
Knuth Morris Pratt - TLE
'''
def count_pattern_KMP(text, pattern):
    m = 0
    i = 0
    if len(pattern) > len(text):
        return []
    prefix = prefix_list(pattern)
    pattern_loc = []
    while m + i < len(text):
        if pattern[i] == text[m+i]:
            if i + 1 == len(pattern):
                pattern_loc.append(str(m + 1))
                i = 0
                m += 1
            i += 1
        else:
            if prefix[i] > -1:
                m = m + i - prefix[i]
                i = prefix[i]
            else:
                i = 0
                m += 1    
    return pattern_loc

def prefix_list(pattern):
    prefix = [-1, 0]
    i = 0
    j = 1
    while j < len(pattern) - 1:
        if pattern[i] == pattern[j]:
            prefix.append(prefix[-1]+1)
            i += 1
        else:
            i = 0
            if pattern[i] == pattern[j]:
                prefix.append(1)
                i += 1
            else:
                prefix.append(0)
        j += 1
    
    return prefix

if __name__ == '__main__':
    N = int(raw_input())
    for i in xrange(0, N):
        input = raw_input().split()
        pattern_loc = count_pattern_KMP(input[0], input[1])
        if len(pattern_loc) == 0:
            print "Not Found"
        else:
            print len(pattern_loc)
            print " ".join(pattern_loc)
            print ""