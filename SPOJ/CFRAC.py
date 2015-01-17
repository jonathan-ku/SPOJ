'''
Created on 2014-12-29

@author: Jonathan
'''

def draw_fraction(p, q):
    whole = int(p/q)
    if whole == float(p)/q:
        graph = []
        whole -= 1
        len_whole = len(str(whole))
        graph.append("." * (len_whole + 3) + "1")
        graph.append( str(whole) + ".+.-")
        graph.append("." * (len_whole + 3) + "1")
        return graph
    p = p - whole * q
    sub_graph = draw_fraction(q, p)
    graph = []
    len_whole = len(str(whole))
    len_denom = len(sub_graph[0])
    len_nume_right = len_denom / 2
    if len_denom%2 == 0:
        len_nume_left = len_nume_right - 1
    else:
        len_nume_left = len_nume_right
    graph.append("." * (len_whole + 3 + len_nume_left) + "1" + "." * len_nume_right)
    graph.append(str(whole) + ".+." + "-" * len(sub_graph[0]))
    for i in sub_graph:
        temp_line = "." * (len_whole + 3) + i
        graph.append(temp_line)
    return graph

if __name__ == '__main__':
    p_q = raw_input()
    counter = 1
    while (p_q != "0 0"):
        p = int(p_q.split()[0])
        q = int(p_q.split()[1])
        print "Case %d:" %counter
        print "%d / %d" %(p, q)
        graph = draw_fraction(p, q)
        for line in graph:
            print line 
        counter += 1
        p_q = raw_input()