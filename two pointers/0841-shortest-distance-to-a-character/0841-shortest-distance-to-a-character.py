class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a, n = [], len(s)
        output = []

        # 특정원소 일단 싹 찾고 배열a에 위치 넣기
        for i in range(n):
                if s[i] == c:
                        a.append(i)


        # 2 pointer
        j = 0
        for i in range(n):
                if s[i] == c:
                        output.append(0)
                        j += 1
                elif i < a[0]:      # 첫번째 c보다 앞에 있는 원소들
                        output.append(a[0] - i)
                elif i > a[-1]:     # 마지막 c보다 뒤에 있는 원소들
                        output.append(i-a[-1])
                else:
                        output.append(min((i-a[j-1]), (a[j] - i)))

        return output
        
