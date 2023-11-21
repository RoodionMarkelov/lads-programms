import csv

class Iterator:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self._iter = self.generator()

    def generator(self):
        with open(self.csv_file, newline ="") as f:
            fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
                          'wind_evening']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in reader:
                date = row['data']
                data = {
                    "data": date,
                    "temp_morning": row['temp_morning'],
                    "presure_morning": row['presure_morning'],
                    "wind_morning": row['wind_morning'],
                    "temp_evening": row['temp_evening'],
                    "presure_evening": row['presure_evening'],
                    "wind_evening": row['wind_evening']
                }
                yield data

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            raise StopIteration

csv_file = 'dataset.csv'
_iter = Iterator(csv_file)
next_data = next(_iter)
print(next_data)
next_data = next(_iter)
print(next_data)
for data in _iter:
    try:
        next_data = next(_iter)
        if next_data:
            print(next_data)
        else:
            print("Data over.")
    except StopIteration:
        print("Data over.")
try:
    next_data = next(_iter)
    if next_data:
        print(next_data)
except StopIteration:
        print("Data over.")

