from datetime import datetime, timedelta
activities = [("User1", "2026-03-14 10:00"), ("User2", "2026-03-10 10:00")]
now = datetime.now()
active_users = [u for u, t in activities if now - datetime.strptime(t, "%Y-%m-%d %H:%M") < timedelta(hours=24)]
print(active_users)
