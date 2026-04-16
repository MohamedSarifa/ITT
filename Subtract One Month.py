from datetime import datetime
from dateutil.relativedelta import relativedelta # Requires pip install python-dateutil
dt = datetime(2026, 3, 10)
print(dt - relativedelta(months=1))
