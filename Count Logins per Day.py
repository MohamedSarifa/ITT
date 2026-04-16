from datetime import datetime
from collections import Counter
logins = ["2026-03-10 10:00", "2026-03-10 12:00", "2026-03-11 09:30"]
days = [log.split()[0] for log in logins]
print(Counter(days))
