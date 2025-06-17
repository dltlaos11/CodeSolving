def solution(today, terms, privacies):
    terms_dict = {term.split()[0]: int(term.split()[1]) for term in terms}
    
    def add_months_and_subtract_day(date_str, months):
        year, month, day = map(int, date_str.split('.'))
        
        # 0-based로 변환 → 계산 → 1-based로 복원
        month += months
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1
        
        day -= 1
        if day == 0:
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            day = 28
        
        return f"{year:04d}.{month:02d}.{day:02d}"
    
    today_formatted = today
    expired = []
    
    for i, privacy in enumerate(privacies):
        collected_date, term_type = privacy.split()
        expire_date = add_months_and_subtract_day(collected_date, terms_dict[term_type])
        
        if today_formatted > expire_date:
            expired.append(i + 1)
    
    return expired