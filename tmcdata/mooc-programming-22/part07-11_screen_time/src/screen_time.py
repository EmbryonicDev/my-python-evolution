from datetime import datetime, timedelta


def get_date_format(date: str):
    return datetime.strftime(date, '%d.%m.%Y')


test = False
# for testing purposes
if test:
    filename = 'first_of_may.txt'
    start_date = '1.5.2020'
    day_count = 1

# get date from user input
else:
    filename = input('Filename: ')
    start_date = input('Starting date: ')
    day_count = int(input('How many days: '))
start_date = datetime.strptime(start_date, "%d.%m.%Y")
end_date = start_date + timedelta(days=day_count - 1)
print('Please type in screen time in minutes on each day (TV computer mobile):')

# define variables
total_minutes = 0
day = start_date
daily_data = {}

# get minutes for each day
for i in range(day_count):
    minutes = input(f"Screen time {get_date_format(day)}: ")

    # minutes to list
    minutes = minutes.split(' ')
    # minutes to integers
    for i in range(len(minutes)):
        minutes[i] = int(minutes[i])
    # date & minutes to dict
    daily_data[get_date_format(day)] = minutes

    total_minutes += sum(minutes)
    day += timedelta(days=1)

# write data to file
with open(filename, 'w') as file:
    file.write(
        f"Time period: {get_date_format(start_date)}-{get_date_format(end_date)}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {total_minutes/day_count:.1f}\n")
    for date, time in daily_data.items():
        file.write(f"{date}: {time[0]}/{time[1]}/{time[2]}\n")

print("Data stored in file late_june.txt")
