from datetime import datetime
date1 = datetime(2024, 2, 14, 12, 0, 0)
date2 = datetime(2024, 2, 15, 12, 0, 0)
difference_in_seconds = (date2 - date1).total_seconds()

print(difference_in_seconds)
