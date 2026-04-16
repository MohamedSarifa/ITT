from datetime import datetime
t1 = datetime.strptime("2026-03-10 10:00:00", "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime("2026-03-10 12:30:00", "%Y-%m-%d %H:%M:%S")
print((t2 - t1).total_seconds())
