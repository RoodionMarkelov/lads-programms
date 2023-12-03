import pandas as pd


def divide_by_weeks(csv_file: str):
    """Divide list by weeks and create the csv_files. Return None."""
    df = pd.read_csv(
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
    df["date"] = pd.to_datetime(df["date"])
    weeks_data = []
    for name, group in df.set_index("date").groupby(pd.Grouper(freq="W")):
        weeks_data.append(
            group.apply(
                lambda x: [
                    str(x.name)[:10],
                    str(x["temp_morning"]),
                    str(x["presure_morning"]),
                    str(x["wind_morning"]),
                    str(x["temp_evening"]),
                    str(x["presure_evening"]),
                    str(x["wind_evening"]),
                ],
                axis=1,
            ).tolist()
        )
    for week in weeks_data:
        if week:
            with open(
                f'week/{week[0][0].replace("-", "")}_{week[-1][0].replace("-", "")}.csv',
                "w",
            ) as f:
                for day in week:
                    f.write(
                        f"{day[0]},{day[1]},{day[2]},{day[3]},{day[4]},{day[5]},{day[6]}\n"
                    )
    return


if __name__ == "__main__":
    divide_by_weeks("dataset.csv")
