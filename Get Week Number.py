from datetime import datetime
dt = datetime.strptime("2026-03-10", "%Y-%m-%d")
print(dt.isocalendar()[1])
