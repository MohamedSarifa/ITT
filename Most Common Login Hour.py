from datetime import datetime
from collections import Counter
logins = ["2026-03-10 10:00", "2026-03-10 10:30", "2026-03-11 10:00"]
hours = [datetime.strptime(log, "%Y-%m-%d %H:%M").strftime("%I %p") for log in logins]
print(Counter(hours).most_common(1))
