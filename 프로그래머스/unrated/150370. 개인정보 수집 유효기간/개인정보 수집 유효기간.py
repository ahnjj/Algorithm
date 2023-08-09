def solution(today, terms, privacies):
    from datetime import datetime 
    from dateutil.relativedelta import relativedelta
    answer = []

    today = datetime.strptime(today, '%Y.%m.%d')

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
        if today >= expire:
            answer.append(num+1)
    return answer