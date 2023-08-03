def solution(n, arr1, arr2):
    # bin -> list

    arr1 = [bin(i).lstrip('0b') for i in arr1]
    arr2 = [bin(i).lstrip('0b') for i in arr2]

    # 만약 bin 숫자 수가 n보다 작으면 0으로 채운다.
    arr1 = ['0'*(n-len(i))+i if len(i)<n else i for i in arr1]
    arr2 = ['0'*(n-len(i))+i if len(i)<n else i for i in arr2]

    # zip
    new = []
    for i in range(n):
        new.append(''.join('#' if int(j[0]) or int(j[1]) else ' ' for j in zip(arr1[i],arr2[i])))

    return new
