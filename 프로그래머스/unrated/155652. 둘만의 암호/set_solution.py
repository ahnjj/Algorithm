# 무작정 간단하게 바로 풀이하지 말고 알고리즘 처음 짤때 자료구조 잘 선택하기
def solution(s, skip, index):
  new = ''
  from string import ascii_lowercase
  
  a_to_z = set(ascii_lowercase)
  a_to_z -= set(skip)
  a_to_z = sorted(a_to_z) 
  l = len(a_to_z)
  
  dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}
  
  for c in s:
      new += a_to_z[(dic_alpha[c] + index) % l]
  
  return new
