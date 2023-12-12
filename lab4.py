import pandas as pd
import datetime
import matplotlib.pyplot as plt


def create_DataFrame(csv_file: str)-> pd.DataFrame:
    """
    Создание pd.DataFrame.
    :param csv_file:
    :return:
    """
    DataFrame = pd.read_csv(
        csv_file,
        names=[
            "date",
            "temp_morning",
            "presure_morning",
            "wind_morning",
            "temp_evening",
            "presure_evening",
            "wind_evening",
        ],
        dtype=str,
    )
    DataFrame["temp_morning"] = pd.to_numeric(
        DataFrame["temp_morning"].str.replace("+", ""), errors="coerce"
    )
    DataFrame["temp_evening"] = pd.to_numeric(
        DataFrame["temp_evening"].str.replace("+", ""), errors="coerce"
    )
    return DataFrame


def data_processing(DataFrame: pd.DataFrame)-> pd.DataFrame:
    """
    Обработка значений 'nan' в pd.DataFrame. Заменяет 'nan' на среднее значение в колонке.
    :param DataFrame:
    :return pd.DataFrame:
    """
    average = round((DataFrame["temp_morning"].mean() + DataFrame["temp_evening"].mean()) / 2, 1)
    DataFrame = DataFrame.fillna(average)
    return DataFrame


def temp_to_fahrenheit(temperature: float)->float:
    """
    Переводит температуры из Градусов Цельсия в градусы Фаренгейта.
    :param temperature:
    :return float:
    """
    return (float(temperature) * 9 / 5) + 32


def create_temp_f(DataFrame: pd.DataFrame)-> pd.DataFrame:
    """
    Создает колонки со значениями температуры по шкале Фаренгейта.
    :param DataFrame:
    :return pd.DataFrame:
    """
    DataFrame["temp_morning_f"] = DataFrame["temp_morning"].apply(temp_to_fahrenheit)
    DataFrame["temp_evening_f"] = DataFrame["temp_evening"].apply(temp_to_fahrenheit)
    return DataFrame


def get_stats(DataFrame: pd.DataFrame, column: str)-> None:
    """
    Возращает статиску по колонке.
    :param DataFrame:
    :param column:
    :return None:
    """
    try:
        return print(DataFrame[column].describe())
    except KeyError:
        print("Error")
    return None


def filter_by_temp(DataFrame: pd.DataFrame, column: str, temp: float)-> pd.DataFrame:
    """
    Фильтрует pd.DataFrame по переданной температуре.
    :param DataFrame:
    :param column:
    :param temp:
    :return pd.DataFrame:
    """
    DataFrame = DataFrame[DataFrame[column] >= temp]
    return DataFrame


def filter_by_date(DataFrame: pd.DataFrame, date_start: str, date_end: str)-> pd.DataFrame:

    """
    Фильтрует pd.DataFrame по переданному диапозону даты.
    :param DataFrame:
    :param date_start:
    :param date_end:
    :return pd.DataFrame:
    """
    DataFrame["date"] = pd.to_datetime(DataFrame["date"])
    date1 = datetime.datetime.strptime(date_start, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date_end, "%Y-%m-%d")
    return DataFrame[
        (pd.to_datetime(DataFrame["date"]) >= date1)
        & (pd.to_datetime(DataFrame["date"]) <= date2)
    ]


def group_by_mounth(DataFrame: pd.DataFrame):
    """
    Групирует pd.DataFrame по месяцам. Возвращает list.
    :param DataFrame:
    :return list:
    """
    DataFrame["date"] = pd.to_datetime(DataFrame["date"])
    mounth_data = []
    for name, group in df.set_index("date").groupby(pd.Grouper(freq="M")):
        mounth_data.append(group)
    return mounth_data


def calculate_average(DataFrame: pd.DataFrame, column: str):
    """
    Подсчитывает среденнее по месяцам. Возвращает list.
    :param DataFrame:
    :param column:
    :return list:
    """
    month_data = group_by_mounth(DataFrame)
    averages = []
    for mounth_df in month_data:
        avg_temperature = mounth_df[column].mean()
        averages.append(avg_temperature)
    return averages


def get_graph(DataFrame: pd.DataFrame):
    """
    Рисует графики для всего периода.
    :param DataFrame:
    :return None:
    """
    x = DataFrame["date"]
    y1 = DataFrame["temp_morning"]
    y2 = DataFrame["temp_morning_f"]
    y3 = DataFrame["temp_evening"]
    y4 = DataFrame["temp_evening_f"]
    plt.figure(figsize=(25, 25))
    plt.ylabel("Температура")
    plt.xlabel("День")
    plt.title("График температуры")
    plt.plot(
        x,
        y1,
        color="green",
        linestyle="-",
        marker="o",
        linewidth=1,
        markersize=2,
        label="Температура днем по Цельсию",
    )
    plt.plot(
        x,
        y2,
        color="red",
        linestyle="-",
        marker="o",
        linewidth=1,
        markersize=2,
        label="Температура днем по Фаренгейту",
    )
    plt.plot(
        x,
        y3,
        color="blue",
        linestyle="-",
        marker="o",
        linewidth=1,
        markersize=2,
        label="Температура ночью по Цельсию",
    )
    plt.plot(
        x,
        y4,
        color="black",
        linestyle="-",
        marker="o",
        linewidth=1,
        markersize=2,
        label="Температура ночью по Фаренгейту",
    )
    plt.legend()
    plt.show()


def get_graph_for_date(DataFrame: pd.DataFrame, mounth: int, year: int):
    """
    Рисует график для pd.DataFrame для заданного периода.
    :param DataFrame:
    :param mounth:
    :param year:
    :return None:
    """
    DataFrame["Year"] = DataFrame["date"].dt.year
    DataFrame["Month"] = DataFrame["date"].dt.month
    DataFrame["Day"] = DataFrame["date"].dt.day
    data_for_date = DataFrame[(DataFrame["Year"] == year) & (df["Month"] == mounth)]
    median_morning_temp = data_for_date["temp_morning"].median()
    mean_morning_temp = data_for_date["temp_morning"].mean()
    median_morning_f_temp = data_for_date["temp_morning_f"].median()
    mean_morning_f_temp = data_for_date["temp_morning_f"].mean()
    median_evening_temp = data_for_date["temp_evening"].median()
    mean_evening_temp = data_for_date["temp_evening"].mean()
    median_evening_f_temp = data_for_date["temp_evening_f"].median()
    mean_evening_f_temp = data_for_date["temp_evening_f"].mean()
    fig = plt.figure(figsize=(25, 25))
    plt.title("Изменение температуры для переданной даты")
    fig.add_subplot(2, 2, 1)
    plt.plot(
        data_for_date["Day"],
        data_for_date["temp_morning"],
        label="Температура днем по Цельсию",
    )
    plt.axhline(median_morning_temp, color="red", linestyle="--", label="Медиана")
    plt.axhline(mean_morning_temp, color="green", linestyle="--", label="Среднее")
    plt.legend(loc=1, prop={"size": 5})
    plt.xlabel("День")
    plt.ylabel("Температура")

    fig.add_subplot(2, 2, 2)
    plt.plot(
        data_for_date["Day"],
        data_for_date["temp_morning_f"],
        label="Температура днем по Фаренгейту",
    )
    plt.axhline(median_morning_f_temp, color="red", linestyle="--", label="Медиана")
    plt.axhline(mean_morning_f_temp, color="green", linestyle="--", label="Среднее")
    plt.legend(loc=1, prop={"size": 5})
    plt.xlabel("День")
    plt.ylabel("Температура")

    fig.add_subplot(2, 2, 3)
    plt.plot(
        data_for_date["Day"],
        data_for_date["temp_evening"],
        label="Температура ночью по Цельсию",
    )
    plt.axhline(median_evening_temp, color="red", linestyle="--", label="Медиана")
    plt.axhline(mean_evening_temp, color="green", linestyle="--", label="Среднее")
    plt.legend(loc=1, prop={"size": 5})
    plt.xlabel("День")
    plt.ylabel("Температура")

    fig.add_subplot(2, 2, 4)
    plt.plot(
        data_for_date["Day"],
        data_for_date["temp_evening_f"],
        label="Температура ночью по Фаренгейту",
    )
    plt.axhline(median_evening_f_temp, color="red", linestyle="--", label="Медиана")
    plt.axhline(mean_evening_f_temp, color="green", linestyle="--", label="Среднее")
    plt.legend(loc=1, prop={"size": 5})
    plt.xlabel("День")
    plt.ylabel("Температура")

    plt.show()


if __name__ == "__main__":
    print("Функция 1")
    df = create_DataFrame("dataset.csv")
    print(df)

    print("Функция 2")
    df = data_processing(df)
    print(df)

    print("Функция 3")
    df = create_temp_f(df)
    print(df)

    print("Функция 4")
    get_stats(df, "temp_morning")
    get_stats(df, "temp_evening")
    get_stats(df, "temp_morning_f")
    get_stats(df, "temp_evening_f")

    print("Функция 5")
    res_df1 = filter_by_temp(df, "temp_morning", 0)
    print(res_df1)
    res_df2 = filter_by_temp(df, "temp_evening", 0)
    print(res_df2)

    print("Функция 6")
    res_df3 = filter_by_date(df, "2022-01-01", "2022-12-31")
    print(res_df3)

    print("Функция 7")
    average = calculate_average(df, "temp_morning")
    print(average)

    print("Функция 8")
    get_graph(df)

    print("Функция 9")
    get_graph_for_date(df, 12, 2022)
