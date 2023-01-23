#!/opt/python

import os

def child():
    print(f"\nA new child with pid({os.getpid()})")
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        print(f"newpid: {newpid}")
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print(f"parent: {pids[0]}, child: {pids[1:]}")    
        reply = input("q for quilt / c for new fork\n")
        if reply == 'c':
            continue
        else:
            break

parent()
