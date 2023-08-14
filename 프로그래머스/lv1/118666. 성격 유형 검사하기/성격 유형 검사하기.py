def solution(survey, choices):
    result = ''
    type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for idx, scores in enumerate(choices):
        if scores == 1:
            type[survey[idx][0]] += 3
        elif scores == 2:
            type[survey[idx][0]] += 2
        elif scores == 3:
            type[survey[idx][0]] += 1
        elif scores == 5:
            type[survey[idx][1]] += 1
        elif scores == 6:
            type[survey[idx][1]] += 2
        elif scores == 7:
            type[survey[idx][1]] += 3

    if type['R'] >= type['T']:
        result += 'R'
    elif type['R'] < type['T']:
        result += 'T'

    if type['C'] >= type['F']:
        result += 'C'
    elif type['C'] < type['F']:
        result += 'F'

    if type['J'] >= type['M']:
        result += 'J'
    elif type['J'] < type['M']:
        result += 'M'

    if type['A'] >= type['N']:
        result += 'A'
    elif type['A'] < type['N']:
        result += 'N'
    return result