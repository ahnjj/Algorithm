def solution(array, commands):
    ans = []

    for i,j,k in commands:
        if j > len(array):
            ans.append(sorted(array[i-1:])[k-1])
        else:
            ans.append(sorted(array[i-1:j])[k-1])
    return ans