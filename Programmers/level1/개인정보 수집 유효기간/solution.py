def solution(today, terms, privacies):
    answer = []
    terms = {t.split()[0]: int(t.split()[1]) for t in terms}
    t_year, t_month, t_day = map(int, today.split("."))
    for i, p in enumerate(privacies):
        date, tmp = p.split()
        year, month, day = map(int, date.split("."))
        month += terms[tmp]
        day -= 1
        if day == 0:
            day = 28
            month -= 1
        if month > 12:
            if month % 12 == 0:
                year += (month // 12) - 1
                month = 12
            else:
                year += (month // 12)
                month = month % 12
        if t_year > year or (t_year == year and t_month > month) or(t_year == year and t_month == month and t_day > day):
            answer.append(i+1)
    return answer
