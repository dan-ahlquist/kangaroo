import sys


def filter_thes(in_file, out_file):
    for line in in_file:
        toks = line.split(',')
        toks_stripped = [t.strip() for t in toks]
        if ' ' in toks_stripped[0]:
            continue
        no_compound = [w for w in toks_stripped if ' ' not in w]
        no_hyphen = [w for w in no_compound if '-' not in w]
        no_empty = [w for w in no_hyphen if len(w) > 0]
        if len(no_empty) > 1:
            out_file.write(','.join(no_empty) + '\n')


if __name__ == '__main__':
    filter_thes(open(sys.argv[1], 'r'), open(sys.argv[2], 'w'))
