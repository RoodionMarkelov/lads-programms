from bs4 import BeautifulSoup
import requests
import csv

# url = "https://www.gismeteo.ru/diary/4618/2023/9/"
#
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)
#
# with open("index.html", "w") as file:
#     file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# table_data = soup.find("table").find("td", class_="first").text
# table_temp = soup.find("table").find("td", class_="first_in_group positive").text
# table_presure = soup.find("table").find("td", class_="first_in_group positive").find_next().text
# table_wind = soup.find("table").find("span").text
# print(table_data)
# print(table_temp)
# print(table_presure)
# print(table_wind)

table = soup.find("table").text
with open('dataset.csv', 'w', newline='') as csvfile:
    for item in table:
        table_data = soup.find("table").find("td", class_="first").text
        table_temp = soup.find("table").find("td", class_="first_in_group positive").text
        table_presure = soup.find("table").find("td", class_="first_in_group positive").find_next().text
        table_wind = soup.find("table").find("span").text
        file_writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        file_writer.writerow([table_data, table_temp, table_presure, table_wind])