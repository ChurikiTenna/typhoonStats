import csv
import pprint
from datetime import datetime

def analyseRow(row):
    if row[3]=="日":
        datetime_object = datetime.strptime(row[5], '%H:%M')
        print('datetime_object',row[5],datetime_object.hour <= 19)
        if datetime_object.hour <= 21:
            return ['Sun','Weekend']
        else:
            return ['Sun','Weekday']
    if row[3]=="月":
        return ['Mon','Weekday']
    if row[3]=="火":
        return ['Tue','Weekday']
    if row[3]=="水":
        return ['Wed','Weekday']
    if row[3]=="木":
        return ['Thu','Weekday']
    if row[3]=="金":
        datetime_object = datetime.strptime(row[5], '%H:%M')
        if datetime_object.hour >= 19:
            return ['Fri','Weekend']
        else:
            return ['Fri','Weekday']
    if row[3]=="土":
        return ['Sat','Weekend']
    return []

with open('台風の動向.csv') as f:
    reader = csv.reader(f)
    dicts = {'Sun': 0,'Mon': 0,'Tue': 0,'Wed': 0,'Thu': 0,'Fri': 0,'Sat': 0}
    dicts_weekend = {'Weekday': 0,'Weekend': 0}
    dicts_from2017 = {'Sun': 0,'Mon': 0,'Tue': 0,'Wed': 0,'Thu': 0,'Fri': 0,'Sat': 0}
    dicts_weekend_from2017 = {'Weekday': 0,'Weekend': 0}
    dicts_okinawa = {'Sun': 0,'Mon': 0,'Tue': 0,'Wed': 0,'Thu': 0,'Fri': 0,'Sat': 0}
    dicts_weekend_okinawa = {'Weekday': 0,'Weekend': 0}
    for row in reader:
        #print(row)
        array = analyseRow(row)
        if len(array) >= 2:
            dicts[array[0]] += 1
            dicts_weekend[array[1]] += 1
            if '2017' in row[2] or '2018' in row[2] or '2019' in row[2] or '2020' in row[2] or '2021' in row[2] or '2022' in row[2]:
                dicts_from2017[array[0]] += 1
                dicts_weekend_from2017[array[1]] += 1
            if row[4] == '沖縄':
                dicts_okinawa[array[0]] += 1
                dicts_weekend_okinawa[array[1]] += 1
    print("dicts",dicts)
    print("dicts_weekend",dicts_weekend)
    print("dicts_from2017",dicts_from2017)
    print("dicts_weekend_from2017",dicts_weekend_from2017)
    print("dicts_okinawa",dicts_okinawa)
    print("dicts_weekend_okinawa",dicts_weekend_okinawa)
