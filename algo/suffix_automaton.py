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
    """Get the length of the longest common substring of given strings
    :param s: first iterable(string or list of strings)
    :param t: second iterable
    :return: length of the longest common substring
    """
    a = Automaton(s)
    cur = a.t0
    current_length = 0
    max_length = 0

    for i in t:
        while i not in cur.trans:
            cur = cur.link
            if cur is None:
                break
            current_length = cur.length
        if cur is None:
            current_length = 0
            cur = a.t0
            continue
        cur = cur.trans[i]
        current_length += 1
        max_length = max(current_length, max_length)
    return max_length
