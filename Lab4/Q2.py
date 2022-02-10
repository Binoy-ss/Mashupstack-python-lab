import datetime

current_date = datetime.date.today()

sub_days = datetime.timedelta(5)

answer = current_date-sub_days

print("5days before from  current date",answer)