from datetime import datetime
dates = ["2026-03-10", "2025-01-01", "2026-05-20"]
oldest = min(dates, key=lambda d: datetime.strptime(d, "%Y-%m-%d"))
print(oldest)
