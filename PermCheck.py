# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    l=len(A)
    f=0
    for i in range (0,l):
        if(A[i]-1 != i):
            f=1
            break
    if(f==1):
        return 0
    else:
        return 1