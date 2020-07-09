import yaml
import datetime
now = datetime.datetime.utcnow()
dates = {}
dates[1] = now.isoformat()
dates[2] = now.isoformat()
with open("example_date.yaml", "w") as ymlfile:
    yaml.dump(dates, ymlfile)
with open("example_date.yaml", "r") as ymlfile:
   dates = yaml.safe_load(ymlfile)
print(dates)
