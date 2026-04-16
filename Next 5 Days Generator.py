from datetime import datetime, timedelta
for i in range(1, 6):
    print((datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"))
