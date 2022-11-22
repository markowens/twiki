# -*- coding: utf-8 -*-
import sys
from itertools import permutations


def check_wrong_position(x, bad_pos):
    res = True
    for i in range(5):
        if len(bad_pos) == 0:
            continue
        for c in bad_pos[i]:
            if x[i] == c:
                return False
    return res

def check_known_positions(x, good_pos):
    res = True
    for i in range(5):
        if len(good_pos[i]) == 0:
            continue
        for c in good_pos[i]:
            if x[i] != c:
                return False   
    return res

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    if num_args < 3:
        print("Usage: python words2.py letters unused_letter bad_postions good_pos")
        sys.exit(1)
        
    bad_pos = args[2:7]        
    good_pos = args[7:]
    # print(bad_pos)
    # print(good_pos)
        
    letters = []
    for arg in args[0]:
        letters.append(arg)
  
    perm = permutations(list(letters))
    for i in perm:
        word = "".join(i)
        for c in args[1]:
            if c in word:
                continue
        if not check_wrong_position(word, bad_pos):
            # print(f"skip: {word}")
            continue
        if not check_known_positions(word, good_pos):
            continue
        print(f"{word:7s} - {args[1]}")
         