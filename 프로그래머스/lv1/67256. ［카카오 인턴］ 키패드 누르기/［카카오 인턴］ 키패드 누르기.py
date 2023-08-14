def solution(numbers, hand):
    L_cur, R_cur = -1, -1
    result =''

    L = {1:{2:1, 5:2, 8:3, 0:4},
         4:{2:2, 5:1, 8:2, 0:3},
         7:{2:3, 5:2, 8:1, 0:2},
         2:{2:0, 5:1, 8:2, 0:3},
         5:{2:1, 5:0, 8:1, 0:2},
         8:{2:2, 5:1, 8:0, 0:1},
         0:{2:3, 5:2, 8:1, 0:0},
         -1:{2:4, 5:3, 8:2, 0:1}}
    R = {3:{2:1, 5:2, 8:3, 0:4},
         6:{2:2, 5:1, 8:2, 0:3},
         9:{2:3, 5:2, 8:1, 0:2},
         2:{2:0, 5:1, 8:2, 0:3},
         5:{2:1, 5:0, 8:1, 0:2},
         8:{2:2, 5:1, 8:0, 0:1},
         0:{2:3, 5:2, 8:1, 0:0},
         -1:{2:4, 5:3, 8:2, 0:1}}

    for i in numbers:
        if i in (1,4,7):
            L_cur = i
            result += "L"
        elif i in (3,6,9):
            R_cur = i
            result += "R"
        elif i in (2,5,8,0):
            if L[L_cur][i] > R[R_cur][i]:
                R_cur = i
                result += "R"
            elif L[L_cur][i] < R[R_cur][i]:
                L_cur = i
                result += "L" 
            elif L[L_cur][i] == R[R_cur][i]:
                if hand == 'left':
                    L_cur = i
                    result += "L"   
                else:
                    R_cur = i
                    result += "R"

    return result