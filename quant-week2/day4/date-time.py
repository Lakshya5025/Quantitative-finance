from datetime import datetime, timedelta

now = datetime.now()
week_later = now + timedelta(days=7)
iso = now.isoformat()
parsed = datetime.fromisoformat(iso)
print(now)
print(week_later)
print(iso)
print(parsed)
