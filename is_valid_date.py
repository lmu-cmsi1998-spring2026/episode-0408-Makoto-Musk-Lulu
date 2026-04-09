from days_in_month import days_in_month

# Misk version
def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False
    if day not in range(1, days_in_month(year, month) + 1):
        return False
    return True
