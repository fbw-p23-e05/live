from datetime import datetime as dt
import pytz

local = dt.now()
print("Local time:", local)

# New York Timezone
ny_timezone = pytz.timezone('America/New_York')
ny_datetime = dt.now(ny_timezone)
print("New York time:", ny_datetime)

# London timezone
lon_timezone = pytz.timezone("Europe/London")
lon_datetime = dt.now(lon_timezone)
print("London time:", lon_datetime)
