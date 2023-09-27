from bs4 import BeautifulSoup
import requests
import csv

for year in range(2022, 2024):
    for mouths in range(1, 13):

        url = "https://www.gismeteo.ru/diary/4618/" + str(year) + "/" + str(mouths) + "/"

        headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"
        }

        req = requests.get(url, headers=headers)
        src = req.text


        with open("index.html", "w") as file:
            file.write(src)

            # with open("index.html") as file:
            #     src = file.read()

        soup = BeautifulSoup(src, "lxml")
        try:
            tab = soup.find("table").find("tbody").find_all("tr")
        except Exception:
            continue

        data_from_table = []
        for item in tab:
            data_from_table_td = item.find_all('td')
            data = data_from_table_td[0].text
            temp_morning = data_from_table_td[1].text
            pres_morning = data_from_table_td[2].text
            wind_morning = data_from_table_td[5].text
            temp_evening = data_from_table_td[6].text
            pres_evening = data_from_table_td[7].text
            wind_evening = data_from_table_td[10].text

            data_from_table.append(
                {
                    "day": data + "." + str(mouths) + "." + str(year),
                    "temp_morning": temp_morning,
                    "presure_morning": pres_morning,
                    "wind_morning": wind_morning,
                    "temp_evening": temp_evening,
                    "presure_evening": pres_evening,
                    "wind_evening": wind_evening
                }
            )

        with open('dataset.csv', 'a', newline='') as csvfile:
            for item in data_from_table:
                file_writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
                file_writer.writerow([item])