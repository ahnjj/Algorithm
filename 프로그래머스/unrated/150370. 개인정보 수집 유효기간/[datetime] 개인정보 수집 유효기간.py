def solution(today, terms, privacies):
    from datetime import datetime 
    from dateutil.relativedelta import relativedelta # 월 계산 할 때는 relativedelta
    answer = []

    today = datetime.strptime(today, '%Y.%m.%d') # string -> datetime 할 때는 strptime

    # terms -> dict 
    terms_dict = {}
    for i in terms:
        terms_dict[i.split()[0]] = i.split()[1]

    # pravacies
    for num, user in enumerate(privacies):
        term_type = user.split()[1] # user의 계약 종류
        term_len = int(terms_dict[term_type]) # user의 유효기간

        start = datetime.strptime(user.split()[0],'%Y.%m.%d') # 계약날짜
        expire = start + relativedelta(months = term_len) # 파기날짜

        # expire인지 체크
        if today >= expire: # datetime 끼리는 크기비교 가능
            answer.append(num+1)
    return answer
