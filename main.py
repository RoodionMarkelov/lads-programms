from bs4 import BeautifulSoup
import requests
import csv
import os
import datetime as dt

# for year in range(1997, 2024):
#     for mouths in range(1, 13):
#
#         url = "https://www.gismeteo.ru/diary/4618/" + str(year) + "/" + str(mouths) + "/"
#
#         headers = {
#                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"
#         }
#
#         req = requests.get(url, headers=headers)
#         src = req.text
#         try:
#             with open("cite.html", "w") as file:
#                 file.write(src)
#         except Exception:
#             continue
#
#             # with open("cite.html") as file:
#             #     src = file.read()
#
#         soup = BeautifulSoup(src, "lxml")
#         try:
#             tab = soup.find("table").find("tbody").find_all("tr")
#         except Exception:
#             continue
#
#         data_from_table = []
#         if(mouths < 10):
#             moun = '0' + str(mouths)
#         else: moun = str(mouths)
#         for item in tab:
#             data_from_table_td = item.find_all('td')
#             data = data_from_table_td[0].text
#             if (len(data) == 1):
#                 data = '0' + data
#             temp_morning = data_from_table_td[1].text
#             pres_morning = data_from_table_td[2].text
#             wind_morning = data_from_table_td[5].text
#             temp_evening = data_from_table_td[6].text
#             pres_evening = data_from_table_td[7].text
#             wind_evening = data_from_table_td[10].text
#
#             data_from_table.append(
#                 {
#                     "data": str(year) + "-" + moun + "-" + data,
#                     "temp_morning": temp_morning,
#                     "presure_morning": pres_morning,
#                     "wind_morning": wind_morning,
#                     "temp_evening": temp_evening,
#                     "presure_evening": pres_evening,
#                     "wind_evening": wind_evening
#                 }
#             )
#
#         with open('dataset.csv', 'a', newline='') as csvfile:
#             for item in data_from_table:
#                file_writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
#                file_writer.writerow([item["data"], item["temp_morning"], item["presure_morning"], item["wind_morning"], item["temp_evening"], item["presure_evening"], item["wind_evening"]])
#
# with open('dataset.csv', newline='') as f:
#     fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind']
#     reader = csv.DictReader(f, fieldnames=fieldnames)
#     for row in reader:
#         file_writer = csv.writer(open('dataset-number.csv', 'a', newline=''), lineterminator="\r")
#         file_writer.writerow([row['data']])
#         file_writer = csv.writer(open('dataset-meteodate.csv', 'a', newline=''), lineterminator="\r")
#         file_writer.writerow([row['temp_morning'], row['presure_morning'], row['wind_morning'], row['temp_evening'], row['presure_evening'], row['wind']])

# for year in range(1997, 2024):
#     output_file = f'{year}.csv'
#     output_folder = 'years'
#     os.makedirs(output_folder, exist_ok=True)
#     output_file = os.path.join(output_folder, output_file)
#     with open('dataset.csv', newline='') as f:
#         fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
#                       'wind_evening']
#         reader = csv.DictReader(f, fieldnames=fieldnames)
#         with open(output_file, 'w', newline='') as file_writer:
#             writer = csv.writer(file_writer, lineterminator="\r")
#             for row in reader:
#                 year_in_row = row['data'].split('-')[0]
#                 if year_in_row == str(year):
#                     writer.writerow([row['data'], row["temp_morning"], row["presure_morning"], row["wind_morning"],row["temp_evening"], row["presure_evening"], row["wind_evening"]])
#
#
# for year in range(1997, 2024):
#     input_file = f'years/{year}.csv'
#     with open(input_file, 'r', newline='') as file:
#         fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
#                       'wind_evening']
#         reader = csv.DictReader(file, fieldnames=fieldnames)
#         try:
#             first_row = next(reader)
#         except Exception:
#             file.close()
#             os.remove(input_file)
#             continue
#         year = first_row['data'][:4]
#         first_date = first_row['data'][5:7] + first_row['data'][8:10]
#         last_date = None
#         for row in reader:
#             last_date = row['data'][5:7] + row['data'][8:10]
#         if last_date is None:
#             last_date = first_date
#         if last_date:
#             output_file = f'years/{year}{first_date}-{year}{last_date}.csv'
#             file.close()
#             os.rename(input_file, output_file)

# with open('dataset.csv', newline='') as file:
#     fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
#                   'wind_evening']
#     reader = csv.DictReader(file, fieldnames=fieldnames)
#     week_start = None
#     week_number = 1
#     week_data = []
#     for row in reader:
#         date = dt.datetime.strptime(row['data'], '%Y-%m-%d')
#         day_of_week = date.weekday()
#
#         if week_start is None:
#             week_start = date - dt.timedelta(days=day_of_week)
#
#         if day_of_week == 6:
#
#             output_folder = 'week'
#             os.makedirs(output_folder, exist_ok=True)
#             output_file = os.path.join(output_folder, f'week-{week_number}.csv')
#
#             with open(output_file, 'w', newline='') as file_writer:
#                 writer = csv.writer(file_writer, lineterminator="\r")
#
#                 for week_data in week_data:
#                     writer.writerow(week_data)
#
#             week_number += 1
#             week_start = None
#             week_data = []
#
#         week_data.append(
#             [row['data'], row["temp_morning"], row["presure_morning"], row["wind_morning"], row["temp_evening"],
#              row["presure_evening"], row["wind_evening"]])

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

csvfile = 'years/20170101-20171231.csv'
target_date = '2017-07-07'
date = get_date_from_file(target_date, csvfile)
print(date)