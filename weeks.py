import pandas as pd

def group_by_week(csv_file:str):
    '''The data from the file is grouped by week. Return list'''
    df = pd.read_csv(csv_file, names=['date', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind_evening'], dtype=str)
    df['date'] = pd.to_datetime(df['date'])
    weekly_data = []
    for name, group in df.set_index('date').groupby(pd.Grouper(freq='W')):
        weekly_data.append(group.apply(lambda x: [str(x.name)[:10], str(x['temp_morning']), str(x['presure_morning']), str(x['wind_morning']), str(x['temp_evening']), str(x['presure_evening']), str(x['wind_evening'])], axis=1).tolist())
    return weekly_data

def divide_by_weeks(weeks_data:list) -> None:
        '''Divide list by weeks and create the csv_files. Return None.'''
        for week in weeks_data:
            if week:
                with open(f'week/{week[0][0].replace("-", "")}_{week[-1][0].replace("-", "")}.csv', 'w') as f:
                    for day in week:
                        f.write(f'{day[0]},{day[1]},{day[2]},{day[3]},{day[4]},{day[5]},{day[6]}\n')


if __name__ == "__main__":
    data = group_by_week('dataset.csv')
    divide_by_weeks(data)

