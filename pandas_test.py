#!/usr/bin/env python3


import datetime
import json
import os
import pandas as pd


def dataframe_from_directory(dirs):
    dfs = []
    for directory in dirs:
        if not os.path.exists(directory):
            continue
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if not os.path.isfile(path):
                continue
            df = pd.read_json(path, lines=True)
            dfs.append(df)
    if not dfs:
        return None
    df = pd.concat(dfs, sort=False, ignore_index=True)
    return df


def create_file():
    fp = open("test.json", "w")
    fp.write("""{"ad_network": "admob", "unit_id": "id1", "country": "CN", "revenue": 120, "impression": 245322}
{"ad_network": "admob", "unit_id": "id1", "country": "US", "revenue": 200, "impression": 356824}
{"ad_network": "admob", "unit_id": "id2", "country": "US", "revenue": 50, "impression": 187098}
{"ad_network": "facebook", "unit_id": "id3", "country": "CN", "revenue": 250, "impression": 609789}
{"ad_network": "facebook", "unit_id": "id3", "country": "JP", "revenue": 300, "impression": 409878}
""")
    fp.close()
    fp = open("test2.json", "w")
    fp.write("""{"ad_network": "admob", "user": 54381}
{"ad_network": "facebook", "user": 86539}
""")
    fp.close()


def delete_file():
    os.remove("test.json")
    os.remove("test2.json")
    os.remove("test.xlsx")


def read_test():
    df = pd.read_json("test.json", lines=True)
    print(df)
    print(df.to_json(orient="records", lines=True))
    print(df.to_csv(encoding="utf-8"))
    print(df.to_html())
    writer = pd.ExcelWriter("test.xlsx")
    df.to_excel(writer, "sheet1", index=False)
    writer.save()


def select_column_test():
    df = pd.read_json("test.json", lines=True)
    df = df[["ad_network", "country", "revenue"]]
    print(df)


def select_row_test():
    df = pd.read_json("test.json", lines=True)
    df = df.loc[
        (df["ad_network"] == "admob") &
        ((df["country"] == "CN") | (df["country"] == "US"))
    ]
    print(df)


def drop_row_test():
    df = pd.read_json("test.json", lines=True)
    df = df.drop(df.loc[df["country"] == "CN"].index)
    print(df)


def drop_column_test():
    df = pd.read_json("test.json", lines=True)
    df = df.drop(["impression", "unit_id"], axis=1)
    print(df)


def rename_column_test():
    df = pd.read_json("test.json", lines=True)
    df = df.rename(columns={"revenue": "revenue_usd"})
    print(df)


def update_condation_test():
    df = pd.read_json("test.json", lines=True)
    # set reveune = revenue / 6.7 where country is CN
    df.loc[df["country"] == "CN", "revenue"] = df["revenue"] / 6.7
    print(df)


def new_column_test():
    df = pd.read_json("test.json", lines=True)
    df["ecpm"] = df["revenue"] * 1000 / df["impression"]
    print(df)
    df["ecpm_format"] = df["ecpm"].apply(
        lambda x: "{}%".format(round(x * 100, 4))
    )
    print(df)


def groupby_test():
    df = pd.read_json("test.json", lines=True)
    # sum group by ad_network, country
    df1 = df.groupby([
        "ad_network", "country",
    ], as_index=False).sum()
    print(df1)
    df2 = df.groupby([
        "ad_network",
    ], as_index=False).agg({
        "revenue": ["mean", "max", "sum"],
        "impression": ["min"],
    })
    print(df2)


def sort_test():
    df = pd.read_json("test.json", lines=True)
    # order by country, revenue desc
    df = df.sort_values(by=[
        "country", "revenue"
    ], ascending=[True, False])
    print(df)


def merge_test():
    df1 = pd.read_json("test.json", lines=True)
    df2 = pd.read_json("test2.json", lines=True)
    # df1 left join df2
    df = pd.merge(df1, df2, how="left")
    print(df)


def type_test():
    df = pd.read_json("test.json", lines=True)
    # datetime
    df["@timestamp"] = "2019-01-15T00:00:00"
    df["date"] = pd.to_datetime(df["@timestamp"])
    df["date"] -= datetime.timedelta(days=2)
    # astype
    df = df.astype({
        "revenue": float, "impression": int,
    })
    print(df)


def fillna_test():
    df1 = pd.read_json("test.json", lines=True)
    df2 = pd.read_json("test2.json", lines=True)
    df2 = df2.drop(df2.loc[df2["ad_network"] == "facebook"].index)
    df = pd.merge(df1, df2, how="left")
    # set user=0 where user is nan
    df.loc[df["user"].isna(), "user"] = 0
    print(df)


def main():
    create_file()
    # read_test()
    # select_column_test()
    # select_row_test()
    # drop_row_test()
    # drop_column_test()
    # update_condation_test()
    # rename_column_test()
    # new_column_test()
    # groupby_test()
    # sort_test()
    # merge_test()
    # type_test()
    fillna_test()
    delete_file()


if __name__ == "__main__":
    main()
