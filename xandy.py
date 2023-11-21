import csv

def divide_on_x_y(csv_file):
    with open(csv_file, newline='') as f:
        fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in reader:
            file_writer = csv.writer(open('dataset-number.csv', 'a', newline=''), lineterminator="\r")
            file_writer.writerow([row['data']])
            file_writer = csv.writer(open('dataset-meteodata.csv', 'a', newline=''), lineterminator="\r")
            file_writer.writerow([row['temp_morning'], row['presure_morning'], row['wind_morning'], row['temp_evening'], row['presure_evening'], row['wind']])

if __name__ == '__main__':
    divide_on_x_y('dataset.csv')