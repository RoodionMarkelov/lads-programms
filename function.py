import csv
def get_date_from_file(target_date, csvfile):
    with (open(csvfile, newline="") as f):
        fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in reader:
            date = row['data']
            if (date == target_date):
                return{
                        "date": row['data'],
                        "temp_morning": row['temp_morning'],
                        "presure_morning": row['presure_morning'],
                        "wind_morning": row['wind_morning'],
                        "temp_evening": row['temp_evening'],
                        "presure_evening": row['presure_evening'],
                        "wind_evening": row['wind_evening']
                }
    return None

csvfile1 = 'years/20170101-20171231.csv'
target_date1 = '2017-07-07'
date = get_date_from_file(target_date1, csvfile1)
if date is None:
    print("Data is not exsist")
if date:
    print("Data is:")
    print(date)

csvfile2 = 'dataset.csv'
target_date2 = '2013-07-07'
date2 = get_date_from_file(target_date2, csvfile2)
if date2 is None:
    print("Data is not exsist")
if date2:
    print("Data is:")
    print(date2)

csvfile3 = 'week/week-15.csv'
target_date3 = '2008-04-12'
date1 = get_date_from_file(target_date3, csvfile3)
if date1 is None:
    print("Data is not exsist")
if date1:
    print("Data is:")
    print(date1)