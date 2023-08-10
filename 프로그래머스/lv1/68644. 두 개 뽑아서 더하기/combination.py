from itertools import combinations
def solution(numbers):
  c = combinations(numbers,2)
  answer = set()
  for a,b in c:
      if a+b not in answer:
          answer.add(a+b)
  return answer
