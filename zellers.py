def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    K = year % 100
    J = year // 100
    h = (q + ((13*(m+1))//5) + K + (K//4) + (J//4) - (2*J)) % 7

    days_of_week = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days_of_week[h]

# Example usage
day =int(input('Enter the day'))
month =int(input('Enter the month'))
year = int(input('Enter the year'))
print(zellers_congruence(day, month, year))