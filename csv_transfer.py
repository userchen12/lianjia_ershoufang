import csv
import re
file = csv.reader(open('ljesf.csv'))
for row in file:
    location = row[5].split(',')
    if len(location)  == 2:
        lng = location[0]
        lat = location[1]
        pattern = re.compile('\d+')
        count = re.findall(pattern,row[4])[0]
        output = '{\"lng\":'+lng+',\"lat\":'+lat+',\"count\":'+count+'},'
        print(output)
