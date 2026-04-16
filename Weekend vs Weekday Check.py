from datetime import datetime
dt = datetime.strptime("2026-03-14", "%Y-%m-%d")
print("Weekend" if dt.weekday() >= 5 else "Weekday")
