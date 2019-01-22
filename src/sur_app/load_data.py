import csv
from sur_app.models import AdultData

with open('../audit_data.csv', r) as ip_file:
    reader = csv.reader(ip_file)
    for row in reader:
        _, created = AdultData.objects.get_or_create(
            age = int(row[0]),
            work_class = row[1],
            fnlwgt = int(row[2]),
            education = row[3],
            ed_no = int(row[4]),
            marital_status = row[5],
            occupation = row[6],
            relationship = row[7],
            race = row[8],
            sex = row[9],
            capital_gain = int(row[10]),
            caplital_loss = introw([11]),
            hours_per_week = int(row[12]),
            native_country = row[13],
            income = row[14]
        )
