'''
Created on 2014-12-28

@author: Jonathan
'''


def can_type(num_key, text):
    char_pos = {}
    inv_char_pos = {}
    max = 0
    curr = 0
    for i in xrange(0, len(text)):
        if text[i] in char_pos.keys():
            inv_char_pos.pop(char_pos[text[i]])
        char_pos[text[i]] = i
        inv_char_pos[i] = text[i]
        if (len(char_pos.keys()) > num_key):
            pos_to_remove = min(inv_char_pos.keys())
            char_pos.pop(inv_char_pos[pos_to_remove])
            inv_char_pos.pop(pos_to_remove)
            curr = i - pos_to_remove - 1
        curr += 1
        if (curr >= max):
            max = curr
    return max

if __name__ == '__main__':
    num_key = int(raw_input())
    while (num_key != 0):
        text = raw_input()
        print can_type(num_key, text)
        num_key = int(raw_input())
