from datetime import *

current_date = date.today()

for i in range(-1, 2):
    new_date = current_date + timedelta(days=i)
    print(new_date)
