import functools
def compare(a,b):
    cmp1 = str(a)+str(b)
    cmp2 = str(b)+str(a)
    return (int(cmp1) > int(cmp2)) - (int(cmp1) < int(cmp2))
def solution(numbers):
    sorted_nums = sorted(numbers, key=functools.cmp_to_key(lambda a, b: compare(a,b)),reverse=True)
    
    answer = "".join(str(x) for x in sorted_nums)
    return "0" if int(answer) == 0 else answer