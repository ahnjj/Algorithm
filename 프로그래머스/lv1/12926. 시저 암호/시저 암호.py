def solution(s, n):
    numbers = [ord(i) for i in s]
    for i in range(len(numbers)):
        if numbers[i] == 32:
            numbers[i] = numbers[i]
        elif (numbers[i] <= 90 and numbers[i] + n > 90) or (numbers[i] >= 97 and numbers[i] + n > 122):
            numbers[i] = numbers[i] + n - 26
        else: numbers[i] = numbers[i] + n 

    return ''.join(chr(i) for i in numbers)