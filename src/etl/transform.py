import pandas as pd

def standardize_columns(df):

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    return df


def remove_duplicates(df):

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(
        f"Duplicates Removed: {before - after}"
    )

    return df


def missing_value_report(df):

    missing = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )

    return missing