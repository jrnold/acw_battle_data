import csv
import yaml

with open("reiter2009_turning_points.yaml", "r") as f:
    data = yaml.load(f)

with open("reiter2009_turning_points.csv", "w") as f:
    writer = csv.DictWriter(f, ("period", "start_date", "description", "favor", "war_aims_change", "comment"))
    writer.writeheader()
    writer.writerows(data)
