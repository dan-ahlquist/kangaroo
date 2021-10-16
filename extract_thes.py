import sys
from enum import Enum


class LineType(Enum):
    HEADING = 1
    BODY = 2


def get_line_type(line):
    if line[0] == '(':
        return LineType.BODY
    else:
        return LineType.HEADING


def extract(in_file, out_file):
    curr_entry = []
    for line in in_file:
        line_type = get_line_type(line)
        if line_type == LineType.HEADING:
            if len(curr_entry) > 0:
                out_file.write(','.join(curr_entry) + '\n')
            curr_entry = [line.split(sep='|')[0]]
        elif line_type == LineType.BODY:
            words = line.split(sep='|')
            words_stripped = [w.strip() for w in words]
            words_no_blank = [w for w in words_stripped if len(w) > 0]
            curr_entry += words_no_blank[1:]
    out_file.write(','.join(curr_entry) + '\n')


if __name__ == "__main__":
    in_file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    extract(in_file, out_file)
