import csv
import os
import datetime as dt
# import pandas as pd
#
# df = pd.read_csv('dataset.csv', parse_dates=['date'], names=['date', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
#                       'wind_evening'])
# df['date'] = pd.to_datetime(df['date'])
# df = df.sort_values(by='date')
# weekly_data = []
# for name, group in df.set_index('date').groupby(pd.Grouper(freq='W')):
#     weekly_data.append(group.apply(lambda x: [str(x.name)[:10], str(x['temp_morning']), str(x['presure_morning']), str(x['wind_morning']), str(x['temp_evening']), str(x['presure_evening']), str(x['wind_evening'])], axis=1).values.tolist())
#
#
# def split_by_weeks(weeks_data) -> None:
#     for week in weeks_data:
#         if week:
#             with open(f'week/{week[0][0].replace("-", "")}_{week[-1][0].replace("-", "")}.csv', 'w') as f:
#                 for day in week:
#                     f.write(f'{day[0]},{day[1]}\n')
#
#
# if __name__ == "__main__":
#     split_by_weeks(weekly_data)
with open('dataset.csv', newline='') as file:
    fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
                  'wind_evening']
    reader = csv.DictReader(file, fieldnames=fieldnames)
    week_start = None
    week_number = 1
    week_data = []
    for row in reader:
        date = dt.datetime.strptime(row['data'], '%Y-%m-%d')
        day_of_week = date.weekday()
        if(row['data'][:4] == '1998' or row['data'][:4] == '2000'):
            week_data.append(
                [row['data'], row["temp_morning"], row["presure_morning"], row["wind_morning"], row["temp_evening"],
                 row["presure_evening"], row["wind_evening"]])
            output_folder = 'week'
            os.makedirs(output_folder, exist_ok=True)
            output_file = os.path.join(output_folder, f'week-{week_number}.csv')

            with open(output_file, 'w', newline='') as file_writer:
                writer = csv.writer(file_writer, lineterminator="\r")
                for week_data in week_data:
                    writer.writerow(week_data)

            week_number += 1
            week_start = None
            week_data = []
            continue

        if week_start is None:
            week_start = date - dt.timedelta(days=day_of_week)

        if day_of_week == 6:
            output_folder = 'week'
            os.makedirs(output_folder, exist_ok=True)
            output_file = os.path.join(output_folder, f'week-{week_number}.csv')

            with open(output_file, 'w', newline='') as file_writer:
                writer = csv.writer(file_writer, lineterminator="\r")
                for week_data in week_data:
                    writer.writerow(week_data)

            week_number += 1
            week_start = None
            week_data = []

        week_data.append(
            [row['data'], row["temp_morning"], row["presure_morning"], row["wind_morning"], row["temp_evening"],
             row["presure_evening"], row["wind_evening"]])