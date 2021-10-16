import sys


def contains(a, b):
    if len(a) == len(b):
        return False
    parent = max(a, b, key=len)
    child = min(a, b, key=len)
    i, j = 0, 0
    while i < len(parent) and j < len(child):
        if parent[i] == child[j]:
            j += 1
        i += 1
    return j == len(child)


def find_joeys(line):
    result = []
    toks = line.split(',')
    toks_stripped = [t.strip() for t in toks]
    parent = toks_stripped[0]
    for tok in toks_stripped[1:]:
        if contains(parent, tok):
            result.append(tok)
    return result


def search(in_file, out_file):
    for line in in_file:
        roos = find_joeys(line)
        if roos:
            parent = line.split(',')[0]
            out_list = [parent] + roos
            out_line = ','.join(out_list) + '\n'
            out_file.write(out_line)


if __name__ == '__main__':
    search(open(sys.argv[1], 'r'), open(sys.argv[2], 'w'))
