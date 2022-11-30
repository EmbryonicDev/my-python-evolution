from datetime import datetime, timedelta

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

birthdate = datetime(year, month, day)
new_millennium = datetime(1999, 12, 31)

if new_millennium > birthdate:
    days_old = new_millennium - birthdate
    print(
        f"You were {days_old.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")
