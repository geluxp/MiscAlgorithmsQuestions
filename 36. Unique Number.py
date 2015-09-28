#36.     Unique Number
#Write, efficient code for extracting uniqueelements from a sorted list of array.
#e.g. (1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9)-> (1, 3, 5, 9).


a=[1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9]
def solution(a):
    b=set(a)
    a=list(b)
    return a

print solution(a)
