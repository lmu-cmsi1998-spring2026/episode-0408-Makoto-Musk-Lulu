from days_in_month import days_in_month


# Misk version
#my version
# Makoto version
def is_valid_date(year, month, day):
    if month not in range(1, 13):
        return False
    if day < 1:
        return False
    return day <= days_in_month(year, month)from days_in_month import days_in_month




