from copy import deepcopy


class Node:
    def __init__(self, length, link):
        self.trans = {}
        self.length = length
        self.link = link


class Automaton:
    def __init__(self, s):
        self.t0 = Node(0, None)
        last = self.t0
        for ind, c in enumerate(s):
            cur = Node(ind + 1, None)
            while last is not None and c not in last.trans:
                last.trans[c] = cur
                last = last.link
            if last is None:
                cur.link = self.t0
            elif last.trans[c].length == last.length + 1:
                cur.link = last.trans[c]
            else:
                nxt = last.trans[c]
                cl = Node(last.length + 1, nxt.link)
                cl.trans = deepcopy(nxt.trans)
                while (last is not None
                       and c in last.trans
                       and last.trans[c] is nxt):
                    last.trans[c] = cl
                    last = last.link
                cur.link = cl
                nxt.link = cl
            last = cur


def longest_common_substring(s, t):
    """Get the longest common substring of given strings
    :param s: first iterable(string or list of strings)
    :param t: second iterable
    """
    a = Automaton(s)
    current_node = a.t0
    current_length = 0
    max_length = 0
    max_end_ind = 0

    for ind, c in enumerate(t):
        while c not in current_node.trans:
            current_node = current_node.link
            if current_node is None:
                break
            current_length = current_node.length
        if current_node is None:
            current_length = 0
            current_node = a.t0
            continue
        current_node = current_node.trans[c]
        current_length += 1
        if max_length < current_length:
            max_length = current_length
            max_end_ind = ind
    return t[max_end_ind - max_length + 1: max_end_ind + 1]
