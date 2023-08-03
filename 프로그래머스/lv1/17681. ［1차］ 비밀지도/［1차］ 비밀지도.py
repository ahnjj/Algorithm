def solution(n, arr1, arr2):
    
    new = [bin(x | y).lstrip('0b').replace('1','#').replace('0',' ') for x,y in zip(arr1, arr2)]

    return [' '*(n-len(i))+i if len(i)<n else i for i in new]

