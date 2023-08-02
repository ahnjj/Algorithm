def solution(number):
    cnt = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for x in range(j+1,len(number)):
                if -(number[i] + number[j]) == number[x]:
                    cnt += 1

    return cnt