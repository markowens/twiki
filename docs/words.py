# -*- coding: utf-8 -*-




known = ["", "r", "i", "", ""]

bad_pos = ["", "", "e", "eir", ""]

in_word = "rie"

not_in_word = "audostn"

def check_known_positions(x):
    res = True
    for i in range(5):
        if len(known[i]) == 0:
            continue
        for c in known[i]:
            if x[i] != c:
                return False   
    return res

def check_wrong_position(x):
    res = True
    for i in range(5):
        if len(bad_pos) == 0:
            continue
        for c in bad_pos[i]:
            if x[i] == c:
                return False
    return res

def check_in_word(x):
    res = True
    for c in in_word:
        if c not in x:
            return False
    return res

def check_not_in_word(x):
    res = True
    for c in not_in_word:
        if c in x:
            return False
    return res


with open("/home/mark/Documents/words.txt", "r") as f:
    cnt = 0
    for line in f:
        x = line.rstrip()
        
        # known positions
        res = check_known_positions(x)
        if res == False:            
            continue
        
        # good letters, bad position
        res = check_wrong_position(x)
        if res == False:
            continue

        # letters must be in
        res = check_in_word(x)
        if res == False:
            continue
        
        # not in word
        res = check_not_in_word(x)
        if res == False:
            continue
            
        cnt += 1
        print(x)
    print(f"Found {cnt} possibilities")
    
        

            
            


