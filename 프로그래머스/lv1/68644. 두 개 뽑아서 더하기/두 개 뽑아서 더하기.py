def solution(numbers):
    answer = set()
    for i, a in enumerate(numbers):
        for b in numbers[i+1:]:
            if a+b not in answer:
                answer.add(a+b)
    return sorted(list(answer))
        